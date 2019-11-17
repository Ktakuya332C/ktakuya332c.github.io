Rのパッケージimagerを入れる
2018-12-10

@p{適当にRのパッケージである@a{imager}{https://cran.r-project.org/web/packages/imager/index.html}をインストールしようと思ったらできなかったのでメモ。}

@p{とりあえずGoogleで検索するとちょうど同じ問題に突き当たっていた人がStackoverflowで@a{質問}{https://stackoverflow.com/questions/23642353/error-message-installing-cairo-package-in-r}をしていた。解答によればCairoパッケージを入れればいいらしい。とりあえずbrewで入れてみる}

@blcode{
$ brew install cairo
}

@p{と何の問題もなく入ったので、とりあえず再度インストール}

@blcode{
$ r
> install.packages("imager")
}

@p{今度はちゃんと入ってくれた。}
