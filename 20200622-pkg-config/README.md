# pkg-configについてまとめる

pkg-configを使う用事ができたので学んでみる。一通りmanページに書かれていることを試せばそれなりに理解できるはず[1]。

## オプションを片っ端から試す

pkg-configがpcファイルを探す先はデフォルトで

- `/usr/lib/pkgconfig`
- `/usr/local/lib/pkgconfig`

などがあるようす[2]。とりあえず中身を覗いてみると、gio-2.0のpcファイルが色々と書かれていて練習に良さそうだったので、このライブラリで試してみる。

そのライブラリのpcファイルの中身は以下

```
$ tail -n 8 /usr/local/lib/pkgconfig/gio-2.0.pc
Name: GIO
Description: glib I/O library
Version: 2.64.3
Requires: glib-2.0, gobject-2.0
Requires.private: gmodule-no-export-2.0, zlib
Libs: -L${libdir} -lgio-2.0
Libs.private: -Wl,-framework,CoreFoundation -Wl,-framework,Carbon -Wl,-framework,Foundation -Wl,-framework,AppKit -lintl -lresolv
Cflags:-I${includedir}
```

### modversion

```
$ pkg-config --modversion gio-2.0
2.64.3
```

### cflags

```
$ pkg-config --cflags gio-2.0
-I/usr/local/Cellar/libffi/3.3/include -I/usr/local/Cellar/glib/2.64.3/include -I/usr/local/Cellar/glib/2.64.3/include/glib-2.0 -I/usr/local/Cellar/glib/2.64.3/lib/glib-2.0/include -I/usr/local/opt/gettext/include -I/usr/local/Cellar/pcre/8.44/include
```

gio自体が要求しているcflagsは存在せず、依存パッケージglibとgobjectによるものが引き継がれているようす

```
$ pkg-config --cflags glib-2.0
-I/usr/local/Cellar/glib/2.64.3/include/glib-2.0 -I/usr/local/Cellar/glib/2.64.3/lib/glib-2.0/include -I/usr/local/opt/gettext/include -I/usr/local/Cellar/pcre/8.44/include
$ pkg-config --cflags gobject-2.0
-I/usr/local/Cellar/libffi/3.3/include -I/usr/local/Cellar/glib/2.64.3/include -I/usr/local/Cellar/glib/2.64.3/include/glib-2.0 -I/usr/local/Cellar/glib/2.64.3/lib/glib-2.0/include -I/usr/local/opt/gettext/include -I/usr/local/Cellar/pcre/8.44/include
```

### libs

```
$ pkg-config --libs gio-2.0
-L/usr/local/Cellar/glib/2.64.3/lib -L/usr/local/opt/gettext/lib -lgio-2.0 -lgobject-2.0 -lglib-2.0 -lintl
```

この中で、次の二つはgioのpcファイルによるもの

- `-L/usr/local/Cellar/glib/2.64.3/lib`
- `-lgio-2.0`

この二つは依存のglibによって追加されたもの

- `-L/usr/local/opt/gettext/lib`
- `-lglib-2.0`
- `-lintl`

さらにgobjectによって次が追加されている

- `-lgobject-2.0`

もちろん `Requires.private` になっているzlibなどによるフラグは入っていない

```
$ pkg-config --libs gmodule-no-export-2.0
-L/usr/local/Cellar/glib/2.64.3/lib -L/usr/local/opt/gettext/lib -lgmodule-2.0 -lglib-2.0 -lintl
$ pkg-config --libs  zlib
-lz
```

### libs-only-L, libs-only-l

確かに `-L` や `-l` だけ抜き出されている

```
$ pkg-config --libs-only-L gio-2.0
-L/usr/local/Cellar/glib/2.64.3/lib -L/usr/local/opt/gettext/lib
$ pkg-config --libs-only-l gio-2.0
-lgio-2.0 -lgobject-2.0 -lglib-2.0 -lintl
```

### static

staticをつけるとprivateになっていたリンクオプションが全てくっつく

```
$ pkg-config --libs --static gio-2.0
-L/usr/local/Cellar/libffi/3.3/lib -L/usr/local/Cellar/glib/2.64.3/lib -L/usr/local/opt/gettext/lib -L/usr/local/Cellar/pcre/8.44/lib -lgio-2.0 -Wl,-framework,CoreFoundation -Wl,-framework,Carbon -Wl,-framework,Foundation -Wl,-framework,AppKit -lintl -lresolv -lgmodule-2.0 -lintl -lz -lgobject-2.0 -lintl -lffi -lglib-2.0 -lintl -Wl,-framework,CoreFoundation -Wl,-framework,Carbon -Wl,-framework,Foundation -Wl,-framework,AppKit -liconv -lpcre -D_THREAD_SAFE -pthread
```

## pcファイルを作る

[3]に従って作ってみる。

```
$ vim foo.pc
$ cat foo.pc
prefix=/usr/local
exec_prefix=${prefix}
includedir=${prefix}/include
libdir=${exec_prefix}/lib
Name: foo
Description: The foo library
Version: 1.0.0
Cflags: -I${includedir}/foo
Libs: -L${libdir} -lfoo
$ vim bar.pc
$ cat bar.pc
prefix=/usr/local
exec_prefix=${prefix}
includedir=${prefix}/include
libdir=${exec_prefix}/lib
Name: bar
Description: The bar library
Version: 1.0.0
Requires.private: foo
Cflags: -I${includedir}/bar
Libs: -L${libdir} -lbar
```

そして実際に使ってみる。

```
$ export PKG_CONFIG_PATH=$(pwd)
$ pkg-config --modversion bar
1.0.0
$ pkg-config --cflags bar
-I/usr/local/include/bar -I/usr/local/include/foo
$ pkg-config --libs bar
-L/usr/local/lib -lbar
$ pkg-config --libs --static bar
-L/usr/local/lib -lbar -lfoo
```

## 参考

1. [pkg-config(1) - Linux man page](https://linux.die.net/man/1/pkg-config)
1. [PKG_CONFIG_PATH environment variable](https://askubuntu.com/questions/210210/pkg-config-path-environment-variable)
1. [Guide to pkg-config](https://people.freedesktop.org/~dbn/pkg-config-guide.html)
