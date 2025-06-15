# pyarrowのデバッグの仕方

今回はpyarrowの開発方法をメモしていく。特に、最低限ソースコードを読み始められるようになるための下準備として

1. ubuntu18環境下でのpython2でのpyarrowライブラリのビルド方法
1. gdbを使用したpyarrowのデバッグ方法

を記載していく。ここで説明する開発方法ではpythonのバージョンはpython2の場合のみを紹介する。python3の場合にも同じような方法で環境を整えていくことが可能なはずだが、まだ試していないので一旦保留としておく。

## pyarrowライブラリのビルド方法

arrowの開発を行うにあたって手元の環境をそのまま使用すると他にインストールしている様々なライブラリの依存関係を破壊してしまう可能性があるので、手元の環境とは別に仮想環境を用意してそちらで開発することにする。今回はvagrantの`bento/ubuntu-18.04`を使用することにする。vagrantはすでにインストールされているものとして、

```
vagrant init bento/ubuntu-18.04
vagrant up
vagrant ssh
vagrant@vagrant: ~$
```

としてubuntu18の環境を作成する。

次にパッケージの状態を全て最新の状態に更新しておく。

```
sudo apt update
sudo apt upgrade -y
```

この作業、特にupgradeを行わないとこの後のビルドがどこかしらで落ちることになる。upgradeの途中でいくつかncurseの画面が出現して入力を求められることがあるかもしれないが、それぞれ適切に答えておく。

pyarrowのライブラリをビルドするためにはまずarrowのC++ライブラリをPythonのサポートをつけた上でビルドすることが必要である。まずC++ライブラリをビルドするために必要な依存ライブラリを全てインストールしてしまう。

```
sudo apt install -y \
    autoconf cmake \
    python-dev python-pip \
    libjemalloc-dev \
    libboost-dev \
    libboost-filesystem-dev \
    libboost-system-dev \
    libboost-regex-dev \
    flex bison
```

本体のコードを取ってきて

```
git clone https://github.com/apache/arrow.git
```

ついでに必要なpythonのライブラリも導入してしまう。

```
pip install -r arrow/python/requirements-build.txt
```

そしてarrowのC++ライブラリをデバッグフラグ付き(`DCMAKE_BUILD_TYPE=debug`)でビルドする。

```
pushd arrow/cpp
  mkdir -p dist build
  export ARROW_HOME=$(pwd)/dist
  export LD_LIBRARY_PATH=$(pwd)/dist/lib
  pushd build
    cmake \
        -DCMAKE_INSTALL_PREFIX=$ARROW_HOME \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DARROW_PYTHON=ON \
        -DCMAKE_BUILD_TYPE=debug \
        ..
    make -j4
    make install
  popd
popd
```

ここで`ARROW_HOME`はC++ライブラリがインストールされる場所を指し、`make install`をするとその場所にコンパイルされた後のライブラリがインストールされる。

最後にpyarrowをデバッグフラグつき(`--build-type=debug`)でビルドする

```
cd arrow/python
python setup.py build_ext --build-type=debug --inplace
```

これでpyarrowがビルドされ、次のようにビルドしたライブラリをimportして使用することができる。

```
python
>>> import pyarrow
>>> pyarrow.array([1,2,3])
<pyarrow.lib.Int64Array object at 0x7f0756443b90>
[
  1,
  2,
  3
]
```

## gdbを利用したpyarrowのデバッグ方法

pyarrowはarrowのC++ライブラリをpythonから使えるようにするためにcythonを利用している。pyarrowはそのほとんどがcythonで書かれているため、その多くがC++に一度コンパイルされて使用されている。よってpyarrowをデバッグする際にはpythonのデバッグ用ライブラリであるpdbなどを使用してpythonのレベルでデバッグするよりも、gdbなどを利用してC++のレベルでデバッグを行う方が効率が良い。よってここではgdbを利用したデバッグ方法を記載する

gdbを利用する際には、まずライブラリをインストールして

```
sudo apt install gdb
```

デバッグしたい、pyarrowを使ったpythonファイルを用意する

```
vim sample.py
```

そしてgdb上でそのpythonファイルを実行する

```
gdb --args python sample.py
(gdb)
```

ついでに見た目が綺麗になるように少しgdbの設定を加えておく

```
(gdb) set print pretty on
```

これで`sample.py`がpythonで実行される様子をC++のレベルでデバッグできるようになった。

あとはcythonがコンパイルしたC++レベルのコードか、pyarrowが呼び出していたarrowのC++ライブラリのコードの一部かを指定して通常のgdbと同じようにデバッグしていけばいい。たとえば次のようなpythonファイルを用意していたら

