# 「測度から確率へ」の第2章のまとめ

測度論が色々な場面で使われているのを見つつも基礎から学んだことがなかったので、最近この教科書

- [はじめての確率論 測度から確率へ](https://www.kyoritsu-pub.co.jp/bookdetail/9784320014732)

で基礎から学んでみている。ただ読んでいくだけでも面白いのだが、せっかくなのでブログにまとめつつ読んでいこうと思う。

## 第2章の概観

この本の第1章は、確率論を議論するにあたって測度論のような理論がなぜ必要なのかを説明している章になっている。特に複雑なことは言っていないので、ブログにまとめを書くことはしない。
今回まとめる予定の第2章は、これからの議論のための土台づくりのような章になっている。大まかにいって

1. $\sigma$-集合体の定義とその性質
1. $\sigma$-集合体の具体例の紹介

の二つの内容から構成されているが、それら以外にも少し後の章のための伏線のような事実がいくつか紹介されている。

## $\sigma$-集合体の定義とその性質

いきなりだが$\sigma$-集合体の定義を紹介する。
> *$\sigma$-集合体*  
> 空でない集合$\Omega$の部分集合族$\mathcal{B}$が$\Omega$上の$\sigma$-集合体であるとは、$\mathcal{B}$が次の三つの条件を満たすことを指す。

1. $\Omega \in \mathcal{B}$
1. $A \in \mathcal{B} \Rightarrow A^C \in \mathcal{B}$
1. 任意の$k \in \mathbb{N}$に対して$A_k \in \mathcal{B}$ならば、$\bigcup_{k=1}^{\infty} A_k \in \mathcal{B}$

この定義から簡単にわかる$\sigma$-集合体の性質として、例えば次のようなものがある。
> *$\sigma$-集合体の性質*  
> 任意の$k \in \mathbb{N}$に対して$A_k \in \mathcal{B}$である時、以下が成り立つ。

1. $\bigcap_{k=1}^{\infty} A_k \in \mathcal{B}$
1. $\limsup_{k \rightarrow \infty} A_k \in \mathcal{B}$
1. $\liminf_{k \rightarrow \infty} A_k \in \mathcal{B}$

ただしここで、
$$
\begin{aligned}
\limsup_{k \rightarrow \infty} A_k &= \bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} A_k \\
\liminf_{k \rightarrow \infty} A_k &= \bigcup_{n=1}^{\infty} \bigcap_{k=n}^{\infty} A_k
\end{aligned}
$$

である。

1つ目の性質は、次のように順を追って証明することができる。

1. $A_k \in \mathcal{B}$より、$A_k^C \in \mathcal{B}$
1. $A_k^C \in \mathcal{B}$より、$\bigcup_{k=1}^{\infty} A_k^C \in \mathcal{B}$
1. $\bigcup_{k=1}^{\infty} A_k^C \in \mathcal{B}$より、$\bigcap_{k=1}^{\infty} A_k \in \mathcal{B}$

2つ目と3つ目の性質は、すでに$\sigma$-集合体は可算個の合併と交叉に閉じていることがわかっているので明らか。

すぐに$\sigma$-集合体の具体例を紹介したいところだが、いくつかの例を作るために次の性質を示しておく必要がある。
> *$\sigma$-集合体の生成*  
> $\Omega$に対する任意の部分集合族$S$に対して、それを含む最小の$\sigma$-集合体が唯一存在する。
このような$\sigma$-集合体を、$S$から生成される$\sigma$-集合体と呼び、$\sigma[S]$と書く。

どんな部分集合族$S$も$\Omega$の冪集合$2^{\Omega}$には必ず含まれるので、$S$を含む$\sigma$-集合体は最低でも一つは存在する。$S$を含む$\sigma$-集合体の全体を$\{\mathcal{B}_{\lambda} : \lambda \in \Lambda\}$と表すことにすると、
$$
\begin{aligned}
\mathcal{B}_1 = \bigcap_{\lambda \in \Lambda} \mathcal{B}_{\lambda}
\end{aligned}
$$

