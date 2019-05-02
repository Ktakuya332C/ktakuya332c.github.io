またもqemu上で動くbootloaderのA20ラインを調べる
2019-03-16


以前qemu上でbootloaderを動かした時に最初からA20ラインがonになっていることを見つけた。その時使用したスクリプトは Intel Syntax で書かれていたのだが、今回同じものを AT&T syntax で書いて見たのでメモ。


# 調査用コード


今回調査に使用したbootloaderのコードは以下のようになった。0x500番地に何かしらの情報を書き込んだ上で、0x100500番地にさらに別のものを書き込んで、最初に0x500番地に書き込んだ情報が上書きされるかどうかを見る。A20ラインがoffになっていれば上書きされ、A20ラインがonになっていれば上書きされないはずである。
\code{
.globl start
start:
  .code16
  
  # Set %es:%di = 0x0 * 0x10 + 0x500 = 0x500
  movw $0x0, %ax
  movw %ax, %es
  movw $0x500, %di

  # Set %ds:%si = 0xffff * 0x10 + 0x510 = 0x100500
  # If A20 is not turned on, the address is equivalent to 0x500
  movw $0xffff, %ax
  movw %ax, %ds
  movw $0x510, %si

  # Write 0x0 to 0x500, and write 0xff to 0x100500
  movb $0x00, %es:(%di)
  movb $0xff, %ds:(%si)

spin:
  jmp spin

  . = start + 510
  .byte 0x55
  .byte 0xaa
}


# 調査内容


\a{Macでbootloader周辺をデバッグする方法}{\rel{debug-bootloader-on-mac}}の通りに環境構築を行った後に、次のように先の調査コードをコンパイルして行く。
\code{
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ vim boot.S # 上記の調査用コードを書く
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ as boot.S -o boot.o
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ ld -Ttext 0x7c00 --oformat=binary --entry start boot.o -o boot.bin
}
これでboot.binと名付けられたbootloaderが作成できるはず。そして今コンパイルしたbootloaderをqemuを使ってデバッグモードで起動して、gdbでデバッグして行く。
\code{
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ qemu-system-i386 boot.bin -nographic -s -S
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ gdb
(gdb) target remote :1234
(gdb) set architecture i8086
}


とりあえずbootloaderが始まる0x7c00番地まで処理を進めておく
\code{
(gdb) b *0x7c00
Breakpoint 1 at 0x7c00
(gdb) c
Continuing.
Breakpoint 1, 0x00007c00 in ?? ()
}
bootloaderが始まったら調査のための準備をし始めるので、そのような調査の準備が終わったところまで処理を進める。
\code{
(gdb) disassemble 0x7c00,+0x12
Dump of assembler code from 0x7c00 to 0x7c12:
=> 0x00007c00:	mov    $0x0,%ax
   0x00007c03:	mov    %ax,%es
   0x00007c05:	mov    $0x500,%di
   0x00007c08:	mov    $0xffff,%ax
   0x00007c0b:	mov    %ax,%ds
   0x00007c0d:	mov    $0x510,%si
   0x00007c10:	movb   $0x0,%es:(%di)
(gdb) b *0x7c10
Breakpoint 2 at 0x7c10
(gdb) c
Continuing.
Breakpoint 2, 0x00007c10 in ?? ()
}


ここからが実際の調査となる。まずはES:DI番地(0x500番地)に0x00をいれておく。
\code{
(gdb) disassemble 0x7c10,+0x1
Dump of assembler code from 0x7c10 to 0x7c11:
=> 0x00007c10:	movb   $0x0,%es:(%di)
End of assembler dump.
(gdb) si
(gdb) x/1bx 0x500
0x500:	0x00
}
次に、DS:SI番地(0x100500番地)に0xffを入れる。
\code{
(gdb) info reg eip
eip            0x7c14	0x7c14
(gdb) disassemble 0x7c14,+0x1
Dump of assembler code from 0x7c14 to 0x7c15:
=> 0x00007c14:	movb   $0xff,(%si)
End of assembler dump.
(gdb) si
0x00007c17 in ?? ()
(gdb) x/1bx 0x100500
0x100500:	0xff
}
そしてこの操作がES:DI番地(0x500番地)の値を上書きしたかどうかを見る。
\code{
(gdb) x/1bx 0x500
0x500:	0x00
}
上書きしていないようなので、すでにA20ラインはonになっていると思って良い。