```
import pyarrow
pyarrow.array([1, 2, 3])
```

`array`関数で呼び出されるarrowのC++ライブラリに含まれる`ConvertPySequence`関数にブレイクポイントを仕掛けて

```
(gdb) br ConvertPySequence
Function "ConvertPySequence" not defined.
Make breakpoint pending on future shared library load? (y or [n]) y
Breakpoint 1 (ConvertPySequence) pending.
```

実行するとその関数にたどり着いた時点で実行が中断される。

```
(gdb) run
Starting program: /usr/bin/python sample.py
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x00007ffff1a7c0e0 in arrow::py::ConvertPySequence(_object*, _object*, arrow::py::PyConversionOptions const&, std::shared_ptr<arrow::ChunkedArray>*)@plt () from /home/vagrant/arrow/python/pyarrow/lib.so
```

いくつか処理を進めてみて

```
(gdb) n
...
(gdb) n
...
(gdb) n
956   PyAcquireGIL lock;
```

その周りの処理を一旦俯瞰してみて

```
(gdb) li  956
952
953 Status ConvertPySequence(PyObject* sequence_source, PyObject* mask,
954                          const PyConversionOptions& options,
955                          std::shared_ptr<ChunkedArray>* out)
956   PyAcquireGIL lock;
957
958   PyDateTime_IMPORT;
959
960   PyObject* seq;
```

例えば`sequence_source`変数に何が入っているのかをみたくなったら`print`関数で見てみる

```
(gdb) print sequence_source
$1 = (PyObject *) 0x7fffee109b48
(gdb) print *sequence_source
$2 = {
  ob_refcnt = 1,
  ob_type = 0x555555a71680 <PyList_Type>
}
(gdb) print *(PyListObject*)sequence_source
$3 = {
  ob_refcnt = 1,
  ob_type = 0x555555a71680 <PyList_Type>,
  ob_size = 3,
  ob_item = 0x555556095b50,
  allocated = 3
}
```

`sequence_source`はリストのようなので、その中に何が入っているかを調べたい場合には少しずつ中身を調べていけばいい。

```
(gdb) print (*(PyListObject*)sequence_source).ob_item[0]
$4 = (PyObject *) 0x555555b08598
(gdb) print *((*(PyListObject*)sequence_source).ob_item[0])
$5 = {
  ob_refcnt = 3051,
  ob_type = 0x555555a6e940 <PyInt_Type>
}
(gdb) print *(PyIntObject*)((*(PyListObject*)sequence_source).ob_item[0])
$8 = {
  ob_refcnt = 3051,
  ob_type = 0x555555a6e940 <PyInt_Type>,
  ob_ival = 1
}
```

`sequence_source`は3つの要素が入っているリストで、一つ目の要素は1であることがわかった。

## その他

一度仮想環境から出て、再度入り直した際には環境変数を少し設定し直しておかないとpyarrowをインポートすることはできない。とりあえず

```
export ARROW_HOME=$(pwd)/arrow/cpp/dist
export LD_LIBRARY_PATH=$ARROW_HOME/lib
```

としておけば問題はない。

またMacOS上でコンパイルした時は、どうもpythonのライブラリからcppのライブラリへのリンクがうまく通らない様子。なのでそのような時はリンクしている先のcppライブラリのパスを確認して

```
$ otool -L pyarrow/lib.cpython-37m-darwin.so
pyarrow/lib.cpython-37m-darwin.so:
 @rpath/libarrow.100.dylib (compatibility version 100.0.0, current version 100.0.0)
 @rpath/libarrow_python.100.dylib (compatibility version 100.0.0, current version 100.0.0)
 /usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 400.9.4)
 /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1252.200.5)
```

リンクされていなさそうなライブラリを絶対パスに書き換えてやると良いかもしれない。

```
install_name_tool -change @rpath/libarrow.100.dylib $LD_LIBRARY_PATH/libarrow.100.dylib pyarrow/lib.cpython-37m-darwin.so
install_name_tool -change @rpath/libarrow_python.100.dylib $LD_LIBRARY_PATH/libarrow_python.100.dylib pyarrow/lib.cpython-37m-darwin.so
```

## 参考文献

1. [pyarrowの公式開発者用ドキュメント](https://github.com/apache/arrow/blob/master/docs/source/developers/python.rst)
1. [Fun with rpath, otool, install_name_tool](https://medium.com/%40donblas/fun-with-rpath-otool-and-install-name-tool-e3e41ae86172)
