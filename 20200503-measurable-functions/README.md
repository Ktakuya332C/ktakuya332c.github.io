# 可測関数の定義とその性質

「測度から確率へ」の第4章を読んでいる。内容としては大きく次の二つに分かれている。

1. 可測関数の定義とその性質の紹介
1. 確率変数の定義とその性質の紹介

今回はその前半、可測関数の定義とその性質について、をまとめていこうと思う。

## 可測関数の定義と性質

> *可測関数*  
> 可測空間$(\Omega, \mathcal{B})$上の実数または$+\infty,-\infty$の値をとる関数$X$が、任意の実数$\alpha$に対して
$$
\{\omega \in \Omega : X(\omega) > \alpha\}
$$

を満たすとき、関数$X$を可測関数と呼ぶ。

可測関数は値域に$+\infty,-\infty$を含んでいることに注意する。

この先、この可測関数に対する積分を定めたいのだが、基本的に積分はリーマン積分の時と同じく何かしらその関数に近い、積分の値っぽいものが定め易そうな関数を持ってきて、それを徐々に本当の関数に近づけていくという方法をとる。この時必要になるのが、まず定義関数というもの。
> *定義関数*  
> 集合$\Omega$のある部分集合$A$に紐づく関数
$$
I_A(\omega) = \begin{cases}
  1 & \omega \in \Omega  \\
  0 & \omega \not \in \Omega
\end{cases}
$$

を定義関数と呼ぶ。

そして、その定義関数を有限個組み合わせて作る単関数というものである。
> *単関数*  
> 可測空間$(\Omega, \mathcal{B})$上の実数値関数$X$に対して、互いに共通部分を持たない可測集合族
$$
A_1, A_2, \cdots, A_n \in \mathcal{B}
$$

と、実数$a_1, a_2, \cdots, a_n \in \mathbb{R}$が存在して
$$
X(\omega) = \sum_{k=1}^n a_k I_{A_k}(\omega)
$$

となるならば、$X$は単関数であるという。

定義からしてカクカクしていて積分の値っぽいものが定め易そうであることがわかると思う。

この本ではここから一気に積分の定義にいくわけではなく、その一歩前の段階として可測関数の積分をしたいと思った時に、それに徐々に近くような単関数を作れるのかどうかという点を考えていくことにしている様子。
> *可測関数列の性質*  
> 可測関数列$\{X_n\}_{n=1}^{\infty}$が与えられたとき、
$$
\sup_n X_n, \inf_n X_n, \limsup_n X_n, \liminf_n X_n
$$

はどれも可測関数である。

まず$\sup$に対しての証明を行う。任意の実数$\alpha$に対して
$$
\sup_n X_n(w) > \alpha \iff \exists n, X_n(w) > \alpha
$$

であるから、
$$
\{\omega \in \Omega : \sup_n X_n(w) > \alpha\} = \bigcup_n \{\omega \in \Omega : X_n(w) > \alpha\} \in \mathcal{B}
$$

よって、$\sup_n X_n$は可測関数である。

つぎに$\inf$については、単に同じ議論をしてしまうと
$$
\inf_n X_n(\omega) \ge \alpha \iff \forall n, X_n(\omega) > \alpha
$$

となってしまうので、少し工夫して
$$
\exists m, \inf_n X_n(\omega) > \alpha + \frac{1}{m} \iff \exists m, \forall n, X_n(\omega) > \alpha + \frac{1}{m}
$$

を証明することにする。必要性は明らかで、十分性は$m$を適切に取った後に
$$
\forall n, X_n(\omega) > \alpha + \frac{1}{m} \Rightarrow \inf_n X_n(\omega) \ge \alpha + \frac{1}{m} > \alpha + \frac{1}{m+1}
$$

として示せる。この結果を使えば
$$
\begin{aligned}
\{\omega \in \Omega : \inf_n X_n(w) > \alpha \} &= \bigcup_m \{\omega \in \Omega : \inf_n X_n(w) > \alpha + \frac{1}{m} \} \\
&= \bigcup_m \bigcap_n \{\omega \in \Omega : X_n(w) > \alpha + \frac{1}{m} \} \in \mathcal{B}
\end{aligned}
$$

