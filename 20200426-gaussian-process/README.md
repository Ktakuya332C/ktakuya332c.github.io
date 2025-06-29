# ガウス過程の簡単な例

確率微分方程式らへんの話を今まで雰囲気でやっていたので、細かいところまで議論できるように準備しておくかと最近まとめ始めているが、ウィーナー過程だのガウス過程だのそこら辺をしっかりと押さえて議論してこなかったので、色々とまとめることが多そう。

とりあえず今回の記事では、ガウス過程についておさらいすることにして、本当は連続性の証明とかいきなりできるといいなと思ったのだがそれもある程度慣れてきたらのほうが良さそうだったので、とりあえず一つ例を作ってお茶を濁すことにした。

## ガウス過程の定義

ガウス過程の定義自体に測度論的な話が大量に必要なのかなと勝手に想像していたが、そういうわけでもなく比較的簡単に定義できる様子。

> *ガウス過程*  
> ガウス過程とは、添え字集合$T$で特徴付けられている確率変数の集合$\{X_t\}_{t \in T}$であって、任意の有限個の添え字$t_1, t_2, \cdots, t_k$に対応する確率変数
$$
(X_{t_1}, X_{t_2}, \cdots, X_{t_k})
$$

の同時分布が多変量正規分布に従うものを指す。

基本的には添え字集合を$\mathbb{R}$などととることが多いのだと思うが、定義上では特にそこは指定されていない様子。

## ガウス過程の例

wikipediaに書かれていた例として、
$$
X_t = \cos(t) \xi_1 + \sin(t) \xi_2
$$

で、$\xi_1$と$\xi_2$が標準正規分布に従うとき
$$
\xi_1, \xi_2 \sim \mathcal{N}(0, 1)
$$

$\{X_t\}_{t \in \mathbb{R}}$がガウス過程になると書かれていたので、それを示してみようと思う。

ガウス過程かどうかを判断するためには、有限個の時刻$t_1, t_2, \cdots, t_k \in \mathbb{R}$をとって、それらの時刻における確率変数の集合
$$
(X_{t_1}, X_{t_2}, \cdots, X_{t_k})
$$

の同時分布が多変量正規分布になっているかどうかを調べれば良い。これらの変数の同時分布は、一変数の標準正規分布を$p_\mathcal{N}$と表して、
$$
p(\{X_{t_i}\}_{i=1}^k) = \int d\xi_1 \int d\xi_2 p_\mathcal{N}(\xi_1) p_\mathcal{N}(\xi_2) \prod_{i=1}^k \delta(X_{t_i} - \cos(t_i) \xi_1 - \sin(t_i) \xi_2)
$$

と表せる。直接この分布の性質を探っていくのは難しそうなので、この分布の積率母関数を計算していくことにすると
$$
\begin{aligned}
&\quad E[\exp(\sum_{i=1}^k s_i X_{t_i})] \\
&= \int \prod_{i=1}^k dX_{t_i} p(\{X_{t_i}\}_{i=1}^k) \exp(\sum_{i=1}^k s_i X_{t_i}) \\
&= \int d\xi_1 \int d\xi_2 p_\mathcal{N}(\xi_1) p_\mathcal{N}(\xi_2) \exp(\sum_{i=1}^k s_i (\cos(t_i) \xi_1 + \sin(t_i) \xi_2)) \\
&= \int d\xi_1 p_\mathcal{N}(\xi_1) \exp(\xi_1 \sum_{i=1}^k s_i \cos(t_i)) \int d\xi_2 p_\mathcal{N}(\xi_2) \exp(\xi_2 \sum_{i=1}^k s_i \sin(t_i)) \\
&= \exp(\frac{1}{2}(\sum_{i=1}^k s_i \cos(t_i))^2) \exp(\frac{1}{2}(\sum_{i=1}^k s_i \sin(t_i))^2) \\
&= \exp(\frac{1}{2} \sum_{i=1}^k \sum_{j=1}^k s_i s_j (\cos(t_i) \cos(t_j) + \sin(t_i) \sin(t_j))) \\
&= \exp(\frac{1}{2} \sum_{i=1}^k \sum_{j=1}^k s_i s_j \cos(t_i - t_j))
\end{aligned}
$$

となって、多変量正規分布の積率母関数となるので、$\{X_t\}_{t \in \mathbb{R}}$はガウス過程と言える。久々に三角関数の合成の式を使った気がする。
