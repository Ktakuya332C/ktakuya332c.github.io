pyarrowのデバッグの仕方
2019-06-16


今回はpyarrowの開発方法をメモしていく。特に、最低限ソースコードを読み始められるようになるための下準備として
\ol
{ubuntu18環境下でのpython2でのpyarrowライブラリのビルド方法}
{gdbを使用したpyarrowのデバッグ方法}
を記載していく。ここで説明する開発方法ではpythonのバージョンはpython2の場合のみを紹介する。python3の場合にも同じような方法で環境を整えていくことが可能なはずだが、まだ試していないので一旦保留としておく。


# pyarrowライブラリのビルド方法


arrowの開発を行うにあたって手元の環境をそのまま使用すると他にインストールしている様々なライブラリの依存関係を破壊してしまう可能性があるので、手元の環境とは別に仮想環境を用意してそちらで開発することにする。今回はvagrantの\emp{bento/ubuntu-18.04}を使用することにする。vagrantはすでにインストールされているものとして、
\code{
vagrant init bento/ubuntu-18.04
vagrant up
vagrant ssh
vagrant@vagrant: ~$
}
としてubuntu18の環境を作成する。


次にパッケージの状態を全て最新の状態に更新しておく。
\code{
sudo apt update
sudo apt upgrade -y
}
この作業、特にupgradeを行わないとこの後のビルドがどこかしらで落ちることになる。upgradeの途中でいくつかncurseの画面が出現して入力を求められることがあるかもしれないが、それぞれ適切に答えておく。


pyarrowのライブラリをビルドするためにはまずarrowのC++ライブラリをPythonのサポートをつけた上でビルドすることが必要である。まずC++ライブラリをビルドするために必要な依存ライブラリを全てインストールしてしまう。
\code{
sudo apt install -y \
    autoconf cmake \
    python-dev python-pip \
    libjemalloc-dev \
    libboost-dev \
    libboost-filesystem-dev \
    libboost-system-dev \
    libboost-regex-dev \
    flex bison
}
ついでに必要なpythonのライブラリも導入してしまう。
\code{
pip install -r arrow/python/requirements-build.txt
}
そしてarrowのC++ライブラリをデバッグフラグ付き(\emp{DCMAKE_BUILD_TYPE=debug})でビルドする。
\code{
pushd arrow/cpp
  mkdir dist build
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
}
ここで\emp{ARROW_HOME}はC++ライブラリがインストールされる場所を指し、\emp{make install}をするとその場所にコンパイルされた後のライブラリがインストールされる。


最後にpyarrowをデバッグフラグつき(\emp{--build-type=debug})でビルドする
\code{
cd arrow/python
python setup.py build_ext --build-type=debug --inplace
}
これでpyarrowがビルドされ、次のようにビルドしたライブラリをimportして使用することができる。
\code{
python
>>> import pyarrow
>>> pyarrow.array([1,2,3])
<pyarrow.lib.Int64Array object at 0x7f0756443b90>
[
  1,
  2,
  3
]
}


# gdbを利用したpyarrowのデバッグ方法


pyarrowはarrowのC++ライブラリをpythonから使えるようにするためにcythonを利用している。pyarrowはそのほとんどがcythonで書かれているため、その多くがC++に一度コンパイルされて使用されている。よってpyarrowをデバッグする際にはpythonのデバッグ用ライブラリであるpdbなどを使用してpythonのレベルでデバッグするよりも、gdbなどを利用してC++のレベルでデバッグを行う方が効率が良い。よってここではgdbを利用したデバッグ方法を記載する


gdbを利用する際には、まずライブラリをインストールして
\code{
sudo apt install gdb
}
デバッグしたい、pyarrowを使ったpythonファイルを用意する
\code{
vim sample.py
}
そしてgdb上でそのpythonファイルを実行する
\code{
gdb --args python sample.py
(gdb)
}
ついでに見た目が綺麗になるように少しgdbの設定を加えておく
\code{
(gdb) set print pretty on
}
これで\emp{sample.py}がpythonで実行される様子をC++のレベルでデバッグできるようになった。


あとはcythonがコンパイルしたC++レベルのコードか、pyarrowが呼び出していたarrowのC++ライブラリのコードの一部かを指定して通常のgdbと同じようにデバッグしていけばいい。たとえば次のようなpythonファイルを用意していたら
\code{
import pyarrow
pyarrow.array([1, 2, 3])
}
\emp{array}関数で呼び出されるarrowのC++ライブラリに含まれる\emp{ConvertPySequence}関数にブレイクポイントを仕掛けて
\code{
(gdb) br ConvertPySequence
Function "ConvertPySequence" not defined.
Make breakpoint pending on future shared library load? (y or [n]) y
Breakpoint 1 (ConvertPySequence) pending.
}
実行するとその関数にたどり着いた時点で実行が中断される。
\code{
(gdb) run
Starting program: /usr/bin/python sample.py
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x00007ffff1a7c0e0 in arrow::py::ConvertPySequence(_object*, _object*, arrow::py::PyConversionOptions const&, std::shared_ptr<arrow::ChunkedArray>*)@plt () from /home/vagrant/arrow/python/pyarrow/lib.so
}
いくつか処理を進めてみて
\code{
(gdb) n
...
(gdb) n
...
(gdb) n
956	  PyAcquireGIL lock;
}
その周りの処理を一旦俯瞰してみて
\code{
(gdb) li  956
952
953	Status ConvertPySequence(PyObject* sequence_source, PyObject* mask,
954	                         const PyConversionOptions& options,
955	                         std::shared_ptr<ChunkedArray>* out)
956	  PyAcquireGIL lock;
957
958	  PyDateTime_IMPORT;
959
960	  PyObject* seq;
}
例えば\emp{sequence_source}変数に何が入っているのかをみたくなったら\emp{print}関数で見てみる
\code{
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
}
\emp{sequence_source}はリストのようなので、その中に何が入っているかを調べたい場合には少しずつ中身を調べていけばいい。
\code{
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
}
\emp{sequence_source}は3つの要素が入っているリストで、一つ目の要素は1であることがわかった。


# 参考文献


\ol
{\a{pyarrowの公式開発者用ドキュメント}{https://github.com/apache/arrow/blob/master/docs/source/developers/python.rst}}
