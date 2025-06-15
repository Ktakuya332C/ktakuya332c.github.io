# ガンベル分布の性質

離散選択モデルがらみでガンベル分布の色々な性質を自然に使っている論文をよくみるので、一度ここでまとめておこうかと思う。まずはガンベル分布の定義から。

> *定義: ガンベル分布の確率密度*  
> ガンベル分布とは二つのパラメータ$\mu, \beta > 0$を持つ確率分布であり、その確率密度$f(x; \mu, \beta)$は

$$
f(x; \mu, \beta) = \frac{1}{\beta} \exp(- z - e^{-z})
$$

である。

適当な確率分布を出されてまず気になるのはその平均値だろう。ガンベル分布の平均値は妙な定数を持った形になる。

> *ガンベル分布の平均値*  
> パラメータ$\mu, \beta>0 \in \mathbb{R}$を持つガンベル分布

$$
\begin{aligned}
f(x; \mu, \beta) &= \frac{1}{\beta} \exp(- (z + e^{-z} )) \\
z &= \frac{x - \mu}{\beta}
\end{aligned}
$$

に従う確率変数$x$の平均値は

$$
E[x] = \mu + \beta \gamma
$$

である。ただしここで$\gamma$はオイラー定数である。

以下で証明する。

$$
\begin{aligned} E[x] &= \int^{\infty}_{-\infty} x f(x; \mu, \beta) dx \\
&= \int^{\infty}_{-\infty} (\beta z + \mu) f(z) \beta dz \\
&= \mu + \beta \int^{\infty}_{-\infty} z \exp(-z - e^{-z}) dz
\end{aligned}
$$

となるが、二つ目の項の$\beta$以外の部分は定数でありこれが一般的にオイラー定数と呼ばれるものとなる。オイラー定数の定義は様々存在するためここではその値がいずれかの定義でなされたオイラー定数に一致することは証明しない。その点を証明したい場合には[このStackExchange](https://math.stackexchange.com/questions/1838415/deriving-the-mean-of-the-gumbel-distribution)などを参考にすると良い。

あと使いそうなのは累積分布なので、とりあえず結果だけ転載しておく。

> *ガンベル分布の累積分布*  
> パラメータ$\mu, \beta>0 \in \mathbb{R}$を持つガンベル分布の累積分布は

$$
F(x; \mu, \beta) = \exp(- e^{-(x-\mu)/\beta})
$$

## よく使われるガンベル分布の性質

離散選択モデルを使用したモデルにおいてよく使われる性質として次のようなものがあるので一応示しておこうかと思う。

> *ガンベル分布と最大値の期待値*  
> $N \in \mathbb{N}$個の実数$\delta_1, \delta_2, \cdots, \delta_N$と同じ数のランダム変数$\epsilon_1, \epsilon_2, \cdots, \epsilon_N$があるとする。このときランダム変数がそれぞれ独立なガンベル分布にしたがっていれば

$$
E[\max_i (\delta_i + \epsilon_i)] = \beta \log \sum_i e^{\delta_i / \beta} + \beta \gamma + \mu
$$

が成立する。ただしここで$\gamma$はオイラーの定数である。

以下で証明する。確率変数$X$を次のように定義する。

$$
X = \max_i (\delta_i + \epsilon_i)
$$

このとき、$X$がある値$x$よりも低い値をとるためには、全ての$\delta_i + \epsilon_i$が$x$よりも低い値を取らなければならないため、

$$
P(X \le x) = \prod_i P(\delta_i + \epsilon_i \le x)
$$

が成立する。よって

$$
\begin{aligned} \log P(X \le x) &= \sum_i \log P(\delta_i + \epsilon_i \le x) \\ &= \sum_i \log P(\epsilon_i \le x - \delta_i) \\ &= \sum_i \log F(x - \delta_i; \mu, \beta) \\ &= - \sum_i e^{-(x - \delta_i - \mu) / \beta} \\ &= - e^{-(x-\mu)/\beta} \sum_i e^{\delta_i / \beta} \\ &=- \exp(- \frac{x -\mu}{\beta}) \exp( \log \sum_i e^{\delta_i / \beta} ) \\ &= - \exp(- \frac{1}{\beta} (x - \mu - \beta\log \sum_i e^{\delta_i / \beta})) \end{aligned}
$$

となる。この式の形をよく見れば、この式はガンベル分布の累積分布になっていることがわかる。

$$
P(X \le x) = F(X; \mu + \beta \log \sum_i e^{\delta_i / \beta}, \beta)
$$

よって$X = \max_i (\delta_i + \epsilon_i)$の平均値は

$$
E[\max_i (\delta_i + \epsilon_i)] = \beta \log \sum_i e^{\delta_i / \beta} + \beta \gamma + \mu
$$

となる。ただしここで$\gamma$はオイラー定数である。

## 参考文献

- [StackExchange: Expectation of the Maximum of iid Gumbel Variables](https://stats.stackexchange.com/questions/192424/expectation-of-the-maximum-of-iid-gumbel-variables)
