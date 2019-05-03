blog
---
ブログのソースコード

## 記事の追加
`articles/`以下に`<記事の名前>.md`というファイルを作成し、特殊なマークダウン方式で記述を行う。最初の行はその記事のタイトルを書き、次の行には日付を`yyyy-mm-dd`の形で書く。それ以降に独自Markdownの記法で本文を書く。描き終わったらトップディレクトリで
```
$ python main.py
```
とすれば`index.html`と`build/`以下の記事が生成される。

## 独自Markdown
独自Markdownは次のような記法を持つ。
* 段落の区切りは`\n\n\n`で表される。要するにMarkdown上で2行分改行を行えば段落が切り替えられる。
* Markdown上で段落の最初に現れる文字が以下のどれかの文字列であれば、その段落全体に規定の修飾が加えられる。それら段落修飾子の次には空白がなければならない。
  * '#'はセクションのタイトルを表す。
  * '>'は引用を表す。
* Markdown上でバックスラッシュから始まる記号は関数を示し、それにつづくかっこに囲われた文字列を引数として規定のhtmlノードを作成する。
  * `\code`関数はコードを表す引数を一つとり、highlightjsでハイライトされたコードを表示する
  * `\ul`関数はいくつかの引数を取り、順序のないリストを表示する
  * `\ol`関数はいくつかの引数を取り、順序のあるリストを表示する
  * `\a`関数はテキストとリンクURLを取り、そのテキストにリンクを貼ったものを表示する
  * `\def`関数は定義の名前とその内容の二つの引数を取り、TEXにおけるtheoremのようなものを出力する
  * `\rel`関数は他の記事の名前を引数として取り、その記事へのリンクURLを返す
  * `\emp`関数は引数をひとつとり、通常のMarkdownでのbacktickと同じ働きをする
  * `\table`関数はコンマ区切りの引数をいくつかとり、それらを並べたテーブルを表示する
  * `\fig`関数は画像へのリンクURLをとり、その画像を表示する

## Unittestの実行
`tests/`以下に含まれるunittestを実行するには
```
$ python -m unittest discover tests
```
とすれば良い。
