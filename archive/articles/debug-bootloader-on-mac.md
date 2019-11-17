Macでbootloader周辺をデバッグする方法
2019-03-09


この\a{os-tutorial}{https://github.com/cfenollosa/os-tutorial}をもとにbootloaderを作っていたのだが、このTutorialにはそのデバッグ方法が書かれていなかった。自分が使用しているPCがMacで動いていたこともあって色々とつまるところがあったので、最終的にどのような開発環境を整えてどのようにデバッグしていくようになったのかをメモする。


# 開発環境


あとで述べる様々な理由によりこの開発は仮想環境の上で行うことにした。仮想環境はVagrantで作成することとして、使用しているboxは32bitのUbuntuである。
\code{
MacBook-Pro$ vagrant box list
ubuntu/trusty32 (virtualbox, 20190226.0.1)
MacBook-Pro$ vagrant init ubuntu/trusty32
MacBook-Pro$ vagrant up
MacBook-Pro$ vagrant ssh
}
今の所bootloaderはos-tutorialになぞってnasmで開発しているので、とりあえずnasmは開発に必須。
\code{
vagrant@vagrant-ubuntu-trusty-32:~$ sudo apt update
vagrant@vagrant-ubuntu-trusty-32:~$ sudo apt install nasm
}
あとはbootloaderを実行するための仮想環境を用意してくれるqemuを入れておく。
\code{
vagrant@vagrant-ubuntu-trusty-32:~$ sudo apt install qemu
}
最後にデバッグ用のgdbを入れておく
\code{
vagrant@vagrant-ubuntu-trusty-32:~$ sudo apt install gdb
}
これで開発に必要な最低限の環境は整った。


# 開発


次のようなbootloaderを作成したとして開発とデバッグの手順を記していく。
\code{
vagrant@vagrant-ubuntu-trusty-32:~$ vim boot.asm
vagrant@vagrant-ubuntu-trusty-32:~$ cat boot.asm
mov ah, 0x0e
mov al, 'A'
int 0x10
jmp $
times 510 - ($-$$) db 0
dw 0xaa55
}
このコードは \a{Bios interrupt call}{https://en.wikipedia.org/wiki/BIOS_interrupt_call}を使って画面に'A'という文字を出力するプログラムになっている[1]。


実際にbootloaderを動かしてみて、文字が出力されていることを確認したい場合には
\code{
vagrant@vagrant-ubuntu-trusty-32:~$ nasm -f bin -o boot boot.asm
vagrant@vagrant-ubuntu-trusty-32:~$ qemu-system-i386 -nographic -curses boot
}
とすれば画面がbootloaderの画面(TUI)に変わり、こんな感じの画面が出力されることになると思う。
\code{
SeaBIOS (version 1.7.4-20150827_223240-lgw01-56)
iPXE (http://ipxe.org) 00:03.0 C900 PCI2.10 PnP PMM+07FC10F0+07F210F0 C900
Booting from Hard Disk...
A
}
そして、確かに'A'という文字が出力されているのがわかる。bootloaderを閉じたい場合にはその画面上で一度ESCと2をおし、次にqを押せば終了することができる[2]。


ここで注意しないければならないのが、qemuのオプションの順番には気をつけなければならないようだということだ。上記のように'-curses'を後に持って来れば問題ないのだが、先に持ってくる
\code{
vagrant@vagrant-ubuntu-trusty-32:~$ qemu-system-i386 -curses -nographic boot
}
とTUIに変わらず停止してしまう。理由はよくわからないがそのような挙動をすることだけは確認してある。このようにしてvagrantによる仮想環境上で開発を行っていくことができる。


# デバッグ準備


デバッグはgdbを使って行う。一つのTerminalをつかってvagrant上でbootloaderを動かしておく。
\code{
MacBook-Pro$ vagrant ssh
vagrant@vagrant-ubuntu-trusty-32:~$ qemu-system-i386 boot -nographic -s -S
}
'-S'オプションをつけることで起動プロセスが勝手に進んでしまうのを防ぎ、'-s'オプションをつけることで1234ポートでgdbからの接続を待つことができる。ただしデバッグ中に'-curses'オプションを使ってTUIを開くことはできなさそうなので、そのオプションはつけていない。もう一つのTerminal画面を開いてvagrant上でgdbを使用して、その1234ポートに接続する。
\code{
MacBook-Pro$ vagrant ssh
vagrant@vagrant-ubuntu-trusty-32:~$ gdb
(gdb) target remote localhost:1234
Remote debugging using localhost:1234
0x0000fff0 in ?? ()
}
最後にデバッグ対象のarchitectureを設定して、どのようにdisassembleをするかなどを定めておく。今回はbootloaderがデバッグ対象なので、\a{Intel 8086 CPU}{https://en.wikipedia.org/wiki/Intel_8086}と同じ動き方をされる前提で起動するはずなので
\code{
(gdb) set architecture i8086
The target architecture is assumed to be i8086
}
と設定しておく。


# デバッグ


gdbを使って内部の動きをさまざま追うことができる。
\ul
{今現在のレジスタの状態を見たいときは
\code{
(gdb) info registers
eax            0x0	0
ecx            0x0	0
...
}
とすれば全てのレジスタの中身の値を見ることができる。それぞれの行はレジスタの名前、16進数の値、10進数の値の順番で表示されている。同様に\emp{info reg}などと省略することもできる。}
{プログラム上でどのような指示が出されているかはdisassembleコマンドを使って確認することができる。例えば、今現在のCSレジスタの値が\emp{0xf000}で、EIPレジスタの値が\emp{0xfff0}の時
\code{
(gdb) info reg
...
eip            0xfff0	0xfff0
...
cs             0xf000	61440
...
}
に、次に実行される指示を確認したい場合を考える。bootloaderの最初の方では、次に実行される指示の番地は
\code{
<次の指示の番地> = cs * 0x10 + ip
}
と計算されるので、この場合に次に実行される番地は\emp{0xffff0}となる。そこから次の一バイト分の指示を取り出して、disassembleして見ると
\code{
(gdb) disassemble 0xffff0,+0x01
Dump of assembler code from 0xffff0 to 0xffff1:
   0x000ffff0:	ljmp   $0xf000,$0xe05b
}
となり、次に実行される指示は\emp{0xf000 * 0x10 + 0xe05b = 0xfe05b}番地にjumpせよという指示であることがわかる。}
{他には break point を設定することができる。例えば\emp{0x7c00}番地にくるまで実行して見たい場合に、まず break point を設定して
\code{
(gdb) b *0x7c00
}
そこにくるまで実行すると、実際にその番地の指示が実行される前まで実行されることがわかる。
\code{
(gdb) c
(gdb) info reg
...
eip            0x7c00	0x7c00
...
cs             0x0	0
...
}}


# Mac上で直接bootloaderを開発する際の難点


ここまでで紹介した開発方法はvagrantで作成された仮想環境の上でさらに仮想環境を作るqemuを走らせるというものだった。本当なら直接Mac上で開発を行いところだったのだが、下記の理由で断念した。


\ul
{gdbをMac上にインストールするのが難しい。比較的新しいMacOSならば基本的にgdbを使うことは推奨されておらず、lldbを使用することが推奨されている。gdbを無理やり使おうと思うとgdbに対してセキュリティ的な認証をせねばらなず手間がかかる[3]。その上、新しいgdbはMac上では動かず少し古いバージョンのものを強制的に入れる必要がある[4]。色々と手間がかかりすぎる上に明らかにMac上でgdbを動かせるようにできていないのであまり無理やり動かせるようにしても将来どうなるかはわからない。}
{lldbでqemuと連携する方法がわからない。lldbとqemuを連携させる方法がどこにも書かれておらず、考えつく方法を色々と試して見たが全てうまくいかなかった。関連しそうなリソースとしてはこのlldbのメーリングリストのスレッド[5]などがあったが、あまり参考にはならない。}


# 参考


\ol
{https://github.com/cfenollosa/os-tutorial/blob/master/02-bootsector-print/boot_sect_hello.asm}
{https://serverfault.com/questions/730355/qemu-running-in-ssh-how-to-exit}
{https://qiita.com/yuzu_afro/items/988020dd65fb4f43962a}
{https://stackoverflow.com/questions/49222683/how-do-i-install-gdb-on-macos-10-13-3-high-sierra}
{http://lists.llvm.org/pipermail/lldb-dev/2014-February/003318.html}

