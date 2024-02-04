# 確率変数についてのまとめ

「測度から確率へ」の4章の後半を読み進めている。今回はその内容である確率変数についてまとめていきたい。

## 確率変数の定義

一般的に確率変数は一般の可測写像に対して定義するようだが、この本では値として$+\infty,-\infty$を取りうるような関数の取り扱いを簡単にするために、可測関数に対しての定義を先に持ってきている。
> *確率変数*  
> 確率空間$(\Omega, \mathcal{B}, \bm{P})$上の可測関数$X$を確率変数と呼ぶ。また特に
- $X$が実関数の場合は実確率変数
- $X$が非負関数の場合は非負確率変数

と呼ぶ。

このように確率変数を定義することで、測度関係の話題が出てくると必ず出てくる次の言葉の意味がわかるようになる。
> *ほとんど確実に成り立つ*  
> 確率変数$X$が何かしらの条件$L$を満たす確率が$1$である
$$
\bm{P}(\{\omega \in \Omega : L(X(\Omega))\})
$$

である場合、その条件$L$はほとんど確実に成り立つといい、
$$
L, a.e.
$$

などと書く。



## 慨収束

この本ではここで、確率変数列の収束に関する定義の一つである慨収束を紹介している。これ以降ですぐにこの定義を使って何かするわけではなさそうだが、測度関係の話が出てくると良く出てくることではあるので、ちょうど良いからここで紹介するという感じだろうか。
> *慨収束*  
> 実確率変数列$\{X_n\}$がある実確率変数$X$に慨収束するとは、ほとんど至る所で$\{X_n\}$が$X$に収束すること、すなわち
$$
X = \lim_{n \rightarrow \infty} X_n, a.e.
$$

を満たすことである。

この定義を使って収束判定をする際には、まず各標本$\omega \in \Omega$それぞれに対して実数列$\{X_n(\omega)\}$が$X(\omega)$に収束するかを検査していって、その次に実際に収束すると判定された標本の集合
$$
\{\omega \in \Omega : \lim_{n \rightarrow \infty} X_n(\omega) = X(\omega) \}
$$

の確率測度が$1$であるかを判断するという流れになる。

実数列に対して収束性を判断する際、その収束先がわからない場合にはコーシー列を使って判断する方法もあった。それに対応するのが慨収束の次の性質である。
> *慨収束の判定方法1*  
> 実確率変数$\{X_n\}$が慨収束するための必要十分条件は、任意の$\epsilon > 0$に対して
$$
\lim_{n \rightarrow \infty} \bm{P}(\sup_{k, l \ge n} |X_k - X_l| > \epsilon) = 0
$$

が成り立つことである。

慨収束の定義はほとんど至る所で$\{X_n\}$がコーシー列となることと言い換えることができる。要するに、確率変数列$\{X_n\}$が慨収束するということは、任意の$\epsilon > 0$に対して
$$
1 = \bm{P}(\{\omega \in \Omega : \exists n, \forall k, l \ge n, |X_k(\omega) - X_l(\omega)| \le \epsilon\})
$$

となることと等しい。同じことだが、
$$
\begin{aligned}
0 &= \bm{P}(\{\omega \in \Omega : \forall n, \exists k, l \ge n, |X_k(\omega) - X_l(\omega)| > \epsilon\}) \\
&= \bm{P}(\bigcap_{n=1}^{\infty} \{\omega \in \Omega : \exists k, l \ge n, |X_k(\omega) - X_l(\omega)| > \epsilon\}) \\
&= \bm{P}(\bigcap_{n=1}^{\infty} \{\omega \in \Omega : \sup_{k,l \ge n} |X_k(\omega) - X_l(\omega)| > \epsilon\}) \\
&= \lim_{n \rightarrow \infty} \bm{P}(\sup_{k,l \ge n}|X_k(\omega) - X_l(\omega)| > \epsilon)
\end{aligned}
$$

となり、題意が成り立つ。

他にも、もっと簡単な収束判定方法もあることが紹介されている。
> *慨収束の判定方法2*  
> 実確率変数列$\{X_n\}$と実確率変数$X$を考える。任意の$\epsilon > 0$に対して
$$
\sum_{k=1}^{\infty} \bm{P}(|X_n - X| > \epsilon) < \infty
$$

の時、$\{X_n\}$は$X$に慨収束する。

