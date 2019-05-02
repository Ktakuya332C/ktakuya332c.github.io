bootloaderからC言語のコードを呼ぶ
2019-03-16


bootloader内でassemblyからC言語のコードを呼ぶことができたのでメモする。


# 調査用コード


調査用コードは\a{Gist}{https://gist.github.com/Ktakuya332C/881eb08b8adcdbef299afc6bf18fa0be}にアップロードしておいた。


それぞれのファイルの役割は
\ul
{boot.S: BIOSから最初に呼び出されるスクリプト。16-bit real mode から 32-bit protected mode に動作方法を変換し、main.cのbootmain関数を呼び出す}
{main.c: 無限ループをする関数bootmainを定義しているスクリプト。}
{sign.pl: 任意のバイナリファイルを読み取り、510バイト以下なら510バイトになるように0を付け足した上で最後にbootloaderであることを示すマジックナンバーであるAA55を付け足すスクリプト。}


# 調査準備


まず、\a{Macでbootloader周辺をデバッグする方法}{\rel{debug-bootloader-on-mac.html}}の通りに環境構築を行う。


次に、今回調査を行うためのスクリプトをコンパイルする。まずはassemblyのスクリプトであるboot.Sをコンパイルする。
\code{
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ as boot.S -o boot.o
}
次に、C言語のスクリプトであるmain.cをコンパイルする。この時\emp{-ffreestanding}フラグをつけることで標準ライブラリなどが入り込まないようにし、コンパイルしている環境に依存しないようにする。
\code{
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ gcc -ffreestanding -c main.c -o main.o
}
そしてそれら二つのオブジェクトファイル(boot.oとmain.o)をリンクする。bootloaderは必ず0x7c00番地からロードされるので引数には\emp{-Ttext 0x7c00}を渡している。
\code{
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ ld -Ttext 0x7c00 --oformat=binary --entry start boot.o main.o -o boot.bin
}
以上の操作でbootloaderの処理が書かれたバイナリファイル\emp{boot.bin}ができたわけだが、bootloaderとして認識されるためには510と511番地にマジックナンバーを書かなければならない。これを書くために\emp{sign.pl}が存在する。
\code{
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ perl sign.pl boot.bin
boot block is 136 bytes (max 510)
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ hexdump boot.bin
0000000 fcfa 010f 2e16 0f7c c020 8366 01c8 220f
0000010 eac0 7c34 0008 0000 0000 0000 0000 ffff
0000020 0000 9a00 00cf ffff 0000 9200 00cf 0017
0000030 7c16 0000 b866 0010 d88e c08e e08e e88e
0000040 d08e 00bc 007c e800 0002 0000 feeb 8955
0000050 ebe5 00fe 0014 0000 0000 0000 7a01 0052
0000060 7c01 0108 0c1b 0404 0188 0000 0018 0000
0000070 001c 0000 ffda ffff 0005 0000 4100 080e
0000080 0285 0d42 0005 0000 0000 0000 0000 0000
0000090 0000 0000 0000 0000 0000 0000 0000 0000
*
00001f0 0000 0000 0000 0000 0000 0000 0000 aa55
0000200
}
最後にaa55の文字が見えるので、きちんと書き込まれたことがわかる。


# 調査内容


作成したbootloaderをqemuで実行し、gdbを使ってその動作を見ていく。
\code{
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ qemu-system-i386 boot.bin -nographic -s -S
vagrant@vagrant-ubuntu-trusty-32:~$ gdb
(gdb) target remote :1234
(gdb) set architecture i8086
}
とりあえずbootloaderの処理が始まる0x7c00まで処理を進める。
\code{
(gdb) b *0x7c00
Breakpoint 1 at 0x7c00
(gdb) c
Continuing.
Breakpoint 1, 0x00007c00 in ?? ()
}
次に 16-bit real mode から 32-bit protected mode に切り替わるところまで処理を進める。
\code{
(gdb) disassemble 0x7c00,+0x12
Dump of assembler code from 0x7c00 to 0x7c12:
=> 0x00007c00:	cli
   0x00007c01:	cld
   0x00007c02:	lgdtw  0x7c2e
   0x00007c07:	mov    %cr0,%eax
   0x00007c0a:	or     $0x1,%eax
   0x00007c0e:	mov    %eax,%cr0
   0x00007c11:	ljmp   $0x8,$0x7c34
End of assembler dump.
(gdb) b *0x7c11
Breakpoint 2 at 0x7c11
(gdb) c
Continuing.
Breakpoint 2, 0x00007c11 in ?? ()
(gdb) si
}
切り替わったら次はbootmainを呼び出す前まで処理を進める。
\code{
(gdb) set architecture i386
(gdb) info reg eip
eip            0x7c34	0x7c34
(gdb) disassemble 0x7c34,+0x14
Dump of assembler code from 0x7c34 to 0x7c48:
=> 0x00007c34:	mov    $0x10,%ax
   0x00007c38:	mov    %eax,%ds
   0x00007c3a:	mov    %eax,%es
   0x00007c3c:	mov    %eax,%fs
   0x00007c3e:	mov    %eax,%gs
   0x00007c40:	mov    %eax,%ss
   0x00007c42:	mov    $0x7c00,%esp
   0x00007c47:	call   0x7c4e
End of assembler dump.
}
この0x7c47番地のcall処理が\emp{call bootmain}に当たることになる。実際にcall処理を呼び出すところまで進めて見る。
\code{
(gdb) b *0x7c47
Breakpoint 3 at 0x7c47
(gdb) c
Continuing.
Breakpoint 3, 0x00007c47 in ?? ()
(gdb) si
0x00007c4e in ?? ()
(gdb) info reg eip
eip            0x7c4e	0x7c4e
}
ここからの処理がどのようになっているのかを見て見る。
\code{
(gdb) disassemble 0x7c4e,+0x4
Dump of assembler code from 0x7c4e to 0x7c52:
=> 0x00007c4e:	push   %ebp
   0x00007c4f:	mov    %esp,%ebp
   0x00007c51:	jmp    0x7c51
End of assembler dump.
}
ここからの処理は、C言語の関数の通常処理と無限ループになっていることがわかる。確かにbootmainを呼ぶことができているようだ。
