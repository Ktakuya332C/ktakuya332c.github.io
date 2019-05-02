Rのパッケージimagerを入れる
2018-12-10


適当にRのパッケージである\a{imager}{https://cran.r-project.org/web/packages/imager/index.html}をインストールしようと思ったらできなかったのでメモ。


とりあえずGoogleで検索するとちょうど同じ問題に突き当たっていた人がStackoverflowで\a{質問}{https://stackoverflow.com/questions/23642353/error-message-installing-cairo-package-in-r}をしていた。解答によればCairoパッケージを入れればいいらしい。とりあえずbrewで入れてみる
\code{
$ brew install cairo
}
と何の問題もなく入ったので、とりあえず再度インストール
\code{
$ r
> install.packages("imager")
}
今度はちゃんと入ってくれた。
