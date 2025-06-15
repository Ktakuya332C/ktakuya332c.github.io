# 多変量正規分布について

多変量正規分布をいじる機会があったのだが、あまりにもその取り扱い方法を忘れてしまっていたので一度復習しておこうと思う。

## 定義

まずは定義から。もっとも普通な、細かく言えば非退化な、正規分布だけを取り扱うことにする。

> *多変量正規分布*  
> 実$N$次元列ベクトル$\bm{x}$が、多変量正規分布$\mathcal{N}(\bm{\mu}, \bm{\Sigma})$に従うとは、その確率密度関数$p(\bm{x})$が
$$
p(\bm{x}) = \frac{1}{\sqrt{(2\pi)^N |\bm{\Sigma}|}} \exp(-\frac{1}{2}(\bm{x} - \bm{\mu})^T \bm{\Sigma}^{-1} (\bm{x} - \bm{\mu}))
$$

であることを指す。ただしここで、$\bm{\mu}$は、$\bm{x}$同様、$N$次元実ベクトルであり、$\bm{\Sigma}$は正定値行列である。

太文字をつかった行列表示は実際に紙に書いたときに太文字とそうでないもの字が見分けづらいので、自分は可能なら添字表記の方を使うのだが、今回は行列演算が多いと見ているので太文字の行列で書いたほうがわかりやすくなりそう。

## 積分して$1$になること

まずは当たり前だが積分したら合計が$1$になることを確かめたい。久しぶりに多変量正規分布の積分をやったが、とりあえず実直に計算していけば辿り着ける感じのものでもないので少し困った。変数の数が1個や2個の場合なら単純に計算をしていくだけでなんとかなるのだが、任意の$N$に対して同じ方法で計算しようと思うと大変なことになる。

鍵は$\bm{\Sigma}$を固有値分解すること。正定値行列なので、固有値は次元数分存在して、それらは全て正の値をとる。
$$
\lambda_1, \lambda_2, \cdots, \lambda_N > 0
$$

そして、これらを対角成分として持つ行列$\bm{\Lambda}$と、直行行列$\bm{V}$が存在して
$$
\bm{\Sigma} = \bm{V}^T \bm{\Lambda} \bm{V}
$$

と分解できることになる。ここまで書いてきて行列は太字で書くのだったか曖昧になり始めたが、ここら辺の定義を書く際に参考にしたWikipediaさんがそう書いているので、その慣習に倣って全部太文字にしていく。

固有値分解さえしてしまえば、あとは実直に計算していくだけなはず。長い長い計算の始まり。
$$
\begin{aligned}
\int d\bm{x} p(\bm{x}) &= \int d\bm{x} \frac{1}{\sqrt{(2\pi)^N |\bm{\Sigma}|}} \exp(-\frac{1}{2}(\bm{x} - \bm{\mu})^T \bm{\Sigma}^{-1} (\bm{x} - \bm{\mu})) \\
&= \frac{1}{\sqrt{(2\pi)^N |\bm{\Sigma}|}} \int d\bm{x}  \exp(-\frac{1}{2}\bm{x}^T \bm{\Sigma}^{-1} \bm{x}) \\
&= \frac{1}{\sqrt{(2\pi)^N |\bm{\Lambda}|}} \int d\bm{x}  \exp(-\frac{1}{2}\bm{x}^T \bm{V}^T \bm{\Lambda}^{-1} \bm{V} \bm{x}) \\
&= \frac{1}{\sqrt{(2\pi)^N |\bm{\Lambda}|}} \int d\bm{y}  \exp(-\frac{1}{2}\bm{y}^T \bm{\Lambda}^{-1} \bm{y}) \\
&= \prod_{i=1}^N \frac{1}{\sqrt{2\pi \lambda_i}} \int_{-\infty}^{\infty} dy_i \exp(-\frac{1}{2\lambda_i} y_i^2)
\end{aligned}
$$

ここまで計算して、ガウス積分の公式を忘れたのでwikipediaからとってくる。ガウス積分における色々な係数がどこに影響するかは以前から必ず忘れていて、毎回検索してしまうのだが、何かいい方法はないか。
$$
\int^{\infty}_{-\infty} dx \exp(-\xi x^2) = \sqrt{\frac{\pi}{\xi}}
$$

これをそのまま使えば
$$
\int_{-\infty}^{\infty} dy_i \exp(-\frac{1}{2\lambda_i} y_i^2) = \sqrt{2 \pi \lambda_i}
$$

なので、
$$
\int d\bm{x} p(\bm{x}) = 1
$$

となりそう。

## 積率母関数を求める

平均や分散なども出していきたいところだが、それぞれを別々に計算していくのは面倒なので、一度積率母関数を求めて、そこから計算していくことにする。特性関数と必ず混ざるのだが、特性関数はFourier変換のようなもので虚数が入っていて、積率母関数はLaplace変換のようなもので虚数が入っていない。

