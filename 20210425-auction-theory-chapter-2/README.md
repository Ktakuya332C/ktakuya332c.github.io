# クリシュナ本の2章のまとめ

オークション理論に関する次の本を読み進めている。

- V.クリシュナ、[オークション理論](https://www.amazon.co.jp/dp/4502237612)

今回はこの本の2章で紹介されている内容をまとめていく。

## 概要

2章では次の4つの種類のゲームの分析を行っている。

1. 留保価格なし二位価格オークション
1. 留保価格なし一位価格オークション
1. 留保価格付き二位価格オークション
1. 留保価格付き一位価格オークション

これらは全て次の形のゲームの特別な場合となっている。
> *私的評価値のオークション*  
> 私的評価値のオークションは次の要素からなる不完備情報ゲームである。

1. プレイヤーの集合$\mathcal{N} = \{1, 2, \cdots, N\}$
1. 各プレイヤー$i \in \mathcal{N}$に関する行動集合$\mathcal{B}_i = \mathcal{B} = \mathbb{R}_{\ge 0}$
1. 各プレイヤー$i \in \mathcal{N}$に関するシグナル集合$\mathcal{X}_i = \mathcal{X} = \mathbb{R}_{\ge 0}$
1. シグナルの積集合$\prod_{i=1}^N \mathcal{X}_i$上の確率密度関数$h$
1. 各プレイヤーに関する利得関数$u_i: \prod_{j=1}^N \mathcal{B}_j \times \prod_{j=1}^N \mathcal{X}_j \rightarrow \mathbb{R}$

ただしここでシグナルの積集合上の確率密度関数$h$は各プレイヤーのシグナルについて独立であり
$$
h(x_1, x_2, \cdots, x_N) = \prod_{i=1}^N f_i(x_i)
$$

かつ全て同じ分布であると仮定する。
$$
f_1 = f_2 = \cdots = f_N = f
$$

以降では上記4つのゲームそれぞれに対して

1. ゲームの対称的なベイジアンナッシュ均衡の計算
1. ベイジアンナッシュ均衡下での売り手の収入の計算

をおこない、それぞれの形式の特徴を比較していく。

## 順序統計に関する記号の整理

それぞれのゲームの解析を行う前に順序統計に関する記号の整理を行っておく。以下ではこれらの記号を使っていくことにする。

- シグナルの確立密度関数$f$
- シグナルの分布関数$F$
- シグナル集合$\mathcal{X}$に値を取り確立密度変数$f$を持つ確率変数$X$
- $N$個のシグナル$X_i$をサンプルした時の最大値の確立密度関数$g^{(N)}_1$
- $N$個のシグナル$X_i$をサンプルした時の最大値の分布関数$G^{(N)}_1$
- $N$個のシグナル$X_i$をサンプルした時の最大値を表す確率変数$Y^{(N)}_1$
- $N$個のシグナル$X_i$をサンプルした時の二位値の確立密度関数$g^{(N)}_2$
- $N$個のシグナル$X_i$をサンプルした時の二位値の分布関数$G^{(N)}_2$
- $N$個のシグナル$X_i$をサンプルした時の二位値を表す確率変数$Y^{(N)}_2$

ただし個数$N$が自明な場合は$g_1, G_1, Y_1$などと表す場合もある。

## 留保価格なし二位価格オークション

このオークションは、私的評価値のオークションにおける利得関数$u_i$が
$$
u_i(\bm{b}, \bm{x}) = (x_i - \max_{j \neq i} b_j) I(b_i > \max_{j \neq i} b_j)
$$

である場合に当たる。ただしここで$I$は指示関数である。

### 対称的なベイジアンナッシュ均衡の計算(1)

ベイジアンナッシュ均衡を求める際には、まず各プレイヤーによる最適反応戦略を求める必要がある。各プレイヤー$i$の最適反応戦略とは、他のプレイヤーの戦略を$\beta_j: \mathcal{X}_j \rightarrow \mathcal{A}_j$と書いたときに
$$
\beta^*_i(x_i, \bm{\beta}_{-i}) = \argmax_{b_i} E[u_i(b_i, \bm{\beta}_{-i}(\bm{X}_{-i}), \bm{X}) | X_i = x_i]
$$

と表現される戦略のことである。これから列挙するいくつかの事実を使えば

- 対称的な解のみに興味があるため、$\beta_j = \beta$と書いて良い
- 私的価値$x$が大きい場合に入札価格$b=\beta(x)$が上昇するのは自明なので$\beta$は非減少関数
- $\max_{j \neq i} x_j$は$g^{(N-1)}_1$に従う確率変数$Y^{(N-1)}_1$である

期待値は次のように変形できる。
$$
\begin{aligned}
&\quad E[u_i(b_i, \bm{\beta}_{-i}(\bm{X}_{-i}), \bm{X}) | X_i = x_i] \\
&= E[(x_i - \max_{j \neq i} \beta_j(X_j)) I(b_i > \max_{j \neq i} \beta_j(X_j))] \\
&= E[(x_i - \max_{j \neq i} \beta(X_j)) I(b_i > \max_{j \neq i} \beta(X_j))] \\
&= E[(x_i - \beta(\max_{j \neq i} X_j)) I(b_i > \beta(\max_{j \neq i} X_j))] \\
&= E[(x_i - \beta(Y^{(N-1)}_1)) I(b_i > \beta(Y^{(N-1)}_1))] \\
&= \int_0^{\beta^{-1}(b_i)} (x_i - \beta(y)) g^{(N-1)}_1(y) dy \\
&= x_i G^{(N-1)}_1(\beta^{-1}(b_i)) - \int_0^{\beta^{-1}(b_i)} \beta(y) g^{(N-1)}_1(y) dy \\
&= (x_i - b_i) G^{(N-1)}_1(\beta^{-1}(b_i)) + \int_0^{\beta^{-1}(b_i)} G^{(N-1)}_1(y) \beta'(y) dy \\
&= (x_i - b_i) G^{(N-1)}_1(\beta^{-1}(b_i)) + \int_0^{b_i} G^{(N-1)}_1(\beta^{-1}(z)) dz
\end{aligned}
$$

増減を調べるために$b_i$で微分すると
$$
\frac{\partial}{\partial b_i} E[u_i(b_i, \bm{\beta}_{-i}(\bm{X}_{-i}), \bm{X}) | X_i = x_i] = (x_i - b_i) \frac{\partial G^{(N-1)}_1(\beta^{-1}(z))}{\partial b_i}
$$

$\beta^{-1}$と$G^{(N-1)}$がどちらも非減少であるため、値の正負は$x_i - b_i$のみで定まる。よって、プレイヤー$i$の最適反応は
$$
\beta^*_i(x_i, \bm{\beta}_{-i}) = x_i
$$

であり、これは他のプレイヤーの戦略に依存しないため支配戦略均衡でもある。

### 売り手の収入

先の均衡においてプレイヤー$i$が支払う金額の期待値は、私的評価値が$x_i$だった場合
$$
\begin{aligned}
&\quad E[(\max_{j \neq i} X_j) I(x_i > \max_{j \neq i} X_j)] \\
&= E[Y^{(N-1)}_1 I(x_i > Y^{(N-1)}_1)] \\
&= \int^{x_i}_0 y g^{(N-1)}_1(y) dy \\
&= E[Y^{(N-1)}_1 | Y^{(N-1)}_1 < x_i] G^{(N-1)}_1(x_i)
\end{aligned}
$$

となる。売り手が得られる収入の期待値は以下のように計算できる。
$$
\begin{aligned}
N E[E[Y^{(N-1)}_1 | Y^{(N-1)}_1 < x_i]G^{(N-1)}_1(x_i)] &= N \int_0^{\infty} dx_i f(x_i) \int_0^{x_i} dy y g^{(N-1)}_1(y) \\
&= N \int_0^{\infty} dy y g^{(N-1)}_1(y) \int_y^\infty dx_i f_(x_i) \\
&= N \int_0^{\infty} dy y g^{(N-1)}_1(y) (1 - F(y)) \\
&= E[Y^{(N)}_2]
\end{aligned}
$$

## 留保価格なし1位価格オークション

このオークションは、私的評価値のオークションにおける利得関数$u_i$が
$$
u_i(\bm{b}, \bm{x}) = (x_i - b_i) I(b_i > \max_{j \neq i} b_j)
$$

である場合に当たる。ただしここで$I$は指示関数である。

### 対称的なベイジアンナッシュ均衡の計算

ベイジアンナッシュ均衡を求める際には、まず各プレイヤーによる最適反応戦略を求める必要がある。今回の場合条件付き期待値は以下のように計算できるため
$$
\begin{aligned}
E[u_i(b_i, \bm{\beta}_{-i}(\bm{X}_{-i}), \bm{X}) | X_i = x_i] &= (x_i - b_i) E[I(b_i > \max_{j \neq i} \beta(X_j))] \\
&= (x_i - b_i) E[I(b_i > \beta(Y_1^{(N-1)}))] \\
&= (x_i - b_i) G_1^{(N-1)}(\beta^{-1}(b_i))
\end{aligned}
$$

その値が最大になるような入札額$b_i$はその一次条件
$$
\begin{aligned}
0 &= \frac{\partial}{\partial b_i} E[u_i(b_i, \bm{\beta}_{-i}(\bm{X}_{-i}), \bm{X}) | X_i = x_i] \\
&= - G_1^{(N-1)}(\beta^{-1}(b_i)) + (x_i - b_i) g_1^{(N-1)}(\beta^{-1}(b_i)) \frac{1}{\beta'(\beta^{-1}(b_i))}
\end{aligned}
$$

を満たす必要がある。この式を満たすような$b_i$を直接計算できる気はしないが、均衡においてはこの式は成立しているはずなので、$b_i = \beta(x_i)$を代入して何が言えるかを見てみる。
$$
\begin{aligned}
&\quad 0 = - G_1^{(N-1)}(x_i) + (x_i - \beta(x_i)) g_1^{(N-1)}(x_i) \frac{1}{\beta'(x_i)} \\
&\iff G_1^{(N-1)}(x_i) \beta'(x_i) + \beta(x_i) g_1^{(N-1)}(x_i) = x_i g_1^{(N-1)}(x_i) \\
&\iff \frac{d}{dx_i} (G_1^{(N-1)}(x_i) \beta(x_i)) = x_i g_1^{(N-1)}(x_i) \\
&\iff G_1^{(N-1)}(x_i) \beta(x_i) = \int^{x_i}_0 z_i g_1^{(N-1)}(z_i) dz_i \\
&\iff \beta(x_i) = E[Y^{(N-1)}_1 | Y^{(N-1)}_1 < x_i]
\end{aligned}
$$

戦略として妥当そうな形が導出できたので、本当にこれが均衡になっているかを確かめる。あるプレイヤー$i$以外のプレイヤーがこの戦略$\beta$に沿っているとき、私的評価値が$x_i$だったプレイヤー$i$が得られる利得は
$$
E[u_i(b_i, \bm{\beta}_{-i}(\bm{X}_{-i}), \bm{X}) | X_i = x_i] = (x_i - b_i) G_1^{(N-1)}(\beta^{-1}(b_i))
$$

となる。便宜的に$b_i = \beta(z_i)$と変数変換をすれば
$$
\begin{aligned}
(x_i - b_i) G_1^{(N-1)}(\beta^{-1}(b_i)) &= (x_i - \beta(z_i)) G_1^{(N-1)}(z_i) \\
&= (x_i - E[Y^{(N-1)}_1 | Y^{(N-1)}_1 < x_i]) G_1^{(N-1)}(z_i) \\
&= x_i G_1^{(N-1)}(z_i) - \int^{z_i}_0 w_i g_1^{(N-1)}(w_i) dw_i \\
&= (x_i-z_i) G_1^{(N-1)}(z_i) + \int^{z_i}_0 G_1^{(N-1)}(w_i) dw_i
\end{aligned}
$$

と変形できる。この増減を調べるために微分すると
$$
\frac{\partial}{\partial z_i} E[u_i(b_i, \bm{\beta}_{-i}(\bm{X}_{-i}), \bm{X}) | X_i = x_i] = (x_i - z_i) g_1^{(N-1)}(z_i)
$$

となり、$x_i = z_i$すなわち$b_i = \beta(x_i)$が最適であることがわかる。これはそのままプレイヤー$i$も戦略$\beta$をとるのが最適であることを示している。よってベイジアンナッシュ均衡は以下のようになる。
$$
\beta^*(x_i, \bm{\beta}_{-i}) = E[Y^{(N-1)}_1 | Y^{(N-1)}_1 < x_i]
$$

### 売り手の収入(1)

先の均衡においてプレイヤー$i$が支払う金額の期待値は、私的評価値が$x_i$だった場合
$$
\begin{aligned}
&\quad E[\beta(X_i) I(\beta(X_i) > \max_{j \neq i} \beta(X_j)) | X_i = x_i] \\
&= \beta(x_i) E[I(\beta(x_i) > \beta(Y^{(N-1)}_1))] \\
&= E[I(\beta(x_i) > \beta(Y^{(N-1)}_1))] G^{(N-1)}_1(x_i)
\end{aligned}
$$

となり、二位価格オークションの場合と同じになる。よって売り手が得られる収入の期待値も同じ値になる。
$$
N E[E[I(\beta(x_i) > \beta(Y^{(N-1)}_1))] G^{(N-1)}_1(x_i)] = E[Y^{(N)}_2]
$$

## 留保価格あり二位価格オークション

このオークションは、私的評価値のオークションにおける利得関数$u_i$がある非負の実数$r$をつかって
$$
u_i(\bm{b}, \bm{x}) = (x_i - \max(\{b_j\}_{j \neq i}, r)) I(b_i > \max(\{b_j\}_{j \neq i}, r))
$$

と表される場合である。ただしここで$I$は指示関数である。

### 対称的なベイジアンナッシュ均衡の計算(2)

ベイジアンナッシュ均衡を求める際には、まず各プレイヤーによる最適反応戦略を求める必要がある。今回の場合条件付き期待値は以下のように計算できる。
$$
\begin{aligned}
&\quad E[u_i(b_i, \bm{\beta}_{-i}(\bm{X}_{-i})) | X_i = x_i] \\
&= E[(x_i - \max(\{\beta(X_j)\}_{j \neq i}, r)) I(b_i > \max(\{\beta(X_j)\}_{j \neq i}, r))] \\
&= E[(x_i - \max(\max_{j \neq i}\beta_j(X_j), r)) I(b_i > \max(\max_{j \neq i}\beta_j(X_j), r))] \\
&= E[(x_i - \max(\beta_j(Y^{(N-1)}_1), r)) I(b_i > \max(\beta(Y^{(N-1)}_1), r))] \\
&= \int_0^{\beta^{-1}(r)} (x_i - r) I(b_i > r) g^{(N-1)}_1(y) dy + \int_{\beta^{-1}(r)}^\infty (x_i - \beta(y)) I(b_i > \beta(y)) g^{(N-1)}_1(y) dy \\
&= (x_i - r) I(b_i > r) G^{(N-1)}_1(\beta^{-1}(r)) + I(b_i > r) \int_{\beta^{-1}(r)}^{\beta^{-1}(b_i)} (x_i - \beta(y)) g^{(N-1)}_1(y) dy \\
&= I(b_i > r) [ (x_i - r) G^{(N-1)}_1(\beta^{-1}(r)) + x_i (G^{(N-1)}_1(\beta^{-1}(b_i)) - G^{(N-1)}_1(\beta^{-1}(r))) ] \\
&\quad - I(b_i > r) \int_{\beta^{-1}(r)}^{\beta^{-1}(b_i)} \beta(y) g^{(N-1)}_1(y) dy \\
&= I(b_i > r) [x_i G^{(N-1)}_1(\beta^{-1}(b_i)) - r G^{(N-1)}_1(\beta^{-1}(r)) ] \\
&\quad - I(b_i > r) [ b_i G^{(N-1)}_1(\beta^{-1}(b_i)) - r G^{(N-1)}_1(\beta^{-1}(r)) - \int_{\beta^{-1}(r)}^{\beta^{-1}(b_i)} \beta'(y) G^{(N-1)}_1(y) dy ] \\
&= I(b_i > r) [ (x_i - b_i) G^{(N-1)}_1(\beta^{-1}(b_i)) + \int^{b_i}_r G^{(N-1)}_1(\beta^{-1}(z)) dz]
\end{aligned}
$$

$I(b_i > r)$を除けば$b_i = x_i$で最大値をとる上に凸な関数である。よって、$x_i > r$の時の最適反応戦略は$b_i = x_i$で入札することである。$x_i \le r$の時は$I(b_i > r)$を除いた関数が最大になるのは$b_i = r$としたときになるが、その時の利得関数の値は
$$
(x_i - r) G^{(N-1)}_1(\beta^{-1}(r)) < 0
$$

となり、値が負になるため$b_i < r$の価格で入札し絶対に競り落とさないのが最適反応戦略である。まとめれば
$$
\beta^*(x_i, \bm{\beta}_{-i}) = \begin{cases}
x_i & x_i > r \\
0 & x_i \le r
\end{cases}
$$

などとなる。さらに、この戦略は他のプレイヤーの戦略に依存しないため、同時に支配均衡戦略になっている。

### 売り手の収入(2)

先の均衡においてプレイヤー$i$が支払う金額の期待値は、私的評価値が$x_i > r$だった場合
$$
\begin{aligned}
&\quad E[(\max(\{\beta(X_j)\}_{j \neq i}, r)) I(\beta(x_i) > \max(\{\beta(X_j)\}_{j \neq i}, r))] \\
&= E[(\max(\beta(Y^{(N-1)}_1), r)) I(x_i > \max(\beta(Y^{(N-1)}_1), r))] \\
&= \int_0^{\beta^{-1}(r)} r I(x_i > r)g^{(N-1)}_1(y) dy + \int_{\beta^{-1}(r)}^{\infty} \beta(y) I(x_i > \beta(y)) g^{(N-1)}_1(y) dy \\
&= r G^{(N-1)}_1(\beta^{-1}(r)) + \int_{\beta^{-1}(r)}^{\beta^{-1}(x_i)} \beta(y) g^{(N-1)}_1(y) dy \\
&= r G^{(N-1)}_1(r) + \int_r^{x_i} y g^{(N-1)}_1(y) dy
\end{aligned}
$$

となり、私的評価値が$x_i \le r$だった場合は$0$になる。よって売り手の期待収入は
$$
\begin{aligned}
&\quad N E[E[(\max(\{\beta(X_j)\}_{j \neq i}, r)) I(\beta(x_i) > \max(\{\beta(X_j)\}_{j \neq i}, r))]] \\
&= N r (1 - F(r)) G^{(N-1)}_1(r) + N \int_r^\infty dx_i f(x_i) \int_r^{x_i} dy y g^{(N-1)}_1(y) \\
&= N r (1 - F(r)) G^{(N-1)}_1(r) + N \int_r^\infty dy y g^{(N-1)}_1(y) \int^\infty_r dx_i f(x_i) \\
&= N r (1 - F(r)) G^{(N-1)}_1(r) + N \int_r^\infty dy y g^{(N-1)}_1(y) (1 - F(y))
\end{aligned}
$$

と表現できる。

## 留保価格あり一位価格オークション

このオークションは、私的評価値のオークションにおける利得関数$u_i$がある非負の実数$r$をつかって
$$
u_i(\bm{b}, \bm{x}) = (x_i - \max(b_i, r)) I(b_i > \max(\{b_j\}_{j \neq i}, r))
$$

と表される場合である。ただしここで$I$は指示関数である。

### 対称的なベイジアンナッシュ均衡の計算(3)

まず利得の期待値は
$$
E[u_i(b_i, \bm{\beta}_{-i}(\bm{X}_{-i})) | X_i = x_i] = (x_i - b_i) I(b_i > r) G(\beta^{-1}(b_i))
$$

となる。指示関数の微分をデルタ関数として、留保価格なし一位価格オークションの時の計算と同じことを行えば、戦略$\beta$が満たすべき式として
$$
\begin{aligned}
&\quad I(z_i > \beta^{-1}(r))[ \beta^{-1}(r) G^{(N-1)}_1(\beta^{-1}(r)) + \int_{\beta^{-1}(r)}^{z_i} w_ig^{(N-1)}_1(w_i) dw_i ] \\
&= I(z_i > \beta^{-1}(r)) G^{(N-1)}_1(z_i) \beta(z_i)
\end{aligned}
$$

となる。$z_i \rightarrow \beta^{-1}(r)$の極限を取れば
$$
\begin{aligned}
&\quad \beta^{-1}(r) G^{(N-1)}_1(\beta^{-1}(r)) = G^{(N-1)}_1(\beta^{-1}(r)) r \\
&\iff \beta^{-1}(r) = r
\end{aligned}
$$

が導けるので、先の式は次の式と同値になる。
$$
I[z_i > r]( r G^{(N-1)}_1(r) + \int_r^{z_i} w_ig^{(N-1)}_1(w_i) dw_i ) = I(z_i > r) G^{(N-1)}_1(z_i) \beta(z_i)
$$

よって、$z_i > r$の領域については
$$
\beta(z_i) = r \frac{G^{(N-1)}_1(r)}{G^{(N-1)}_1(z_i)} + \frac{1}{G^{(N-1)}_1(z_i)} \int_r^{z_i} w_ig^{(N-1)}_1(w_i) dw_i
$$

であり、$z_i \le r$の領域については入札しないという戦略が候補になる。これが本当に均衡であることの証明はここではおこなわない。

### 売り手の収入(3)

留保価格あり二位価格オークションの時と似た計算を行うと、その時と同じ結果になることが確認できる。
