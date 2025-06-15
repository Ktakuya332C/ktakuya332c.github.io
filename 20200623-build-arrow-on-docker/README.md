# docker上でapache-arrowのビルドをする

以前は開発環境をvagrantで作っていたが、dockerの方がやはり簡単なのでそちらで行ってみる。

## C++のための開発環境整備

Dockerfileとセットアップスクリプトを用意する

```
$ mkdir arrow-env
$ cd arrow-env
$ vim Dockerfile
$ cat Dockerfile
FROM ubuntu:latest
RUN apt-get update &amp;&amp; \
    apt-get install -y \
      vim less wget curl git \
      build-essential cmake &amp;&amp; \
    apt-get clean
WORKDIR /root
CMD [&quot;bash&quot;]
$ vim setup.sh
$ cat setup.sh
#!/usr/bin/env bash
set -eu
CUR_DIR=$(pwd)
docker build -t arrow-env $CUR_DIR
docker run -it --rm -v $CUR_DIR:/root arrow-env bash
```

あとはセットアップをして開発をする。

```
bash setup.sh
git clone https://github.com/apache/arrow.git
cd arrow/cpp
mkdir release
cd release
cmake ..
make
```

## Pythonのための開発環境整備

Dockerfileを次のように変更する。apt-getで導入できるcmakeはビルドパスなどを引数で指定できないので、新しめのものを導入しておく。

```
$ vim Dockerfile
$ cat Dockerfile
FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y \
      vim less wget curl git \
      build-essential pkg-config autoconf \
      libjemalloc-dev libboost-dev \
      libboost-filesystem-dev \
      libboost-system-dev \
      libboost-regex-dev \
      python3-dev python3-pip \
      flex \
      bison && \
    apt-get clean && \
    wget -q -P /tmp https://github.com/Kitware/CMake/releases/download/v3.17.3/cmake-3.17.3-Linux-x86_64.sh && \
    sh /tmp/cmake-3.17.3-Linux-x86_64.sh --skip-license --prefix=/usr/local
WORKDIR /root
CMD ["bash"]
```

セットアップスクリプトは変更せず

```
$ vim setup.sh
$ cat setup.sh
#!/usr/bin/env bash
set -eu
CUR_DIR=$(pwd)
docker build -t arrow-env $CUR_DIR
docker run -it --rm -v $CUR_DIR:/root arrow-env bash
```

dockerを立ち上げる。

```
bash setup.sh
```

arrowのソースコードを持ってきて

```
git clone https://github.com/apache/arrow.git
```

ビルドの成果物を入れるディレクトリとインストール先のディレクトリを決める。ここではデフォルトの設定どおり`/usr/local`以下にインストールするのではなく、`/root/dist`にインストールすることにする

```
mkdir dist build
export ARROW_HOME=/root/dist
export LD_LIBRARY_PATH=$ARROW_HOME/lib:$LD_LIBRARY_PATH
```

まずはC++のライブラリをビルドする

```
$ cmake -DCMAKE_INSTALL_PREFIX=$ARROW_HOME \
        -DARROW_PYTHON=ON \
        -S arrow/cpp -B build
$ cmake --build build --target all
$ cmake --build build --target install
```

最後にpythonのライブラリをビルドする

```
$ pip3 install --upgrade pip
$ pip3 install \
    -r arrow/python/requirements-build.txt \
    -r arrow/python/requirements-test.txt
$ cd arrow/python
$ python3 setup.py build_ext --inplace
```
