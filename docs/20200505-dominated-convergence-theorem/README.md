# 優収束定理

「測度から確率へ」の第5章を読み進めている。今回はそこで紹介されている優収束定理を示していきたい。

## 事前準備

優収束定理を示す前にそれよりも簡単な次の定理を示したい。
> *単調収束定理*  
> 単調増加する非負確率変数列$\{X_n\}$に対して
$$
\lim_{n \rightarrow \infty} \bm{E}[X_n] = \bm{E}[\lim_{n \rightarrow \infty} X_n]
$$

単調増加するので、$X = \lim_{n \rightarrow \infty} X_n$とすると、任意の$n \in \mathbb{N}$に対して
$$
X_n \le X \Rightarrow \bm{E}[X_n] \le \bm{E}[X]
$$

よって
$$
\lim_{n \rightarrow \infty} \bm{E}[X_n] \le \bm{E}[X]
$$

一方で、一般の非負確率変数に対する平均値の定義から、任意の$\epsilon > 0$に対して、ある非負単関数$Y$があって
$$
\bm{E}[X] - \epsilon < \bm{E}[Y]
$$

を満たす。ここで
$$
\Gamma_n = \{ \omega \in \Omega : X_n(\omega) > Y(\omega) - \epsilon\}
$$

とすると、
$$
\Gamma_1 \subset \Gamma_2 \subset \cdots, \Omega = \bigcup_{n=1}^{\infty} \Gamma_n
$$

であり、かつ
$$
YI_{\Gamma_n} < (X_n + \epsilon)I_{\Gamma_n} \le X_n + \epsilon
$$

となるので、
$$
\bm{E}[YI_{\Gamma_n}] < \bm{E}[X_n] + \epsilon
$$

$n$を無限に飛ばせば
$$
\bm{E}[Y] < \lim_{n \rightarrow \infty} \bm{E}[X_n] + \epsilon
$$

$Y$をどのようにして取ったかを思い出せば、任意の$\epsilon$に対して
$$
\bm{E}[X] - \epsilon < \bm{E}[Y] < \lim_{n \rightarrow \infty} \bm{E}[X_n] + \epsilon
$$

よって、$\lim_n \bm{E}[X_n] \le \bm{E}[X]$と合わせれば
$$
\lim_{n \rightarrow \infty} \bm{E}[X_n] = \bm{E}[X] = \bm{E}[\lim_{n \rightarrow \infty} X_n]
$$


この定理から導かれることとして次の補題がある。
> *Fatouの補題*  
> 非負確率変数列$\{X_n\}$に対して
$$
\bm{E}[\liminf_{n \rightarrow \infty} X_n] \le \liminf_{n \rightarrow \infty} \bm{E}[X_n]
$$

$\inf_{k \ge n} X_k$を考えれば、それは単調増加なので単調収束定理より
$$
\bm{E}[\liminf_{n \rightarrow \infty} X_n] = \lim_{n \rightarrow \infty} \bm{E}[\inf_{k \ge n} X_k]
$$

任意の$n \in \mathbb{N}$に対して
$$
\bm{E}[\inf_{k \ge n} X_k] \le \bm{E}[X_n]
$$

なので、
$$
\bm{E}[\inf_{k \ge n} X_k] \le \liminf_{n \rightarrow \infty} \bm{E}[X_n]
$$

よって
$$
\bm{E}[\liminf_{n \rightarrow \infty} X_n] = \lim_{n \rightarrow \infty} \bm{E}[\inf_{k \ge n} X_k] \le \liminf_{n \rightarrow \infty} \bm{E}[X_n]
$$



## 証明
ではまず定理を述べておく。
> *優収束定理*  
> 慨収束する確率変数列$\{X_n\}$に対して、
$$
\sup_{n \in \mathbb{N}} |X_n| \le S, a.e.
$$

となるような平均可能な非負確率変数$S$が存在する時、
$$
X = \lim_{n \rightarrow \infty} X_n, a.e.
$$

も平均可能である上に
$$
\lim_{n \rightarrow \infty} \bm{E}[X_n] = \bm{E}[\lim_{n \rightarrow \infty} X_n]
$$

導くための条件全てに「ほとんど至る所」という制限がついてはいるが、平均値を議論する限り基本は無視して置いていい。
$S$の性質から、$S+X_n$や$S-X_n$は非負確率変数である。これらに対してFatouの補題を適用すると
$$
\begin{aligned}
\bm{E}[S] + \bm{E}[\liminf_n X_n] &\le \bm{E}[S] + \liminf_n \bm{E}[X_n] \\
\bm{E}[S] - \bm{E}[\limsup_n X_n] &\le \bm{E}[S] - \limsup_n \bm{E}[X_n] \\
\end{aligned}
$$

合わせれば
$$
\limsup_n \bm{E}[X_n] \le \bm{E}[\limsup_n X_n] = \bm{E}[\liminf_n X_n] \le \liminf_n \bm{E}[X_n]
$$

よって
$$
\lim_{n \rightarrow \infty} \bm{E}[X_n] = \bm{E}[\lim_{n \rightarrow \infty} X_n]
$$
