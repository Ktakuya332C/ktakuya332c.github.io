# PIOを使ってハードディスクを読む

PIO(Programmed I/O)を使ってハードディスクを読むようなbootloaderを書いたのでメモ。

## 調査用コード

ハードディスクの二つ目のセクターに存在する適当なバイト列をメモリに読み込むことができることを確認するために、次のようなスクリプトを書いた。

```
.set PROT_MODE_CSEG, 0x8
.set PROT_MODE_DSEG, 0x10
.set CR0_PE_ON, 0x1

.globl start
start:
  .code16

  cli # Disable interrupts
  cld # String operations increment the counter

  # Switch from 16-bit real mode to 32-bit protected mode
  lgdt gdtdesc
  movl %cr0, %eax
  orl $CR0_PE_ON, %eax
  movl %eax, %cr0
  ljmp $PROT_MODE_CSEG, $protcseg

gdt:
	# Null segment
	.word 0x0, 0x0
	.byte 0x0, 0x0, 0x0, 0x0
	# Code segment
	.word 0xffff
	.word 0x0
	.byte 0x0
	.byte 0b10011010
	.byte 0b11001111
	.byte 0x0
	# Data segment
	.word 0xffff
	.word 0x0
	.byte 0x0
	.byte 0b10010010
	.byte 0b11001111
	.byte 0x0
gdtdesc:
	.word 0x17
	.long gdt

	.code32
protcseg:
	# Setup the 32-bit protected mode data segment registers
	movw $PROT_MODE_DSEG, %ax
	movw %ax, %ds
	movw %ax, %es
	movw %ax, %fs
	movw %ax, %gs
	movw %ax, %ss

	# Wait for the disk to be ready
	call waitdisk

	# Prepare to read the disk
	movw $0x1f2, %dx
	movb $0x1, %al
	outb %al, %dx
	movw $0x1f3, %dx
	movb $0x1, %al
	outb %al, %dx
	movw $0x1f4, %dx
	movb $0x0, %al
	outb %al, %dx
	movw $0x1f5, %dx
	movb $0x0, %al
	outb %al, %dx
	movw $0x1f6, %dx
	movb $0xe0, %al
	outb %al, %dx
	movw $0x1f7, %dx
	movb $0x20, %al
	outb %al, %dx

	# Wait for the disk to be ready
	call waitdisk

	# Read the disk
	movw $0x1f0, %dx
	movl $0x100000, %edi
	mov $0x1, %cx
	repne insl

spin:
  jmp spin

waitdisk:
	movw $0x1f7, %dx
waitdisk_loop:
	inb %dx, %al
	andb $0xc0, %al
	cmpb $0x40, %al
	jnz waitdisk_loop
	ret

	# Bootloader Magic Number
  . = start + 510
  .byte 0x55
  .byte 0xaa

  # 5 bytes are placed at the head of second sector
  # to check that `insl` reads exactly 4 bytes from the hard disk
  .byte 0x01
  .byte 0x02
  .byte 0x03
  .byte 0x04
  .byte 0x05
```


全体的には次のような処理を行っている。

1. 16-bit real mode で起動したbootloaderの動作方法を 32-bit protected mode での動作に変更する
1. PIOを用いて、ハードディスクが読み込み可能になるまで待つ
1. PIOを用いて、ハードディスクにどの部分の情報をどのくらい読み出すかを設定する
1. PIOを用いて、実際にハードディスクから情報を読み出す


PIOを使用する際には、まずそのPIOがその時点でコマンドを受け付けているかどうかを確認しなければならない。PIOの状態は0x1f7番ポートの状態を読み取れば良く[2]、0x1f7番ポートの情報を読むためにはDXレジスタにそのポート番号0x1f7を入力してからinb命令を実行すれば良い[4]。読み取り結果はALレジスタに保存される[4]。

```
movw $0x1f7, %dx
inb %dx, %al
```