となり、$\inf_n X_n$も可測関数であることがわかる。

$\limsup$と$\liminf$は、
$$
\limsup_n X_n = \inf_n \sup_{k \ge n} X_k, \liminf_n X_n = \sup_n \inf_{k \ge n} X_k,
$$

であり、$\sup$と$\inf$の組み合わせなので、可測関数である。

> *可測関数列の極限*  
> 可測関数列$\{X_n\}_{n=1}^{\infty}$が与えられたときに
$$
\limsup_n X_n = \liminf_n X_n
$$

となれば、その値を
$$
\lim_n X_n
$$

と表すこととする。

ここまで準備すれば、可測関数に徐々に近づくような単関数を作れるかという点についてある程度の回答を得ることができる。
> *非負可測関数と単関数の関係*  
> 可測空間$(\Omega, \mathcal{B})$上の非負関数$X$が可測となる必要十分条件は、ある非負単関数列$\{X_n\}$で
$$
0 \le X_1 \le X_2 \le \cdots \le X
$$

を満たし、かつ
$$
\lim_n X_n = X
$$

となるようなものが存在することである。

十分性は、単関数が可測であり、可測関数の極限も可測になることから明らかである。必要性は、任意の非負可測関数$X$に対して
$$
\begin{aligned}
A_0^n &= \{\omega : X(\omega) > n\} \in \mathcal{B} \\
A_k^n &= \{\omega : \frac{k-1}{2^n} \le X(\omega) < \frac{k}{2^n} \} \in \mathcal{B} \\
X_n(\omega) &= \sum_{k=1}^{n2^n} \frac{k-1}{2^n} I_{A_k^n}(\omega) + I_{A_0^n}(\omega)
\end{aligned}
$$

とすれば、$\{X_n\}$が上記の条件を満たすことがわかる。

最後に一工夫すると、どんな可測関数に対してもそれに近づいていくような単関数列を作ることができることがわかる。
> *可測関数と単関数の関係*  
> 可測空間$(\Omega, \mathcal{B})$上の関数$X$が可測となる必要十分条件は、ある単関数列$\{X_n\}$で
$$
0 \le X_1 \le X_2 \le \cdots \le X
$$

を満たし、かつ
$$
\lim_n X_n = X
$$

となるようなものが存在することである。

十分性は先ほどと同じく明らか。必要性は、
$$
X^+(\omega) = \max(X(\omega), 0) \\
X^-(\omega) = - \min(X(\omega), 0)
$$

とすれば、それらに対して近似単関数列$X^+_n, X^-_n$が取れるが、
$$
X_n = X^+_n - X^-_n
$$

とすれば目的の単関数列が得られる。

## 可測関数と可測写像

可測関数は値域が実数と$+\infty,-\infty$の場合についての話だったが、可測関数とは別に可測写像と呼ばれる、値域が一般の可測空間の場合の話をすることもできる。
> *可測写像*  
> 可測空間$(\Omega, \mathcal{B})$から$(\Omega', \mathcal{B}')$への写像$T$が、任意の$\mathcal{B}'$-可測集合$A$に対して
$$
T^{-1}(A) \in \mathcal{B}
$$

となる時、写像$T$は可測写像であるという。

ここで注意するべきは、一般に可測関数は可測写像ではないということである。一番それっぽいのは実数と1次元ボレル集合体で作られる可測空間への関数
$$
T: (\Omega, \mathcal{B}) \rightarrow (\mathbb{R}, \bm{B}_1)
$$

だが、残念ながらこの関数の値域に$+\infty,-\infty$が含まれない。

ただし、可測関数は可測写像っぽい性質を満たしてはいる。
> *可測関数の逆像に関する性質*  
> 可測関数$X$について次が成り立つ。

1. $X^{-1}(+\infty) \in \mathcal{B}$
1. $X^{-1}(-\infty) \in \mathcal{B}$
1. 任意の1次元ボレル集合$B \in \bm{B}_1$に対して、$X^{-1}(B) \in \mathcal{B}$

