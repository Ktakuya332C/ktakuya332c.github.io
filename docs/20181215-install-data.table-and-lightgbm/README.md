# data.tableとxgboostをMacに入れる際の問題

[data.table](https://github.com/Rdatatable/data.table)パッケージを[この指示](https://github.com/Rdatatable/data.table/wiki/Installation)に従ってllvmを使ってインストールした。

```
$ xcode-select --install
$ brew install llvm
$ mkdir ~/.R
$ vim ~/.R/Makevars
$ cat ~/.R/Makevars
LLVM_LOC = /usr/local/opt/llvm
CC=$(LLVM_LOC)/bin/clang -fopenmp
CXX=$(LLVM_LOC)/bin/clang++ -fopenmp
CFLAGS=-g -O3 -Wall -pedantic -std=gnu99 -mtune=native -pipe
CXXFLAGS=-g -O3 -Wall -pedantic -std=c++11 -mtune=native -pipe
LDFLAGS=-L/usr/local/opt/gettext/lib -L$(LLVM_LOC)/lib -Wl,-rpath,$(LLVM_LOC)/lib
CPPFLAGS=-I/usr/local/opt/gettext/include -I$(LLVM_LOC)/include
```


その後色々なライブラリを入れて使っていたが、その時は何も問題が起きなかった。

問題が起きたのは、LightGBMを使いたくなったので、[この指示](https://github.com/Microsoft/LightGBM/tree/master/R-package)に従ってインストールしてみた時だ。

```
$ brew install libomp
$ git clone --recursive https://github.com/Microsoft/LightGBM
$ cd LightGBM
$ Rscript build_r.R
```


こうやってインストールしたLightGBMをdata.tableを入れた後にインストールしたライブラリとともに使用したらエラーが出た。

```
OMP: Error #15: Initializing libomp.dylib, but found libomp.dylib already initialized.
OMP: Hint This means that multiple copies of the OpenMP runtime have been linked into the program. That is dangerous, since it can degrade performance or cause incorrect results. The best thing to do is to ensure that only a single OpenMP runtime is linked into the process, e.g. by avoiding static linking of the OpenMP runtime in any library. As an unsafe, unsupported, undocumented workaround you can set the environment variable KMP_DUPLICATE_LIB_OK=TRUE to allow the program to continue to execute, but that may cause crashes or silently produce incorrect results. For more information, please see http://openmp.llvm.org/
Abort trap: 6
```


どうもlibomp.dylibが二つ以上リンクされているということらしい。

このエラーの原因は多分libompとllvmの二つのライブラリでインストールされたlibomp.dylibがどちらもリンクされてしまっていることが問題だろう。確かにlibompでインストールされたもの

```
$ ls /usr/local/lib | grep libomp.dylib
libomp.dylib
```


と、llvmでインストールされたもの

```
$ ls /usr/local/opt/llvm/lib | grep libomp
libomp.dylib
```


の二つが存在している。さらに、data.tableをインストールする時に`-Wl,-rpath,$(LLVM_LOC)/lib`としてlllvm側の`libomp.dylib`にリンクしていることがわかるし、多分`build_r.R`も内部でlibomp側の`libomp.dylib`にリンクしているのだろう。

lightGBMをllvmの持っているopemMPIとともにインストールする方法が乗っていなかったうえに、Makefileをいじらないといけなさそうだったのでそこは回避して、llvmを使わない方向に決めた。とりあえずdata.tableからllvmの依存を抜いてみた

```
$ r
> remove.packages("data.table")
$ rm -rf ~/.R
$ r
> install.packages("data.table")
```


が、まだ先ほどと同じエラーが出る。

data.tableを入れた後に入れたいくつかのライブラリが原因であると思われるので、とりあえずllvmのopemMPIにリンクしているライブラリを全て再インストールすることで解決を図った。とりあえずライブラリがインストールされているパスは

```
> .libPaths()
[1] "/usr/local/lib/R/3.5/site-library"
[2] "/usr/local/Cellar/r/3.5.1/lib/R/library"
```


の二つのようなので、それぞれのディレクトリで全てのライブラリに対してotoolで依存している dynamic library をみていけばllvmにリンクされてしまっているものがわかる。

```
$ cd /usr/local/lib/R/3.5/site-library
$ for d in */; do
  cd $d
  if [[ -d libs ]]; then
    cd libs
    otool -L *.so | grep libomp > /dev/null
    if [[ $? == 0 ]]; then
      pwd
      otool -L *.so
    fi
    cd ..
  fi
  cd ..
done
```


とりあえず適当にスクリプトを走らせてみると、いくつか該当するライブラリが見つかった。依存性で入ってきているものが多いので、あまり記憶にないものが多いが、記憶にあるものは最近入れたものなので妥当だろう。それらの該当するライブラリを再度インストールしてみることで、llvmに依存するライブラリはなくなるはずだ。

以上でllvmへの依存を全て抜いたはずなので、これでlightGBMとそのほかのライブラリを併用しても問題がなくなった。
