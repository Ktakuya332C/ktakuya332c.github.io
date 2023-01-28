32bit protected mode に移行
2019-03-10

@p{@a{os-tutorial}{https://github.com/cfenollosa/os-tutorial}に基づいてbootloaderを作成して見ているのだが、やっと 16bit real mode から 32bit protected mode への移行ができたのでメモ。基本的に@a{32-bit-enter}{https://github.com/cfenollosa/os-tutorial/tree/master/10-32bit-enter}を元に作っているが、元々は複数のファイルに分かれているのに対して、今回は一つのファイルにまとめてしまっている。}

@section{コード本体}

@p{@a{Gistに貼った}{https://gist.github.com/Ktakuya332C/d9485e8c661290bf0765beaec1cba4bf}ので詳細はそちらを参考にしてほしい。}

@section{実行方法}

@p{まずは@a{以前の記事}{@rel{/build/debug-bootloader-on-mac.html}}で書いたような開発環境を用意する。もちろんこれ以外の環境でも動くかもしれないが、ハードウェアに近いコードなので一度仮想環境を作成した上で起動したほうが確実なように思う。}

@p{次に、コードを@incode{boot.asm}として仮想環境の適当な場所に保存し、nasmでコンパイル、qemuで実行する。}

@blcode{
$ hostname
vagrant-ubuntu-trusty-32
$ ls
boot.asm
$ nasm -f bin -o boot boot.asm
$ qemu-system-i386 boot -curses -nographic
}

@p{するとTerminalの画面が別の画面に切り替わり、}

@blcode{
Started in 32-bit protected mode223240-lgw01-56)
iPXE (http://ipxe.org) 00:03.0 C900 PCI2.10 PnP PMM+07FC10F0+07F210F0 C900
Booting from Hard Disk...
Started in 16-bit read mode
}

@p{のような文字列が出力されるはずである。一番下の'Started in 16-bit real mode'という文章が、最初に 16bit real mode で起動した際に bios interrupt call を使用して出力された文章で、一番上の行の'Started in 32-bit protected mode'という文章が 32bit protected mode に変わってから出力された文章である。}

@section{注意}

@p{gdbでデバッグをするときに16bitのときには}

@blcode{
(gdb) set architecture i8086
}

@p{としていたと思うが、32bitのコードをdisassembleする場合には}

@blcode{
(gdb) set architecture i386
}

@p{として、32bitで動いていることを示さないと正しいdisassemble結果が返ってこなくなる。}