一つ目は
$$
\{\omega \subset \Omega : X(\omega) = \infty\} = \bigcap_n \{\omega \subset \Omega : X(\omega) > n \} \in \mathcal{B}
$$

より明らか。二つ目も同様に
$$
\{\omega \subset \Omega : X(\omega) = - \infty\} = \bigcap_n \{\omega \subset \Omega : X(\omega) \le -n \} \in \mathcal{B}
$$

より明らか。三つ目は
$$
\mathcal{B}_0 \equiv \{B \subset \mathbb{R} : X^{-1}(B) \in \mathcal{B}\}
$$

とすると、任意の$-\infty < a \le b \le \infty$に対して
$$
X^{-1}((a, b]) = X^{-1}((a, \infty] - (b, \infty]) = X^{-1}((a, \infty]) - X^{-1}((b, \infty]) \in \mathcal{B}
$$

となるので、
$$
\bm{J}_1 \subset \mathcal{B}_0 \Rightarrow \bm{B}_1 \subset \mathcal{B}_0
$$

よって任意の$B \in \bm{B}_1$に対して$X^{-1}(B) \in \mathcal{B}_0$となる。

そして実関数に限ればそれらは同じ意味。
> *実関数における可測関数と可測写像*  
> 実関数に限れば、それが可測関数であることの必要十分条件は可測写像であることである。そしてそのような関数のことを実可測関数と呼ぶ。

## 実可測関数の性質

実可測関数は足し算したり掛け算したりしても相変わらず実可測関数である。そのことを示すためにまず次を示す。
> *可測空間から$d$次元ユークリッド空間への写像*  
> 可測空間$(\Omega, \mathcal{B})$から$(\mathbb{R}, \bm{B}_1)$への可測写像$X_1, X_2, \cdots, X_d$を組み合わせた写像
$$
\bm{X}: \omega \in \Omega \rightarrow (X_1(\omega), X_2(\omega), \cdots, X_d(\omega))
$$

は、$(\Omega, \mathcal{B})$から$(\mathbb{R}^d, \bm{B}_d)$への可測写像である。

次のような集合族を考える。
$$
\mathcal{B}_0 \equiv \{B \subset \mathbb{R}^d : \bm{X}^{-1}(B) \in \mathcal{B}\}
$$

任意の$\bm{J}_d$の元
$$
J = \prod_{j=1}^d (a_j, b_j], a_j, b_j \in \mathbb{R}
$$

に対して、その$\bm{X}$による逆像は
$$
\bigcap_{j=1}^d X^{-1}_j((a_j, b_j]) \in \mathcal{B}
$$

となるため、
$$
\bm{J}_d \subset \mathcal{B}_0 \Rightarrow \bm{B}_d \subset \mathcal{B}_0
$$

よって、任意の$B \in \bm{B}_d$に対して、$\bm{X}^{-1}(B) \in \mathcal{B}$。要するに$\bm{X}$は可測写像。

さらにこちらも示す。
> *$\mathbb{R}^d$から$\mathbb{R}$への連続写像*  
> 任意の$\mathbb{R}^d$から$\mathbb{R}$への連続写像$X$は可測写像である。

次のような集合族を考える。
$$
\mathcal{B}_0 \equiv \{ B \subset \mathbb{R} : X^{-1}(B) \in \bm{B}_d \}
$$

この時、$X$は連続であるから、任意の$\mathbb{R}$の開集合$O$の逆像も開集合なので
$$
\mathcal{O} \subset \mathcal{B}_0 \Rightarrow \bm{B}_1 \subset \mathcal{B}_0
$$

ここで、$\mathcal{O}$は$\mathbb{R}$の開集合族。よって、任意の1次元ボレル集合$B$に対して、その逆像は$d$次元ボレル集合。要するに$X$は可測写像。

これらを組み合わせれば、例えば以下などがわかる。
> *実可測関数の足し算掛け算*  
> 実可測関数$X,Y$に対して
$$
X+Y, XY
$$

なども実可測関数である。
