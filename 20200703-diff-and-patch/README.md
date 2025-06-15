# diffとpatch

カーネルのメーリングリストなどを読んでいると頻繁にdiffとpatchが登場するので慣れておく。

## diff

diff自体はよく使うが、メーリングリストではそのパッチでの差分を出力形式の一つであるunified形式で送っている。diffにuオプションを追加すれば出力できるようで、例えば

```
$ for i in {1..12}; do echo $i >> test1.txt; done;
$ cp test1.txt test2.txt
$ vim test2.txt
$ diff -u test1.txt test2.txt
--- test1.txt 2020-07-03 22:31:13.000000000 +0900
+++ test2.txt 2020-07-03 22:24:45.000000000 +0900
@@ -3,7 +3,8 @@
 3
 4
 5
-6
+6a
+6b
 7
 8
 9
```

と出力される。

まず最初の二行

```
--- test1.txt 2020-07-03 22:31:13.000000000 +0900
+++ test2.txt 2020-07-03 22:24:45.000000000 +0900
```

はどのファイルの差分をいつ取ったかを表示してくれている。

その後の

```
@@ -3,7 +3,8 @@
```

は、調べると

```
@@ -変更前のファイルにおける開始行,行数 +変更後のファイルにおける開始行,行数@@
```

という形になっているらしく、変更前のファイルのこの領域が変更後のファイルのこの領域に該当するようになりますよ、ということを意味している様子。今回の場合で言えば、変更前のファイルの3行目からの7行分が、変更後のファイルの3行目から8行分に当たりますよと言っている。

最後は見た目明らかで

```
...
-6
+6a
+6b
...
```

消された行と追加された行を表している

## patch

ついでなのでこのdiffに基づいたpatchも試してみた。patchをdiffコマンドで作ってみて

```
diff -u test1.txt test2.txt > diff.patch
```

そのpatchを実際に当ててみると確かに変更される。

```
$ patch -u test1.txt < diff.patch
$ head -n 7 test1.txt | tail -n 2
6a
6b
```

ちなみにdiffの開始行数などを適当にいじってやると

```
$ vim diff.patch
$ head -n 3 diff.patch | tail -n 1
@@ -3,7 +3,10 @@
```

patchを当てたときに失敗する

```
$ cp /dev/null test1.txt
$ for i in {1..12}; do echo $i >> test1.txt; done;
$ patch test1.txt < diff.patch
patching file test1.txt
patch: **** malformed patch at line 12:
$ echo $?
2
```

## 参考

- [Linuxエンジニアらしいパッチのつくりかた](https://qiita.com/astro_super_nova/items/e30dcaf4d106deebc63c)
- [diffによるunified形式の意味について](https://den8.hatenadiary.org/entry/20100622/1277226958)
- [diff & patch コマンドでのパッチを適用する方法](http://mrgoofy.hatenablog.com/entry/20101019/1287500809)
