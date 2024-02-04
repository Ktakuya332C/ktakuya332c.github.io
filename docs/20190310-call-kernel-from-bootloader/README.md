# bootloaderからcのkernel関数を呼び出す

[os-tutorial](https://github.com/cfenollosa/os-tutorial)を元にbootloaderを作って見ている。この記事では以下の処理を行うことのできる簡単なbootloaderを紹介する。

1. diskからkernelをメモリーにロードして、
1. 16bit real mode から 32bit protected mode にスイッチ
1. C言語で書かれたカーネルに書かれた処理を実行する


これはos-tutorialにおける13-kernel-barebonesまでと同じ機能を持っていることになる。

## 実装本体

実装は[このGist](https://gist.github.com/Ktakuya332C/413a3b877b86fd1d39010738f6d06f6f)に記録してある。

## 実行方法

開発環境は[この記事](../build/debug-bootloader-on-mac.html)にしたがって整備しておく。

次に上記の実装をコピペしてVagrantによる仮想環境上に置いておく。

```
vagrant@vagrant-ubuntu-trusty-32:~$ ls
boot.asm  entry.asm  kernel.c  Makefile
```


開発環境が全て整っていれば次のコマンドで実行イメージ(image.bin)を作成できるはずである。

```
$ make
nasm -f bin -o boot.bin boot.asm
nasm -f elf -o entry.o entry.asm
gcc -ffreestanding -o kernel.o -c kernel.c
ld -o kernel.bin -Ttext 0x1000 entry.o kernel.o --oformat binary
ld: warning: cannot find entry symbol _start; defaulting to 0000000000001000
cat boot.bin kernel.bin > image.bin
```


リンカーの警告が一つ出ているがこれは今の所無視して良い。

実行は次のようにqemuを使って実行する

```
vagrant@vagrant-ubuntu-trusty-32:~$ qemu-system-i386 -nographic -curses image.bin
```


実行すれば画面がTUIに切り替わり、次のような文字列が出力されるはずである。

```
Aanded in 32-bit Protected Mode_223240-lgw01-56)
iPXE (http://ipxe.org) 00:03.0 C900 PCI2.10 PnP PMM+07FC10F0+07F210F0 C900
Booting from Hard Disk...
Started in 16-bit Real Mode
Loading kernel into memory
```


この画面は今回実行したbootloaderがいくつかの出力を画面に行なった結果である。

1. bootloaderが処理を始めたときに BIOS interrupt call を使って'Started in 16-bit Real Mode'と出力する
1. bootloadreがkernelをdiskからロードし始めたときに BIOS interrupt call を使って'Loading kernel into memory'と出力する
1. bootloadeが 16bit real mode での動作から　32bit protected mode への動作に移った際に、VGAメモリに直接書き込むことで'Landed in 32-bit Protected Mode'と出力する。Offsetを計算する処理を入れていないため、TUIの一番上に出力されてしまう。
1. bootloaderがC言語で書かれたkernelを呼び出した際に、VGAメモリに直接'A'と書き込むことで左上の文字がAに書き換わる。


## コメント

基本的には[os-tutorial](https://github.com/cfenollosa/os-tutorial)の13-kernel-barebonesまでを読めば理解できるはずだが、比較的複雑なところだけコメントしておく。

- `load_disk`関数で使用されている BIOS interrupt call 0x13 はdisk処理を行うinterruptで、その使用方法は例えば[この資料](http://stanislavs.org/helppc/int_13-2.html)などに記載されている。
- `kernel.c`の`func_dummy`関数は、`entry.asm`の役割を際立たせるために置いてある関数である。もしmain関数が必ずファイルの一番上に書かれていることが約束されるのならば`boot.asm` に書かれた処理が終わった後に直接`kernel.c`の一番最初のアドレスに飛んでしまっても問題はない。しかしそれでは`kernel.c`内部での関数の順番が重要になってきてしまうために`entry.asm`という単純にmain関数を呼ぶためだけのものを作成している。
- linkerは引数にとるオブジェクトファイルの順番を保つため、ldコマンドに渡すオブジェクトファイルの順番は今回の通りにしなければならない。
- 当然だがimage.binを作成するときにcatをするときも最初の512bytesにbootloaderのコードが入るように順番に気をつけなければならない。
