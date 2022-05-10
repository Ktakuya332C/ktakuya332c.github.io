# Blog
ブログのソースコード

## 記事の追加
`articles_{ja,en}/`以下に`<記事の名前>.txt`というファイルを作成し、次のようなファイル構成で記事を作成する

```
<タイトル>
<日付(YYYY-MM-DD)>
<コンテンツ>
```

コンテンツは以下で説明する独自の書き方になっている。書き終わったらトップディレクトリから

```
$ python -m cmds.main_ja
$ python -m cmds.main_en
```

と実行すれば、`build_{ja,en}/`以下にそれぞれの記事が生成される。

## 独自記法の文法
通常の文章に加えて、`@`で始まる関数を呼び出すことができるようになっている。例えば

```
これは@a{テストリンク}{http://example.com}です。
```

という文章は、`@a`という名前の関数を呼び出すことによって

```
これは<a href="http://example.com">テストリンク</a>です。
```

という文章にコンパイルされる。

今定義されている関数は下記の関数である。

| 関数名 | 呼び出し例 | 説明
| --- | --- | --- |
| `@p` | `@p{パラグラフ}` | パラグラフ |
| `@a` | `@a{リンク}{http://example.com}` | リンク |
| `@rel` | `@rel{/build/document.html}` | ドキュメントルートからのパス |
| `@ul` | `@ul{アイテム}{他のアイテム}` | 順序なしリスト |
| `@ol` | `@ol{一つ目}{二つ目}` | 順序ありリスト |
| `@def` | `@def{定義名}{定義内容}` | 定義 |
| `@fig` | `@fig{サイズ(e.g. 70)}{@rel{/static/example.png}}` | 画像 |
| `@table` | `@table{項目1,項目2}{データ1,データ2}` | テーブル |
| `@section` | `@section{セクション}` | セクション |
| `@subsection` | `@subsection{サブセクション}` | サブセクション |
| `@quote` | `@quote{これは引用です}` | 引用 |
| `@incode` | `@incode{#include <iostream>}` | inlineコード |
| `@blcode` | `@blcode{int a = 1}` | blockコード |
| `@pre` | `@pre{これはそのまま出力されます}` | そのまま出力 |
| `@inmath` | `@inmath{a^t_k}` | inline-math |
| `@blmath` | `@blmath{\sum_{n=1}^10 = 55}` | block-math |
| `@mermaid` | `@mermaid{graph TD; A-->B;}` | [mermaid](http://mermaid-js.github.io/mermaid/)の出力 |


## 開発
unittestを実行する場合

```
$ python -m unittest discover tests
```

lintをかける場合

```
$ autopep8 -iaar .
```

型チェックをかける場合

```
$ mypy .
```
