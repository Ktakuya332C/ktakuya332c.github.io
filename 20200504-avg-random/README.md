# 確率変数の平均値

「測度から確率へ」の第5章を読み進めている。5章の内容は

- 確率変数に対する平均値の定義とその性質
- 平均値と極限操作の関係
- 平均値に関する幾つかの不等式
- $L^p$-収束

となっている。ここでは、確率変数に対する平均値の定義とその性質についてまとめていこうと思う。

## 非負単関数に対する定義

まずは一番簡単なものに対してから定義を始めていく。
> *定義1*  
> 確率空間$(\Omega, \mathcal{B}, \bm{P})$上の確率変数$X$が、$\Omega$を分割する互いに交わらない可測集合族$\{A_k\}_{k=1}^n$をもとにした非負単関数
$$
X(\omega) = \sum_{k=1}^n a_k I_{A_k}(\omega), a_k \ge 0
$$

として表せる時、その平均値を
$$
\bm{E}[X] = \sum_{k=1}^n a_k \bm{P}(A_k)
$$

として定義する。

単関数の表現は一意的ではないため、どのような表現をとっても値が同じになることを示す。
> *命題1*  
> 非負単関数$X$の平均値は、その単関数の表現にかかわらず同じ値をとる。

もし二つの表現があったとする。
$$
X = \sum_{k=1}^n a_k I_{A_k} = \sum_{l=1}^m b_l I_{B_l}
$$

この時、$C_{kl} = A_k \cap B_l$として
$$
c_{kl} = \begin{cases}
  a_k (= b_l) & C_{kl} \neq \phi \\
  0 & C_{kl} = \phi
\end{cases}
$$

とすると、
$$
\begin{aligned}
\bm{E}[X] &= \sum_{k=1}^n a_k \bm{P}(A_k) \\
&= \sum_{k=1}^n a_k \sum_{l=1}^m \bm{P}(C_{kl}) \\
&= \sum_{k=1}^n \sum_{l=1}^m c_{kl} \bm{P}(C_{kl})
\end{aligned}
$$

となるが、これは$\{B_l\}$を使った場合の展開も同じことである。よって表現にはよらないことが確認できた。

その他にいくつか簡単な性質を並べておく。証明は先ほどと同じく$\{C_{kl}\}$を出してくればできるので、ここでは明示的に書くことはやめる。
> *命題2*  
> 非負単関数$X,Y$に対して

1. $X \le Y$の時、$\bm{E}[X] \le \bm{E}[Y]$
1. $\bm{E}[X + Y] = \bm{E}[X] + \bm{E}[Y]$

## 非負確率変数に対する定義

一段難しくなって単関数以外に対する定義をする。ただしまだ非負性は残している。
> *定義2*  
> 非負確率変数$X$は非負可測関数でもあるので、それに近づく近似単関数列$\{X_n\}$を取ることができる。この近似単関数列の平均値の極限を$X$の平均値と定義する。
$$
\bm{E}[X] \equiv \lim_{n \rightarrow \infty} \bm{E}[X_n]
$$

やはりこの場合でも先ほどと同様一意性が気になるので示しておく。
> *命題3*  
> 非負確率変数の平均値は、それを定義する際に使用する近似単関数列によらず一意に定まる。

非負確率変数$X$の近似単関数列として$\{X_n\}$と$\{Y_n\}$が取れたとする。これらから
$$
Z_n(\omega) = \max(X_n(\omega), Y_n(\omega)), \omega \in \Omega
$$

とすると、先ほどの非負単関数の平均値の性質より
$$
\bm{E}[X_n] \le \bm{E}[Z_n] \Rightarrow \lim_{n \rightarrow \infty} \bm{E}[X_n] \le \lim_{n \rightarrow \infty} \bm{E}[Z_n]
$$

また、適当に$m \in \mathbb{N}$と$\epsilon > 0$を決めて
$$
\Gamma_n \equiv \{\omega \in \Omega : X_n(\omega) > Z_m(\omega) - \epsilon\}
$$

とすると、この集合は単調増加して最終的には$\Omega$にたどり着く
$$
\Gamma_1 \subset \Gamma_2 \subset \cdots, \bigcup_{n=1}^{\infty} \Gamma_k = \Omega
$$

この集合の上では
$$
\bm{E}[Z_m I_{\Gamma_n}] < \bm{E}[X_n] + \epsilon
$$

となるが、両辺で$n$を無限に飛ばせば
$$
\bm{E}[Z_m] < \lim_{n \rightarrow \infty} \bm{E}[X_n] + \epsilon
$$

任意の$\epsilon > 0$と任意の$m \in \mathbb{N}$に対して成り立っているので、
$$
\lim_{m \rightarrow \infty} \bm{E}[Z_m] \le \lim_{n \rightarrow \infty} \bm{E}[X_n]
$$

と言える。よって、
$$
\lim_{n \rightarrow \infty} \bm{E}[X_n] = \lim_{n \rightarrow \infty} \bm{E}[Z_n]
$$

だが、$\{Y_n\}$に関しても同様のことが言えるはずなので、題意は得られる。

非負単関数に対して調べた性質をこちらでも示しておく。
> *命題4*  
> 非負確率変数$X,Y$に対して

1. $X \le Y$の時、$\bm{E}[X] \le \bm{E}[Y]$
1. $\bm{E}[X + Y] = \bm{E}[X] + \bm{E}[Y]$

一つ目は先ほどと同じく
$$
Z_n(\omega) = \max(X_n(\omega), Y_n(\omega)), \omega \in \Omega
$$

とすると、明らかに
$$
\bm{E}[X_n] \le \bm{E}[Z_n]
$$

極限を取れば
$$
\bm{E}[X] = \lim_{n \rightarrow \infty} \bm{E}[X_n] \le \lim_{n \rightarrow \infty} \bm{E}[Z_n] = \bm{E}[Y]
$$

もう一つの方は単純に非負単関数の時の結果を援用すれば示せる。
$$
\bm{E}[X + Y] = \lim_{n \rightarrow \infty} \bm{E}[X_n + Y_n] = \lim_{n \rightarrow \infty} (\bm{E}[X_n] + \bm{E}[Y_n]) = \bm{E}[X] + \bm{E}[Y]
$$

## 一般の確率変数に対しての定義

やっと一般の確率変数を取り扱うことができる。
> *定義3*  
> 確率変数$X$をその正の部分と負の部分に切り分けた時に
$$
\begin{aligned}
X^+(\omega) &= \max(X(\omega), 0) \\
X^-(\omega) &= -\min(X(\omega, 0))
\end{aligned}
$$

それぞれの平均値が発散しない
$$
\bm{E}[X^+] < \infty, \bm{E}[X^-] < \infty
$$

とき、確率変数$X$は平均可能であるといい、その平均値を
$$
\bm{E}[X] = \bm{E}[X^+] - \bm{E}[X^-]
$$

とする。

平均可能性を正の部分と負の部分に分けて考えるのは面倒なので、次の性質が使える。
> *命題5*  
> 確率変数$X$が平均可能であることと
$$
\bm{E}[|X|] < \infty
$$

は同値。

$$
\bm{E}[|X|] = \bm{E}[X^+] + \bm{E}[X^-]
$$

なので、明らか。

## その他

今までは定義や補題などに、この本に書いていない場合には、適当な名前をつけてきたが、それもそろそろめんどくさくなってきたので、今回から定義には「定義」、補題や定理などには「性質」とつけることにした。補題と定理のさがいまいちわかっておらず、区別するのもめんどくさいので、とりあえず「補題」という言葉に統一することにした。