ボレル-カンテリの定理を使えば
$$
\begin{aligned}
0 &= \bm{P}(\limsup_{n \rightarrow \infty} \{ \omega \in \Omega : |X_n(\omega) - X(\omega)| > \epsilon \} ) \\
&= \bm{P}(\bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} \{ \omega \in \Omega : |X_k(\omega) - X(\omega)| > \epsilon \} )
\end{aligned}
$$

であることがわかる。逆に言えば
$$
\begin{aligned}
1 &= \bm{P}(\bigcup_{n=1}^{\infty} \bigcap_{k=n}^{\infty} \{ \omega \in \Omega : |X_k(\omega) - X(\omega)| > \epsilon \} ) \\
&= \bm{P}(\{ \omega \in \Omega : \forall n \in \mathbb{N}, \exists k \ge n, |X_k(\omega) - X(\omega)| > \epsilon \} )
\end{aligned}
$$

これが任意の$\epsilon>0$について成り立つということは、ほとんど至る所の標本$\omega \in \Omega$で実数列$\{X_k(\omega)\}$が$X(\omega)$に収束していること、要するに慨収束していることを指す。


## 確率収束

慨収束とは別の収束の定義である確率収束と呼ばれる定義も紹介されている。こちらも比較的見聞きしたこのある言葉ではある。
> *確率収束*  
> 実確率変数列$\{X_n\}$が実確率変数$X$に確率収束するとは、任意の$\epsilon$に対して
$$
\lim_{n \rightarrow \infty} \bm{P}(|X_n - X| > \epsilon) = 0
$$

となることをいう。これをこの本では
$$
X = (\bm{P}) \lim_{n \rightarrow \infty} X_n
$$

と書くことにしている様子。

wikpediaを見ると確率収束の書き方として
$$
X = \plim_{n \rightarrow \infty} X_n
$$

という書き方がされているものがあった。

確率収束は慨収束よりも弱い概念である。
> *慨収束するなら確率収束もする*  
> 実確率変数列$\{X_n\}$が実確率変数$X$に慨収束するならば、確率収束もする。

適当に式変形すると
$$
\begin{aligned}
\lim_{n \rightarrow \infty} \bm{P}(|X_n - X| > \epsilon) &= \limsup_{n \rightarrow \infty} \bm{P}(|X_n - X| > \epsilon) \\
&\le \bm{P}( \limsup_{n \rightarrow \infty}\{ \omega \in \Omega : |X_n(\omega) - X(\omega)| > \epsilon \}) \\
&= \bm{P}(\{ \omega \in \Omega : \forall n \in \mathbb{N}, \exists k \ge n, |X_n(\omega) - X(\omega)| > \epsilon \})
\end{aligned}
$$

となるが、慨収束するならば任意の$\epsilon > 0$に対して
$$
\begin{aligned}
1 &= \bm{P}(\{ \omega \in \Omega : \exists n \in \mathbb{N}, \forall k \ge n, |X_n(\omega) - X(\omega)| \le \epsilon \}) \\
\iff 0 &= \bm{P}(\{ \omega \in \Omega : \forall n \in \mathbb{N}, \exists k \ge n, |X_n(\omega) - X(\omega)| > \epsilon \})
\end{aligned}
$$

であるから、
$$
\lim_{n \rightarrow \infty} \bm{P}(|X_n - X| > \epsilon) = 0
$$

となり、これは確率収束を表す。

ただし、それほど弱い概念というわけでもない。
> *確率収束するなら慨収束する部分列が存在する*  
> 実確率変数列$\{X_n\}$が実確率変数$X$に確率収束するなら、慨収束する部分列が存在する

実確率変数列$\{X_n\}$が実確率変数$X$に確率収束するなら、任意の$k \in \mathbb{N}$に対して、
$$
\bm{P}(|X_{n_k} - X| > \frac{1}{2^k}) < \frac{1}{2^k}
$$

となるような自然数列$n_1 \le n_2 \le \cdots$が取れる。この両辺の輪を取ると
$$
\sum_{k=1}^{\infty} \bm{P}(|X_{n_k} - X| > \frac{1}{2^k}) < \infty
$$

となるが、先ほどこの条件を満たすなら$\{X_{n_k}\}$が$X$に慨収束することを示したばかり。


## その他

この本では、他に確率収束するための必要十分条件として、確率収束に対するコーシー列みたいなものを証明していたが、手間がかかりそうだったので割愛している。基本は実数におけるコーシー列と収束性の関係に少し手を加えたものみたいな感じになっている様子。後できになるようだったら証明してみる。
