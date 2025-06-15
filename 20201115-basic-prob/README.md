# 確率微分方程式(1)

次の本を読み始めた。

- 谷口説男著、[確率微分方程式](https://www.kyoritsu-pub.co.jp/bookdetail/9784320112018)

今回はこの本の第一章をまとめていく。
第一章は確率論の基礎の復習を行う章になっている。この章で紹介されている内容については他の本などですでに学習済みであることが想定されているため、細かい定義の説明や定理の証明などは掲載されていない。この記事ではそれら紹介されている定義と定理を可能な限り簡潔にまとめていく。

## 基礎的な定義

確率論を構成するにあたって最低限必要な定義を列挙してく。

> *完全加法族*  
> 集合$\Omega$の部分集合族$\mathcal{F}$が完全加法族であるとは、次の3つの条件を満たすことを言う。

1. $\phi, \Omega \in \mathcal{F}$
1. $A \in \mathcal{F}$ならば$A^C \in \mathcal{F}$
1. 任意の$i \in \mathbb{N}$に対して$A_i \in \mathcal{F}$ならば$\bigcup_{i=1}^{\infty} A_i \in \mathcal{F}$

ただしここで$A^C$は$A$の補集合を表す。完全加法族の要素$A \in \mathcal{F}$を可測集合と呼び、組$(\Omega, \mathcal{F})$を可測空間と呼ぶ。

> *確率測度*  
> $(\Omega, \mathcal{F})$を可測空間とする。関数$\textbf{P}: \mathcal{F} \rightarrow [0, 1]$が次の2条件を満たすとき、$\textbf{P}$を確率測度と呼ぶ。

1. $\textbf{P}(\Omega) = 1$
1. $A_i \in \mathcal{F}$が互いに交わらない場合に、$\textbf{P}(\bigcup_{i=1}^{\infty}A_i) = \sum_{i=1}^{\infty} \textbf{P}(A_i)$が成り立つ

さらに、三つ組$(\Omega, \mathcal{F}, \textbf{P})$を確率空間と呼ぶ。

> *$E$-値確率変数*  
> 確率空間$(\Omega, \mathcal{F}, \textbf{P})$から可測空間$(E, \mathcal{E})$への関数$X: \Omega \rightarrow E$が$E$-値確率変数であるとは以下を満たすことを指す
$$
\forall A \in \mathcal{E} \quad X^{-1}(A) \in \mathcal{F}
$$

特に確率変数の値域が実数である場合に興味がある。

> *完全加法族の生成*  
> ある集合$\Omega$の部分集合族$\mathcal{A}$に対して、それを含む完全加法族の全体を$\Lambda(\mathcal{A})$と書く。このときこの中の最小の要素
$$
\sigma(\mathcal{A}) = \bigcap_{\mathcal{G} \in \Lambda(\mathcal{A})} \mathcal{G}
$$

を$\mathcal{A}$が生成する完全加法族と呼ぶ。

> *ボレル完全加法族*  
> 位相空間$\Omega$に対して、その開集合族$\mathcal{O}$が生成する完全加法族を$\mathcal{B}(\Omega)$と書き、ボレル完全加法族と呼ぶ。

> *確率変数*  
> 値域として可測空間$(\mathbb{R}, \mathcal{B}(\mathbb{R}))$をとる$\mathbb{R}$-値確率変数を、単に確率変数と呼ぶ。

確率変数に対しては期待値と呼ばれる実数を定義できる。

> *期待値*  
> 確率変数$X$の期待値$\textbf{E}[X]$を次の手順で定義する。
まず$a_i \in \mathbb{R}$と$A_i \in \mathcal{F}$によって定義される確率変数
$$
X = \sum_{i=1}^{n} a_i \textbf{1}_{A_i}
$$

の全体を$\mathcal{SF}$と定義し、各要素$X$に対してその期待値を以下のように定める。
$$
\textbf{E}[X] = \sum_{i=1}^{n} a_i \textbf{P}(A_i)
$$

次に、任意の非負確率変数$X$に対してその期待値を次のように定める
$$
\textbf{E}[X] = \sup \{\textbf{E}[Y] | Y \in \mathcal{SF}, 0 \le Y \le X\}
$$

最後に、任意の確率変数$X$に対して
$$
\begin{aligned}
X^{+}(\omega) &= \max \{X(\omega), 0 \} \\
X^{-}(\omega) &= \max \{X(-\omega), 0 \}
\end{aligned}
$$

という定義を使って、その期待値を次のように定める
$$
\textbf{E}[X] = \textbf{E}[X^{+}] - \textbf{E}[X^{-}]
$$

以上が確率論における基本的な概念であり、これらを組み合わせて様々な議論をしていくことになる。

## 基礎的な性質

ここまでで定義していた概念の性質を列挙していく。

### 確率測度の性質

> *単調性*  
> $A,B \in \mathcal{F}$に対して以下が成り立つ。
$$
A \subset B \Rightarrow \textbf{P}(A) \le \textbf{P}(B)
$$

さらに、可測集合列$A_i \in \mathcal{F}$に対して
$$
\begin{aligned}
A_i \subset A_{i+1} &\Rightarrow \textbf{P}(\bigcup_{i=1}^{\infty} A_i) = \lim_{i \rightarrow \infty} \textbf{P}(A_i)\\
A_i \supset A_{i+1} &\Rightarrow \textbf{P}(\bigcap_{i=1}^{\infty} A_i) = \lim_{i \rightarrow \infty} \textbf{P}(A_i)
\end{aligned}
$$

> *独立性*  
> $A_1,A_2,\cdots,A_n \in \mathcal{F}$が独立であるとは、任意の$m \le n$と$1 \le i_1 < \cdots < i_m \le n$に対して次が成り立つことを指す。
$$
\textbf{P}(\bigcap_{j=1}^{m} A_{i_j}) = \prod_{j=1}^{m} \textbf{P}(A_{i_j})
$$

さらに、完全加法族$\mathcal{G}_1, \cdots, \mathcal{G}_n \subset \mathcal{F}$が独立であるとは、任意の$A_1 \in \mathcal{F}_1, \cdots, A_n \in \mathcal{F_n}$が独立であることを指す。

> *ボレルカンテリの補題*  
> $A_i \in \mathcal{F}$に対して、
$$
\sum_{i=1}^{\infty} \textbf{P}(A_i) < \infty \Rightarrow \textbf{P}(A) = 0
$$

さらに、もし$A_1, \cdots, A_n$が独立ならば
$$
\sum_{i=1}^{\infty} \textbf{P}(A_i) = \infty \Rightarrow \textbf{P}(A) = 1
$$

### $E$-値確率変数の性質

$E$-値確率変数の議論には確率分布を使用した方がわかりやすいことが多い。
> *確率分布*  
> $E$-値確率変数に対して、$\textbf{Q}: \mathcal{E} \rightarrow [0,1]$を
$$
\textbf{Q}(A) = \textbf{P}(X^{-1}(A))
$$

と定義すると、$\textbf{Q}$は$(E,\mathcal{E})$上の確率測度であり、これを$X$の確率分布と呼ぶ。

また、$E$-値確率変数についても独立性の議論をすることができる。
> *独立性*  
> $E$-値確率変数$X$に対して、$X$の生成する完全加法族として
$$
\mathcal{F}^X = \{X^{-1}(A) | A \in \mathcal{E}\}
$$

と定義する。確率変数$X_1,\cdots,X_n$が独立であるとは、対応する完全加法族$\mathcal{F}^{X_1},\cdots,\mathcal{F}^{X_n}$が独立であることを指す。

さらに、値域に距離$d$を入れた場合、$E$-値確率変数列の収束の議論をすることができる。
> *$E$-値確率変数列の収束性*  
> 可測空間$(E,\mathcal{E})$に対して距離$d$が定義されているとする。$E$-値確率変数変数列$X_n$について考える。
$X_n$が$X$に概収束するとは次を満たすことを指す。
$$
\textbf{P}(\lim_{n \rightarrow \infty} d(X_n, X) = 0) = 1
$$

$X_n$が$X$に確率収束するとは、任意の$\epsilon > 0$に対して次を満たすことを言う。
$$
\lim_{n \rightarrow \infty} \textbf{P}(d(X_n, X) > \epsilon) = 0
$$

ここで概収束の方が強い概念である。
> *概収束と確率収束*  
> 次の二つが成り立つ。

1. $X_n$が$X$に概収束すれば、確率収束する。
1. $X_n$が$X$に確率収束すれば、概収束する部分列$\{X_{n_k}\}_{k=1}^{\infty}$が存在する。

### 期待値の性質

全ての確率変数に対して期待値が定義できるわけではない。
> *可積分*  
> 確率変数$X$に対して$\textbf{E}[X] < \infty$となるとき、$X$は可積分であるという。
さらに、$p > 0$に対して$|X|^p$が可積分であるとき、$X$は$p$-乗可積分であるといい、これらの全体を$L^p(\textbf{P})$と表す。$X \in L^p(\textbf{P})$に対して
$$
\|X\|_p = (\textbf{E}[|X|^p])^{1/p}
$$

とおく。

期待値についても収束の議論をすることができる。
> *収束定理*  
> (単調収束定理) $X_n \le X_{n+1}, \textbf{P}-a.s.$ならば次が成り立つ。
$$
\lim_{n \rightarrow \infty} \textbf{E}[X_n] = \textbf{E}[\lim_{n \rightarrow \infty} X_n]
$$

(Fatouの補題) $X_n \ge 0, \textbf{P}-a.s.$ならば次が成り立つ。
$$
\textbf{E}[\liminf_{n \rightarrow \infty} X_n] \le \liminf_{n \rightarrow \infty} \textbf{E}[X_n]
$$

(優収束定理) $|X_n| \le Y, \textbf{P}-a.s.$となる確率変数$Y \in L^p(\textbf{P})$が存在し、$\lim_{n \rightarrow \infty} X_n$が至る所存在する場合以下が成り立つ。
$$
\lim_{n \rightarrow \infty} \textbf{E}[X_n] = \textbf{E}[\lim_{n \rightarrow \infty} X_n]
$$

可積分の概念を確率変数列に拡大することもできる。
> *一様可積分*  
> 確率変数列$X_n$が以下を満たすとき、一様可積分であるという。
$$
\lim_{\lambda \rightarrow \infty} \sup_{n \in \mathbb{N}} \textbf{E}[|X_n| ; |X_n| \ge \lambda] = 0
$$

ただしここで$\textbf{E}[X ; A] = \textbf{E}[X\textbf{1}_A]$という記法を使っている。

この場合はより強い収束定理が成り立つ。
> *収束定理*  
> 確率変数列$X_n$が一様可積分であり
$$
\lim_{n \rightarrow \infty} X_n = X, \textbf{P}-a.s.
$$

である場合、$X \in L^p(\textbf{P})$であり、任意の$A \in \mathcal{F}$に対して以下が成り立つ。
$$
\lim_{n \rightarrow \infty} \textbf{E}[X_n ; A] = \textbf{E}[X; A]
$$

ついで、独立性についてもよく知られた次の性質が成り立つ。
> *独立性*  
> 確率変数$X,Y$が独立でともに可積分ならば、$XY$も可積分で、$\textbf{E}[XY] = \textbf{E}[X] \textbf{E}[Y]$

## 備考

- 条件付き期待値をまとめる前に力尽きました。
- フビニの定理とトネリの定理を別でまとめたい。
- この本では拡張実数を確率変数の値域に入れていないようだが、それによる問題は何か出てくるかどうか。
