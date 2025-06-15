# アナリストは何をしている?

自分が現エンジニアなこともあってデータサイエンスの仕事をしている=機械学習をしているくらいの認識だったのだが、以前調べてみたところによるとどうもそんな感じでもないということがわかってきたので、それ以外の人は何をしているのだろうというのを調べてみたい。一般用語として正しく認識されているかどうかはわからないが、とりあえず[この動画](https://www.youtube.com/watch?v=l05OHGUyK-E)によれば、Machine Learning Engineer というのが一般的に機械学習を使ってソフトウェアエンジニアのことで、Data Scientist というのはもっとビジネスよりの人たちのことを言うようだ。データサイエンスと言う言葉で機械学習エンジニアのことを指している記事などもよく見るのでまあそこは曖昧なのだろう。今回の記事ではエンジニアとしてではなくビジネスとしてやっている人たちが何をしているのかを探りたい。

とりあえず調べて行って一つ目に見つけたのがmickさんの記事

- [データアナリストのスキルセット](https://custle.hatenablog.com/entry/2019/11/04/110529)
- [データ分析の仕事って何するの？](https://custle.hatenablog.com/entry/2019/04/29/120034)

最近までこれらの記事の存在を知らなかったのだが、とてもよくまとまっていて参考になる。具体的にやっていることとしてはKPI設計、需要予測、効果検証、構造分析やKPIモニタリングなどが挙げられていて、先に紹介した動画とも一致する内容だ。意思決定を支えるためにデータを分析することが仕事であると言うのは [Decision Intelligence](https://towardsdatascience.com/introduction-to-decision-intelligence-5d147ddab767) という言葉があることからも知ってはいたが、具体化したときにKPIの設計などもそれに入るというのはあまり具体的に思いついていなかった。[データアナリストはカーナビのようなものである](https://custle.hatenablog.com/entry/2019/09/28/104221)という記事にもあるように何をすればよくなるのかというを具体的な数値まで落として議論することがデータアナリストの目的であり、そのためにはそもそも何を目指しているのかを数値ができないと議論を始めることすらできないということなのだろう。

次に見つけたのが Joma Tech さんのYoutubeチャンネル。Facebookの Data Scientist, Product の仕事を以前行なっていたらしく、その仕事関連の話題をYoutubeで流してくれている。

- [What REALLY is Data Science? Told by a Data Scientist](https://www.youtube.com/watch?v=xC-c7E5PK0Y)
- [3 Types of Data Science Interview Questions](https://www.youtube.com/watch?v=4Z6lxfglvUU)
- [Why I left my Data Science Job at FANG](https://www.youtube.com/watch?v=M5v1nXiUaOI)

面白かったのはデータサイエンスの仕事につくときに尋ねられる interview question を色々と説明してくれている動画で、実際仕事をしているときにどういうことをやっているのかというのの一端をみれている気がした。確かに interview question からその仕事内容を探るというのもまあ良い手だなと思ったのでfacebookのそのポジションの interview question を見てみると、実際にインタビューにくる人に当てたメールが出てきた。

- [How would you prepare for Data scientist (Analytics) role at Facebook?](https://www.quora.com/How-would-you-prepare-for-Data-scientist-Analytics-role-at-Facebook)

それらの記事を総合するとこういう感じのことが尋ねられるらしい

1. Product Interpretation: ケーススタディーを使ってどうやって製品を改善させていくかを問う質問
1. Applied Data: どうやって一般的な製品の問題をデータで答えられる質問に落としていくかを問う質問
1. Quantitative Analysis: 数理的、統計的な知識を問う質問
1. Technical Analysis: SQLとかの質問らしい
1. Data Transformation: データをどうやって変形させていくかみたいな質問らしい
1. Technical Software Engineering: 競技プログラマイングみたいな質問みたい

後半はハード的な知識で、「データサイエンス」という一般的な名称から想像される技術内容としては普通なので想像通り。ただし前半の二つは実際に仕事でやっていることを質問として問うているようなのでこれは面白い。基本的にはどうやってデータを使って製品を改善させていくかみたいなものが問われているらしく、これはまあ普通に「データサイエンス」として統計とか機械学習とかを学んでいてもあまり気づかないものだろう。

もっと具体的にどういう感じなのかを知りたいなと思って調べていたらこういう記事に突き当たった。

- [7 Steps to Ace a Data Scientist Job Interview in Silicon Valley. Part 1: Analytics/Inference Track](https://medium.com/%40skills_ai/7-steps-to-prepare-for-a-data-scientist-interview-part-1-analytics-inference-track-c08a7fdbdb15)
- [How to land a Data Scientist job at your dream company — My journey to Airbnb](https://elu.nl/how-to-land-a-data-scientist-job-at-your-dream-company%E2%80%8A-%E2%80%8Amy-journey-to-airbnb/)

どうもデータを使ってどうやって製品を改善させていくかみたいな知識は「Product Sense」という言葉でまとめられているらしく、その参考図書としてあげられているのは以下の二つの本だった。

- [Lean Analytics](https://www.amazon.com/Lean-Analytics-Better-Startup-Faster/dp/1449335675)
- [Cracking the PM Interview](https://www.amazon.com/Cracking-PM-Interview-Product-Technology-ebook/dp/B00ISYMUR6)

この Lean Analytics という本の方を読んでみたが非常に面白かった。どうやってデータを持って製品の改善を導いていくかということが Lean Startup の文脈で書かれている上に、その具体例が色々と乗っていたので参考になった。特にいくつかの業種に対して具体的にどのようなKPIを立ててその製品の改善方法を導いていけばいいかみたいなことが書かれている章があり、どのようにユーザーがその製品とか変わるかというののメンタルモデルを持った上で、ユーザーが最終的にお金を落としてくれるようになるまでを考え、その要所要所をデータで計測して改善していくという考え方は、すごい目新しいという感じではないが、すぐに思いつく感じのものでもなかった。

また、この「Product Sense」の質問は多くの Product Manager のinterviewでも尋ねられるようで、以下のサイトにいくつも事例が載っていた。

- [Prepare for Product Manager Job Interviews](https://www.productmanagementexercises.com/metrics)
