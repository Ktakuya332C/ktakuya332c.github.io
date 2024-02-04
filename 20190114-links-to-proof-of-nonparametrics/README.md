# nonparametric統計検定手法の導出へのリンク

統計的な検定手法についての本は大抵次のどちらかに別れる。

1. 統計的な検定を使用する人用の本で、どのような場合にどの手法を使えば良いかが書かれているが、どのようにそれらの検定手法が導出されたかが書かれていない。たとえば[Handbook of Biological Statistics](http://www.biostathandbook.com/)などがその系統。
1. 統計学を学ぶ人用の本で、一般的な統計学の定理などの導出などはきちんと書かれているが、統計的な検定手法について上記の本で紹介されているくらい深く掘り下げてはいない。例えば Elementary statistics (by Paul G. Hoel) などがある。


最近nonparametric統計の手法を使って検定を行わないといけない事案に幾度か遭遇して、その度に上で言うところの1の系統の本にあたってどの検定手法が最も適しているかを探っていたのだが、どれもやはり導出が書いていないのでどのような過程を置いているかがわかりずらく、この検定手法があってるかなと思ってとりあえずGoogle検索すると違う手法の方が良いと言われることが多かった。かといって2の系統の本には大抵カイ二乗検定くらいの導出で本が終わっており、nonparametrics系の検定手法について書かれていることは少なかった。

nonparametrics系まで導出まで書いてくれている本はないかと探したがなかったので、取り合えず最近出会ったnonparametrics系の導出の参考になりそうなリンクを貼っておく。導出を忘れてどれがいいか迷った時はまたここに戻ってくる予定。

- Chi squared: [Penn State University の授業資料かも](http://personal.psu.edu/drh20/asymp/fall2006/lectures/ANGELchpt07.pdf)
- Mann Whitney: [MITの数学科の授業資料かも](https://math.mit.edu/~rmd/650/nonpartests.pdf)
- Kruskal Wallis: W.H.Kruskal and W.A.Wallis (1952), [Use of ranks in one-criterion variance analysis](https://people.ucalgary.ca/~jefox/Kruskal%20and%20Wallis%201952.pdf)
- Kendall's tau: M.G.Kendall (1938), [A new measure of rank correlation](https://www.jstor.org/stable/pdf/2332226.pdf?seq=1#page_scan_tab_contents), JSTORなので一月に読める回数制限あり。


ざっと見た感じ、どのnonparametricsの導出も大学受験の感じな確率論を使って対象の統計量の平均値と分散値を導出したのちに、中心極限定理を使ってその平均と分散を持つ正規分布に近づくという近似を使っているように見えた。それほど複雑な導出ではないように見えるので、使う前には一度思い出してみるのも良いかもしれない。
