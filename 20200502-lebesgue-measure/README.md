# ルベーグ測度の定義

相変わらず「測度から確率へ」を読み進めているが、今回はその3章の後半らへんをまとめようと思う。内容としては
1. 確率空間の完備化
1. 一般的な測度の導入
1. ルベーグ測度の導入

を説明していくことにする。最後のルベーグ測度の導入が主で、それより前の二つはそのための準備に見える。


## 確率空間の完備化

確率空間が完備であるとはどういうことかをまずは定義する。
> *完備確率空間*  
> 確率空間$(\Omega, \mathcal{B}, \bm{P})$に対して次の条件が成り立つとき、その確率空間は完備であるという。
$$
N \in \mathcal{B}, \bm{P}(N) = 0, A \subset N \Rightarrow A \in \mathcal{B}
$$

定義としては簡単で証明はしやすそうなのだが、この定義よりは適当にとってきた確率空間をもとに完備確率空間を作る、完備化と呼ばれる作業のほうが理解しやすい気がしている。
> *完備化*  
> 確率空間$(\Omega, \mathcal{B}, \bm{P})$から、新たな事象集合$\bar{\mathcal{B}}$を
$$
\bar{\mathcal{B}} = \{ A \subset \Omega : \exists A', A'' \in \mathcal{B}, A' \subset A \subset A'', \bm{P}(A'' - A') = 0\}
$$

とし、新たな確率測度$\bar{\bm{P}}$を
$$
\bar{\bm{P}}(A) = \bm{P}(A')
$$

として、完備確率空間$(\Omega, \bar{\mathcal{B}}, \bar{\bm{P}})$を作成する作業を完備化と呼ぶ。

この作業で本当に確率空間が作れるのかどうかは一応確かめておく必要がある。確かめる点としては
1. $\bar{\mathcal{B}}$が$\sigma$-集合族であること
1. $\bar{\bm{P}}$が一意であること
1. $\bar{\bm{P}}$が確率測度であること
1. $(\Omega, \bar{\mathcal{B}}, \bar{\bm{P}})$が完備であること

の四つ。

$\bar{\mathcal{B}}$が$\sigma$-集合族であることは以下のように示せる。
1. $\Omega \in \mathcal{B}$より、$\Omega \in \bar{\mathcal{B}}$
1. $A \in \bar{\mathcal{B}}$の時、$A', A'' \in \mathcal{B}$があって、$A' \subset A \subset A''$と$\bm{P}(A'' - A') = 0$を満たす。これらの条件はどちらも$A'$と$A''$の補集合をとっても似た性質が成り立つので、$A^C \in \bar{\mathcal{B}}$
1. $\bar{\mathcal{B}}$-可測集合族$\{A_k\}_{k=1}^{\infty}$をとると、その定義から$\mathcal{B}$-可測集合族$\{A'_k, A''_k\}_{k=1}^{\infty}$が取れて、$A'_k \subset A_k \subset A''_k$と$\bm{P}(A''_k - A'_k)=0$が成り立つ。それらの和集合$\bigcup_{k=1}^{\infty} A_k$に対しては、$\bigcup_{k=1}^{\infty} A'_k \subset \bigcup_{k=1}^{\infty} A_k \subset \bigcup_{k=1}^{\infty} A''_k$と、$\bm{P}(\bigcup_{k=1}^{\infty} A''_k - \bigcup_{k=1}^{\infty} A'_k) \le \bm{P}(\bigcup_{k=1}^{\infty} (A''_k - A'_k)) = 0$が成り立つので、$\bigcup_{k=1}^{\infty} A_k \in \bar{\mathcal{B}}$


$\bar{\bm{P}}$が一意であることは、二つ取れた場合に$\bar{\bm{P}}_1, \bar{\bm{P}}_2$それらが必ず同じであることを示せればいい。適当に$\bar{\mathcal{B}}$-可測集合$A$をとると、それを中と外から囲う二つの$\mathcal{B}$-可測集合$A', A''$をとることができて
$$
\begin{aligned}
\bm{P}(A') \le \bar{\bm{P}}_1(A) \le \bm{P}(A'') \\
\bm{P}(A') \le \bar{\bm{P}}_2(A) \le \bm{P}(A'') \\
\end{aligned}
$$

が成り立つ。それらを組み合わせれば
$$
\bm{P}(A') \le \bar{\bm{P}}_2(A) \le \bar{\bm{P}}_1(A) \le \bm{P}(A') \\
$$

とすることができて、$\bar{\bm{P}}_2(A) = \bar{\bm{P}}_1(A)$がわかる。

$\bar{\bm{P}}$が確率測度測度であることは以下のように示せる。
1. 任意の$A \in \bar{\mathcal{B}}$に対して$0 \le \bar{\bm{P}}(A) \le 1$は自明
1. $\bar{\bm{P}}(\phi)=0$も自明
1. 互いに交わらない$\bar{\mathcal{B}}$-可測集合族$\{A_k\}_{k=1}^{\infty}$が取れたとき、それらに囲まれる$\mathcal{B}$-可測集合族$\{A'_k\}_{k=1}^{\infty}$が取れる。これを仲介として$\bar{\bm{P}}(\bigcup_{k=1}^{\infty} A_k) = \bm{P}(\bigcup_{k=1}^{\infty} A'_k) = \sum_{k=1}^{\infty} \bm{P}(A'_k) = \sum_{k=1}^{\infty} \bar{\bm{P}}(A_k)$となる。

最後に$(\Omega, \bar{\mathcal{B}}, \bar{\bm{P}})$が完備であることは、
$$
N \in \bar{\mathcal{B}}, \bar{\bm{P}}(N) = 0, A \subset N
$$

となる任意の$A \subset \Omega$に対して、
$$
\begin{aligned}
\phi \subset A \subset N \\
\bar{\bm{P}}(N - \phi) = 0
\end{aligned}
$$

となるので、$A \in \bar{\mathcal{B}}$が確認できる。


## 一般的な測度の導入

この本ではこれまで確率測度しか導入しておらず、一般的な測度の定義を導入していなかったが、ここで一応導入しておくことにする様子。多分主な目的はルベーグ測度を導入することで、それ以外に使う用途はなさそうだが、一応まとめる。
> *測度*  
> 可測空間$(\Omega, \mathcal{B})$を考える。$\mathcal{B}$上の含む実数値関数$\bm{m}$が次の条件を満たす時それを測度と呼ぶ。ただし測度のとりうる値として$\infty$も許すこととする。
1. 任意の$A \in \mathcal{B}$に対して、$0 \le \bm{m}(A) \le \infty$
1. $\bm{m}(\phi) = 0$
1. 互いに交わらない$\mathcal{B}$-可測集合族$\{A_k\}_{k=1}^{\infty}$に対して、$\bm{m}(\bigcup_{k=1}^{\infty} A_k) = \sum_{k=1}^{\infty} \bm{m}(A_k)$

また、$(\Omega, \mathcal{B}, \bm{m})$の組を測度空間と呼ぶ。

また、この特殊なものの一つとして次の定義が挙げられている。
> *$\sigma$-有限測度*  
> 測度空間$(\Omega, \mathcal{B}, \bm{m})$を考える。$\Omega$を可算の部分集合に分割したときに、それぞれの測度が有限である場合、
$$
\Omega = \bigcup_{n=1}^{\infty} \Omega_n, \Omega_m \cap \Omega_n = \phi (m \neq n), \bm{m}(\Omega_n) < \infty
$$

その測度を$\sigma$-有限測度であるという。

$\sigma$-有限測度の使い道については何も述べられていないので、どう伏線を回収していくのか、この先のお楽しみのような形になっている様子。


## ルベーグ測度の導入

ここまで準備してあるとルベーグ測度の導入は早い。
> *1次元ルベーグ測度*  
> $(\mathbb{R}, \bm{B}_1)$上の測度$\bm{m}_0$で、
$$
\bm{m}_0((a, b]) = b - a, -\infty < a \le b \le \infty
$$

となるものが存在することが知られている。この測度空間を完備かしたものを$(\mathbb{R}, \bm{M}_1, \bm{m})$と書き、$\bm{M}_1$を一次元ルベーグ可測集合、$\bm{m}$を1次元ルベーグ測度と呼ぶ。

また、これを実数全体ではなくもっと狭い範囲のみに注目したものも定義しておく様子。これもどこかでまた使うのだろう。
> *ルベーグ空間*  
> 特にこれを実数全体ではなくて、$(0, 1]$に制限したものを考えると
- 標本空間$\Omega = (0, 1]$
- 事象集合$\bm{M}(0, 1] = \bm{M}_1 \cap (0, 1]$
- 確率測度$\bm{m}$

となる確率空間を作ることができる。これをルベーグ空間と呼ぶ。

そういえば多次元の場合の導入はしていないが、この本では使わないということで良さそう。知りたくなったら、また別の測度論のみを取り扱った本でも読んでみよう。