は、$S$を含む任意の$\sigma$-集合体に含まれる。さらにこの集合族は$\sigma$-集合体となる条件三つを満たす。

1. $\Omega \in \mathcal{B}_1$
1. $A \in \mathcal{B}_1$ならば、$A^C \in \mathcal{B}_1$
1. 任意の$k \in \mathbb{N}$に対して$A_k \in \mathcal{B}_1$ならば、$\bigcup_{k=1}^{\infty} A_k \in \mathcal{B}_1$

よって、$\mathcal{B}_1$は$S$を含む最小の$\sigma$-集合体である。また、もし他に同じく$S$を含む最小の$\sigma$-集合体として$\mathcal{B}_2$が存在したとすれば、$\mathcal{B}_1$の定義から
$$
\mathcal{B}_1 \subset \mathcal{B}_2
$$

となるが、$\mathcal{B}_2$の最小性から同様に$\mathcal{B}_2 \subset \mathcal{B}_1$となり、結果的に$\mathcal{B}_1 = \mathcal{B}_2$となるため、唯一である。

## $\sigma$-集合体の具体例の紹介

この本では$\sigma$-集合体の具体例をいくつか紹介している。
> *可算集合とその補集合で構成される$\sigma$-集合体*  
> $\Omega$を空でない集合として
$$
\mathcal{B}_{\#}(\Omega) = \{A \in \Omega : AまたはAの補集合が高々可算\}
$$

とすると、$\mathcal{B}_{\#}(\Omega)$は$\Omega$上の$\sigma$-集合体である。

$\sigma$-集合体であることは

1. $\phi \in \mathcal{B}_{\#}(\Omega)$より、$\Omega \in \mathcal{B}_{\#}(\Omega)$
1. $A \in \mathcal{B}_{\#}(\Omega)$なら$A^C \in \mathcal{B}_{\#}(\Omega)$は、明らか
1. 任意の$k \in \mathbb{N}$に対して$A_k \in \mathcal{B}_{\#}(\Omega)$の時、$A_k$が全て可算集合ならその可算個の合併$\bigcup_{k=1}^{\infty} A_k$も可算集合。もし一つでも補集合が可算なものがあれば、$(\bigcup_{k=1}^{\infty} A_k)^C = \bigcap_{k=1}^{\infty} A_k^C$が可算になる。よっていずれにしろ、$\bigcup_{k=1}^{\infty} A_k \in \mathcal{B}_{\#}(\Omega)$

として確認できる。

> *ボレル集合体*  
> 距離空間$E=(E, \bm{d})$を考える。$E$の開集合全体$\mathcal{O}$から生成される$\sigma$-集合体をボレル集合体と呼び、
$$
\mathcal{B}(E) = \sigma[\mathcal{O}]
$$

と書く。また、その要素をボレル集合と呼ぶ。

ボレル集合の要素としては

- $E$の開部分集合全体
- $E$の閉部分集合全体
- $E$の可算集合全体
- $E$の有限集合全体

などが含まれる。

> *$d$次元ボレル集合体*  
> 距離空間$E$として$d$次元ユークリッド空間$\mathbb{R}^d$を取った場合のボレル集合を$\bm{B}_d$と書き
$$
\bm{B}_d = \mathcal{B}(\mathbb{R}^d)
$$

$d$次元ボレル集合体と呼ぶ、また、その要素を$d$次元ボレル集合と呼ぶ。

「$d$次元」と入ると一般の距離空間ではなく$d$次元ユークリッド空間を対象にすることに注意。

## 備考

この本の2章ではここで記載した内容以外に

- $d$次元ボレル集合体の幾つかの性質の紹介
- ボレル集合体と連続関数の関係

について紹介しているのだが、きりが良いので一度ここでこの記事は終わりとして、それらは他の記事に回すことにする。