この計算もさっきと同じく$\bm{\Sigma}$の固有値分解をつかえば行けそうな雰囲気がする。
$$
\begin{aligned}
E[\exp(\bm{t}^T \bm{x})] &= \int d\bm{x} \frac{1}{\sqrt{(2\pi)^N |\bm{\Sigma}|}} \exp(\bm{t}^T \bm{x}-\frac{1}{2}(\bm{x} - \bm{\mu})^T \bm{\Sigma}^{-1} (\bm{x} - \bm{\mu})) \\
&= \frac{1}{\sqrt{(2\pi)^N |\bm{\Lambda}|}} \int d\bm{x} \exp(\bm{t}^T \bm{x}-\frac{1}{2}(\bm{x} - \bm{\mu})^T \bm{V}^T \bm{\Lambda}^{-1} \bm{V} (\bm{x} - \bm{\mu}))
\end{aligned}
$$

だが、次のような変数変換をして
$$
\begin{aligned}
\bm{y} &= \bm{V} (\bm{x} - \bm{\mu}) \\
\iff \bm{x} &= \bm{V}^T \bm{y} + \bm{\mu}
\end{aligned}
$$

整理すると
$$
\begin{aligned}
E[\exp(\bm{t}^T \bm{x})] &= \frac{1}{\sqrt{(2\pi)^N |\bm{\Lambda}|}} \int d\bm{y} \exp(\bm{t}^T \bm{V}^T \bm{y} + \bm{t}^T \bm{\mu} -\frac{1}{2}\bm{y}^T \bm{\Lambda}^{-1} \bm{y}) \\
&= \frac{\exp(\bm{t}^T \bm{\mu})}{\sqrt{(2\pi)^N |\bm{\Lambda}|}} \prod_{i=1}^N \int dy_i \exp(-\frac{1}{2\lambda_i} y_i^2 + y_i \sum_{j=1}^N V_{ij} t_j) \\
&= \frac{\exp(\bm{t}^T \bm{\mu})}{\sqrt{(2\pi)^N |\bm{\Lambda}|}} \prod_{i=1}^N \int dy_i \exp(-\frac{1}{2\lambda_i} (y_i - \lambda_i \sum_{j=1}^N V_{ij} t_j)^2 + \frac{\lambda_i}{2} (\sum_{j=1}^N V_{ij} t_j)^2) \\
&= \exp(\bm{t}^T \bm{\mu} + \sum_{i=1}^N \frac{\lambda_i}{2}(\sum_{j=1}^N V_{ij} t_j)^2) \\
&= \exp(\bm{t}^T \bm{\mu} + \frac{1}{2} \bm{t}^T \bm{\Sigma} \bm{t})
\end{aligned}
$$

となり、それっぽい式を得ることができた。

## 平均や共分散など

積分母関数から平均は簡単に求めることができる。
$$
\begin{aligned}
E[x_i] &= \left.\frac{\partial}{\partial t_i}\right|_{\bm{t}=\bm{0}} E[\exp(\bm{t}^T\bm{x})] \\
&= \mu_i
\end{aligned}
$$

より、
$$
E[\bm{x}] = \bm{\mu}
$$

となり期待通り。共分散も似たような感じで、
$$
\begin{aligned}
E[x_i x_j] &= \left.\frac{\partial^2}{\partial t_i \partial t_j}\right|_{\bm{t}=\bm{0}} E[\exp(\bm{t}^T\bm{x})] \\
&= \left.\frac{\partial}{\partial t_i}\right|_{\bm{t}=\bm{0}} \exp(\bm{t}^T \bm{\mu} + \frac{1}{2} \bm{t}^T \bm{\Sigma} \bm{t}) (\mu_j + \sum_{k=1}^N \Sigma_{jk} t_k) \\
&= \left[\exp(\bm{t}^T \bm{\mu} + \frac{1}{2} \bm{t}^T \bm{\Sigma} \bm{t}) ((\mu_j + \sum_{k=1}^N \Sigma_{jk} t_k) (\mu_i + \sum_{k=1}^N \Sigma_{ik} t_k) + \Sigma_{ij})\right]_{\bm{t}=\bm{0}} \\
&= \Sigma_{ij} + \mu_i \mu_j
\end{aligned}
$$

より、
$$
E[(x_i-\mu_i)(x_j-\mu_j)] = \Sigma_{ij}
$$

となって期待通り。和の記号と分散の$\Sigma$が近くに配置されてしまって少し式が見にくくなってしまったので、もしかすると別の記号を使っていたほうが見やすくなった感とも思った。ただし一変数の時の分散が$\sigma^2$などと表されているのと統一されてはいるので、どちらを取るかは微妙なところ。
