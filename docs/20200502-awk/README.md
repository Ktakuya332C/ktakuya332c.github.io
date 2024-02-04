# Awkのサンプルスクリプト

ackernewsを漁っていたらこんな記事を見つけた
- [Awk in 20 minutes](https://ferd.ca/awk-in-20-minutes.html)

この記事はAwkの使い方をとても明確に説明してくれていてとても助かる。ざっと読んでAwkの文法が大体理解できた気がするので、説明してあった内容について一つ一つ試して行こうかと思う。

## Code Structure

まずは基本的なAwkスクリプトの構造から。スクリプトは入力された内容を一行ずつ処理してくらしい。
```
$ vim input.txt
$ cat input.txt
This is a pen
Those are pens
$ vim script.awk
$ cat script.awk
{ print $0; }
{ print &quot;interlude&quot;; }
$ awk -f script.awk input.txt
This is a pen
interlude
Those are pens
interlude
```

ちなみに、文字列定数をsingle-quoteで囲ったらエラーが出た。

## Patterns

中括弧の前に色々な条件を指定することでいつそのスクリプトが発火するかを決めることができる様子。
```
$ vim input.txt
$ cat input.txt
This is a pen
Those are pens
It is a pen
There is a pen
$ vim script.awk
$ cat script.wak
BEGIN { num = 0; }
/^T/ { num += 1; }
END { print num; }
$ awk -f script.awk input.txt
3
```

対象の行の一部を使って条件分岐や計算もできる様子。
```
$ vim script.awk
$ cat script.awk
BEGIN { num = 0; }
/^T/ &amp;&amp; $2 == &quot;is&quot; { num += 1; }
END { print num; }
$ awk -f script.awk input.txt
2
```


## Actions

IF分やFOR文、関数なども使えるらしい。
```
$ vim script.awk
$ cat script.awk
BEGIN {
  if (num == &quot;&quot;) {
    num = 2;
  }
  print &quot;START OUTPUT&quot;;
}
/^T/ {
  for (i=0; i&lt;num; i++) {
    print $1;
  }
}
END {
  print &quot;END OUTPUT&quot;
}
$ awk -f script.awk input.txt
START OUTPUT
This
This
Those
Those
There
There
END OUTPUT
```

普通にプログラミング言語なんだなと感じてきた。

## その他

以前tclコマンドの一部を抜き出すという事例があった記憶があるので、それをやってみたい。こんな入力があったときに
```
$ vim input.txt
$ cat input.txt
command1 {argument1=1234} {argument2=string1} {argument3=2345}
command2 {argument2=string1} {argument1=345}
command1 {argument3=4566} {argument1=0987}
command1 {argument1=2345} {argument2=string2} {argument3=0987}
```

`command1`の`argument1`だけを取り出したいという場合のAwkスクリプトは
```
$ vim script.awk
$ cat script.awk
function extract(string) {
  num = 10
  match(string, /argument1=[0-9]+/);
  return substr(string, RSTART+num, RLENGTH-num);
}
BEGIN {
  print &quot;ARGUMENT1&quot;;
}
/^command1/ {
  print extract($0);
}
$ awk -f script.awk input.txt
ARGUMENT1
1234
0987
2345
```

もう少し良いやり方がある気もするが、とりあえず取り出すことはできた。
