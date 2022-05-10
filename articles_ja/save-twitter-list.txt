Twitterのリストのバックアップを取る
2018-12-28

@p{Twitterのリストをバックアップする機能が本家になかったので、無理やりスクレイピングしてアカウント名を保存した。}

@p{基本的にはまず保存したいリストのユーザー一覧のページにアクセスする。基本的には次のような形になっているはず。}

@blcode{
https://twitter.com/<ユーザー名>/lists/<リスト名>/members
}

@p{単純にこのページを取ってくるだけで良いのなら簡単なのだが、スクロールして最後まで行かないと全てのアカウントがhtmlに現れないので手でスクロールする。スクロールしたらその画面のhtmlをどのような方法でも良いのでローカルに保存する。とりあえず自分はChromeの保存機能を使って保存をおこなった。}

@p{保存したhtmlファイルを@incode{members.htm}として、あとはここからメンバーのアカウント一覧を取ってくるだけ。とりあえず@incode{rvest}ライブラリを使って取り出して見る。}

@blcode{
$ r
> library(tidyverse)
> library(rvest)
> members <- read_html("members.htm") %>%
+   html_nodes(".account") %>%
+   html_attr("data-screen-name")
}

@p{これでmembers変数にはアカウントからアットマークを取ったものが入っている。あとは適当に何処かに保存しておくだけだ。}

@blcode{
> write(members, "members.txt")
}

@p{rvestライブラリが以下に簡単にhtmlを扱えるかがわかる。}
