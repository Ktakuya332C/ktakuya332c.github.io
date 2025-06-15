# 傾向スコアマッチングのPython実装

最近よく経済学と機械学習の融合を図るような研究をよく見る[1]のですが、特にその際に重視されているのは因果推論のようです。例えば構造的因果モデルで有名なJuda Pearlさんが出した論文[2]などは現在の機械学習の欠点の一つとして因果的な効果を明示的に取り込むことができないことをあげています。また、実際にデータ分析を行う実務家の方々も使っている様子[3]です。

こういう状況を見て自分も因果推論を勉強してみた[4]のですがいまいち実際にどう使うのかが掴めないので、色々と因果推論の手法を使って見ていきたいと考えています。今回は特に初歩的な手法の一つである傾向スコアマッチングの実装をしてみて感覚を掴みたいと思います。ある統計家の方のブログ記事[5]が傾向スコア関連の分析について詳しい記事を載せていらしたので、まずその記事と同じデータについて傾向スコアマッチングを行なってみて結果が同じになるかどうかから始めようと思います。全く同じことをやってもつまらないので、今回は記事[5]とは異なり、Pythonで推定を行なってみました。

今回の分析では、因果推論では定番[6]らしいLalondeデータセットを使います。1970年代中盤[7]に行われたある職業訓練の効果を測るために行われた研究[8]などで使用されたデータセットです。データは記事[5]に従ってLalondeデータの公式ページと思われる場所[9]から取ってきました。データは185人の処置群と429人の対照群を含んでいます。データは(185+429, 10)の行列として与えられており、それぞれの行は以下の表の意味を持ちます。

| 行番号 | 意味 |
| --- | --- |
| 0 | 職業訓練を受けた(1.0)、受けていない(0.0) |
| 1 | その人の年齢 |
| 2 | 教育を受けた年数 |
| 3 | 黒人である(1.0)、でない(0.0) |
| 4 | ヒスパニックである(1.0)、でない(0.0) |
| 5 | 結婚している(1.0)、していない(0.0) |
| 6 | 高校を卒業した(1.0)、していない(0.0) |
| 7 | 1974年の実質所得(単位はドル、1982年による調整あり) |
| 8 | 1975年の実質所得(単位はドル、1982年による調整あり) |
| 9 | 1978年の実質所得(単位はドル、1982年による調整あり) |

まず、分析に必要なライブラリをimportします。

```
import os
import numpy as np
from sklearn.linear_model
import LogisticRegression
```

次にデータをロードします。データセットは処置群、対照群のデータがどちらもDATA_DIRに存在しているとします。

```
treated = np.loadtxt(os.path.join(DATA_DIR, "treated.txt"))
control = np.loadtxt(os.path.join(DATA_DIR, "control.txt"))
data = np.vstack([treated, control])
t = data[:, 0]
x = data[:, 1:7]
y = data[:, 7:]
```

ここでtは処置パラメータ、xは共変量、yは結果変数を表します。これらについて各実験参加者に対する傾向スコアpをscikit-learnのLogisticRegressionを用いて推定します。

```
model = LogisticRegression()
model.fit(x, t)
p = model.predict_proba(x)[:, 1]
```

scikit-learnのLogisticRegressionは基本的にL2正則化がかかっています[10]が、今回はそのまま使用します。

次に傾向スコアマッチングを行うのですが、マッチングの方法は様々存在します[11]。今回は記事[5]の方法の通りに、Rでの関数MatchItのmethod=nearsetで使用されているNearest Neighbor Matchingを使用します。この手法では各処置群に対して傾向スコアが最も近い対照群の要素をGreedyに選び出していくことで、処置群に対応する対照群の部分集合を取り出します[11]。この方法は以下のように実装できます。

```
def matching(t_vals, c_vals):
  assert len(t_vals) <= len(c_vals)
  idxs = list()
  t_vals = np.sort(t_vals)[::-1]
  for t_val in t_vals:
    srtd = np.argsort(np.abs(c_vals - t_val))
    for idx in srtd:
      if not idx in idxs:
        idxs.append(idx)
        break
  return idxs

idxs = matching(p[t == 1.0], p[t == 0.0])
c_y = y[t == 0.0][idxs]
t_y = y[t == 1.0]
```

このマッチングはもう少し早い実装ができそうですが、今回はサンプル数が比較的少ないのであまり時間はかかりません。

以上のマッチングで得られたデータを使って処置効果を各年に対して計算してみます。

```
c_means = np.mean(c_y, axis=0)
t_means = np.mean(t_y, axis=0)
print("Year", "Control", "Treated")
print(1994, int(c_means[0]), int(t_means[0])) # 1994 2707 2095
print(1995, int(c_means[1]), int(t_means[1])) # 1995 1526 1532
print(1998, int(c_means[2]), int(t_means[2])) # 1998 5274 6349
```

1978年における職業訓練による実質所得への因果効果は6349 - 5274 = 1075ドルと推定されました。これは記事(5)の推定結果とも大まかに一致しています。また1994, 1995, 1998年と徐々にその因果効果が大きくなってることが観察できます。

とりあえず因果効果の推定としては妥当なものを出せたのではないでしょうか。記事[5]ではさらに深い解析を行なっているようなので、以降そちらも試してみたいと思います。

## 参考文献

1. Athey et al. (2017), [Matrix Completion Methods for Causal Panel Data Models](https://arxiv.org/abs/1710.10251)
1. Pearl (2018), [Theoretical Impediments to Machine Learning With Seven Sparks from the Causal Revolution](https://arxiv.org/abs/1801.04016)
1. Muralidharan et al. (2017), [The Unofficial Google Data Science Blog](http://www.unofficialgoogledatascience.com/2017/01/causality-in-machine-learning.html)
1. 星野(2009), [調査観察データの統計科学](https://www.iwanami.co.jp/book/b257892.html)をざっと読んだ。この本を選んだ理由は界隈では[勉強会なども開かれており](http://takehiko-i-hayashi.hatenablog.com/entry/20120427/1335475881)有名な本らしいから。
1. Ellis (2017), [Exploring propensity score matching and weighting](http://ellisp.github.io/blog/2017/04/09/propensity-v-regression)
1. [R用のLalondeデータパッケージ](https://github.com/jjchern/lalonde)があるくらいなので多分定番のはず。
1. LaLonde (1986), Evaluating the Econometric Evaluations of Training Programs with Experimental Data
1. Dehejia et al. (1999), Causal Effects in Nonexperimental Studies: Reevaluating the Evaluation of Training Programs
1. Dehejiaさんの個人ホームページの[データページ](http://users.nber.org/~rdehejia/nswdata2.html)から処置群として"nswre74_treated.txt"を、対照群として"cps3_controls.txt"を取ってきた。その後、処置群のデータは"treated.txt"、対照群のデータは"control.txt"と名前を変えて使用している。
1. scikit-learnの[LogisticRegressionのページ](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)にはInverse of regularization strength Cがデフォルトで1.0となっていると書かれている。
1. Ho et al. (2011), [MatchIt: Nonparametric Preprocessing for Parametric Causal Inference](https://imai.princeton.edu/research/files/matchit.pdf)
