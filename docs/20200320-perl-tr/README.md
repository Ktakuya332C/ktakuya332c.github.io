# perlのtr演算子

perlのtr演算子を使っているコードを見たのだが、いまいち意味がわからなかったので使い方をメモして置く。

## 基本的な使い方まとめ
`tr`演算子は当てはまる文字を対応する文字に変換する機能の様子。例えば
```
-bash$ perl -e '
$string = "this is a pen";
$string =~ tr/a-z/A-Z/;
print "$string\n";
'
THIS IS A PEN
```

という感じで、一文字一文字を対応する文字に変換することができる機能な様子。他にも
```
-bash$ perl -e '
$string = "this is a pen";
$string =~ tr/a-z/A/;
print "$string\n";
'
AAAA AA A AAA
```

などとして、全ての文字を一つの文字に置き換えることもできる模様。
変換後の文字を、変換前の文字の数と同じでもなく、一つでもない、適当な数置いてみるとどうなるか気になったのでやってみると、
```
-bash$ perl -e '
$string = "abcdefghi";
$string =~ tr/a-z/AB/;
print "$string\n";
'
ABBBBBBBB
```

となり、どうも変換前の文字の対応が決定されていないときは最後の文字が使われるらしい。

## オプション
`qw`コマンドと同じく`tr`コマンドにもオプションがいくつかあるらしい。
まずは`c`オプションを取り上げると、このオプションは補集合を表すらしく、変換前の文字を補集合で設定できるらしい。`abc`に含まれる文字以外を`A`に変換せよというコマンドを打ってみると
```
-bash$ perl -e '
$string = "abcdefghi";
$string =~ tr/abc/A/c;
print "$string\n";
'
abcAAAAAA
```

となり、期待通りになった。
`d`オプションは、変換前の文字に対して対応する変換後の文字がなかったらその文字を削除する様子。
```
-bash$ perl -e '
$string = "abcdefghi";
$string =~ tr/a-z/AB/d;
print "$string\n";
'
AB
```

確かに、`d`オプションをつけない時は`B`が繰り返されていたが、今回は繰り返されていた文字が消えた。
`s`オプションは置換された文字が連続した時に圧縮するオプションらしく、例えば
```
-bash$ perl -e '
$string = "abcdefghi";
$string =~ tr/a-z/A/s;
print "$string\n";
'
A
```

となるようす。全部`A`に置換されて、それらが圧縮された感じ。

## 最後に

`tr`が使われていたのはこういう感じ
```
$string =~ tr,\n\t , ,s
```

だったのだが、今なら意味がわかる。要するに空白っぽい文字を全部一つの空白にまとめましょうという意味。なので実際に使うとしたら
```
-bash$ perl -e '
$string = "
This  is a pen
Those   are   pens
";
$string =~ tr,\n\t , ,s;
print "$string\n";
'
 This is a pen Those are pens
```

となって、確かに空白っぽい文字が全部一つの空白に変換されている。