読み取り結果の中でコマンドを受け付けているかどうかがわかるのは上位二つのビット、最上位のBSYビット(何かしらの作業中なら0)と次点のRDYビット(コマンドを受け付ける準備ができているなら0)である[2]。それら上位にビットを次のように確認する。

```
andb $0xc0, %al # 0xc0 = 0b11000000
cmpb $0x40, %al # 0x40 = 0b1000000
```


PIOがコマンドを受け付けられる状態になったら、次はハードディスクのどの部分の情報をどれくらい読み出す可能性があるかを伝える。今回はハードドライブから一つのセクターを

```
movw $0x1f2, %dx
movb $0x1, %al
outb %al, %dx
```


28-bit [LBA(Logical Block Address)](https://en.wikipedia.org/wiki/Logical_block_addressing)で0始まりで1つめのセクター(普通に数えれば2つめ)を起点として、0番目のハードドライブからLBA方式で読み出す予定ですと

```
movw $0x1f3, %dx
movb $0x1, %al # 28-bit LBA の一番下の8bit
outb %al, %dx
movw $0x1f4, %dx
movb $0x0, %al # 28-bit LBA の真ん中下の8bit
outb %al, %dx
movw $0x1f5, %dx
movb $0x0, %al # 28-bit LBA の真ん中上の8bit
outb %al, %dx
movw $0x1f6, %dx
movb $0xe0, %al # 0xe0 = 0b11100000, 下4bitはLBAに使用される
outb %al, %dx
```


伝えている[2]。

```
movw $0x1f7, %dx
movb $0x20, %al
outb %al, %dx
```


どのような情報を読み取るか伝えてハードディスクが読み取っても良いと言ったら実際に読み取ることになる。読み取り用のポートを設定し[2]

```
movw $0x1f0, %dx
```


読み取り先のメモリのアドレスをEDXに指定し[4]

```
movl $0x100000, %edi
```


1度だけinslコマンドを使って4byteを読み込む(inslのlによってlong=4byteが読まれることが指定される)。

```
mov $0x1, %cx # repneに渡す引数
repne insl
```


## 調査内容

[Macでbootloader周辺をデバッグする方法](../build/debug-bootloader-on-mac.html)の通りに環境を用意し、上記のスクリプトをコンパイルした上でデバッグモードで実行する。

```
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ as boot.S -o boot.o
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ ld -Ttext 07c00 --oformat=binary --entry start boot.o  -o boot.bin
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ qemu-system-i386 boot.bin -nographic -s -S
```


別のTerminalでgdbを使って最後まで実行してみる。

```
vagrant@vagrant-ubuntu-trusty-32:~$ gdb
(gdb) target remote :1234
(gdb) c
Continuing.
```


適当なところでCtrl-Cなどを押して処理を止める。多くの場合は最後の処理まで言っているはずなので、実際にハードディスクを読み取った先のアドレス0x10000には読み取った値が記録されているはずである。

```
(gdb) x/5bx 0x100000
0x100000:	0x01	0x02	0x03	0x04	0x00
```


実際に読み取りを行なった4byteは確かに読み取れていることがわかる。今回はinsl命令を一度しか行なっていないため4byteしか読み込まれず、5byte目の0x05は読み取られていないことがわかる。

## 参考文献

1. assemblyのinやoutなどの命令がどのような意味なのかという質問に対して、IOポートとは何かというところから明確に回答している[Stackoverflow](https://stackoverflow.com/questions/3215878/what-are-in-out-instructions-in-x86-used-for)
1. IOポートを使ってハードディスクを読む際に具体的にどのようにすれば良いのかを説明してくれている唯一と言ってもよい[資料](https://wiki.osdev.org/ATA_PIO_Mode)
1. MITで開かれたOSについての授業の[資料](https://pdos.csail.mit.edu/6.828/2018/)。このサイトで公開されている授業用に作成されたカーネルJOSのbootloaderの処理を参考にしている。
1. Intel 386 の[仕様書](https://css.csail.mit.edu/6.858/2014/readings/i386.pdf)
