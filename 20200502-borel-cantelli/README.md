# ボレル-カンテリの補題

相変わらず「測度から確率へ」を読み進めていて、今は第3章の「確率測度」の項目を読み進めている。第3章の内容は大きく分けて
- 確率測度の定義とその一般的な性質
- $d$次元ボレル集合体の上に定義される確率測度の性質
- 完備化とルベーグ測度の導入

になっているようで、やはり第2章と同じく、これからの議論を進めるために色々な場所の準備を進めている感じになっている。

今回はその中でも、確率測度の定義と性質の部分をまとめてみて、そのパートの最後に述べられている「ボレル-カンテリの定理」までを少し説明しようかと思う。

## 確率測度の定義と性質

確率測度はこの本では次のように定義されている。
> *確率測度*  
> 可測空間$(\Omega, \mathcal{B})$を考える。$\mathcal{B}$上の実数値関数$\bm{P}$が三つの条件
1. 任意の可測集合$A$に対して、$0 \le \bm{P}(A) \le 1$
1. $\bm{P}(\phi) = 0$
1. 互いに交わらない可測集合族$\{A_k\}_{k=1}^{\infty}$が与えられた時、$\bm{P}(\bigcup_{k=1}^{\infty} A_k) = \sum_{k=1}^{\infty} \bm{P}(A_k)$

を満たす時、$\bm{P}$を確率測度と呼び、組$(\Omega, \mathcal{B}, \bm{P})$を確率空間と呼ぶ。

確率を特徴付けるのに十分かどうかはすぐにはわからないが、確率の特徴として正しそうであることはすぐにわかる感じになっている。

このように定義した確率測度についていくつかその性質が紹介されている。
> *確率測度の性質*  
> $(\Omega, \mathcal{B}, \bm{P})$を確率空間とする。この時、
1. 任意の可測集合$A \subset B$に対して、$\bm{P}(A) \le \bm{P}(B)$
1. 任意の可測集合族$\{A_k\}_{k=1}^{\infty}$に対して、$\bm{P}(\bigcup_{k=1}^{\infty} A_k) \le \sum_{k=1}^{\infty} \bm{P}(A_k)$

一つ目の照明はとても簡単。
$$
\bm{P}(B) = \bm{P}(A) + \bm{P}(B-A) \ge \bm{P}(A)
$$

二つ目の証明は
$$
\begin{aligned}
B_1 &= A_1 \\
B_k &= A_k - \bigcup_{l=1}^{k-1} A_l
\end{aligned}
$$

という可測集合に注目することさえ見つけられれば証明は簡単。
$$
\bm{P}(\bigcup_{k=1}^{\infty} A_k) = \bm{P}(\bigcup_{k=1}^{\infty} B_k) = \sum_{k=1}^{\infty} \bm{P}(B_k) \le \sum_{k=1}^{\infty} \bm{P}(A_k)
$$


その他にも例えば、$\lim$と組み合わせたときの性質が紹介されていたり
> *単調増加する可測集合の確率測度*  
> 可測集合族$\{A_k\}_{k=1}^{\infty}$が単調増加($A_1 \subset A_2 \subset \cdots$)する時
$$
\bm{P}(\bigcup_{k=1}^{\infty} A_k) = \lim_{k \rightarrow \infty} \bm{P}(A_k)
$$

が成り立つ。

先ほどと同様に
$$
B_1 = A_1, B_k = A_k - A_{k-1}
$$

と定義すると、
$$
\bm{P}(\bigcup_{k=1}^{\infty} A_k) = \sum_{k=1}^{\infty} \bm{P}(B_k) = \lim_{n \rightarrow \infty} \bm{P}(\bigcup_{k=1}^n B_k) = \lim_{k \rightarrow \infty} \bm{P}(A_k)
$$

となり証明終了。

$\limsup$との性質が紹介されていたりした。
> *$\limsup$と確率測度の関係*  
> 任意の可測集合族$\{A_k\}_{k=1}^{\infty}$に対して
$$
\limsup_{k \rightarrow \infty} \bm{P}(A_k) \le \bm{P}(\limsup_{k \rightarrow \infty} A_k)
$$

が成り立つ。

まずは$\limsup$を分解して
$$
\limsup_{k \rightarrow \infty} A_k = \bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} A_k = \bigcap_{n=1}^{\infty} B_n
$$

と書くことにすると、$B_n$は単調減少していくことになる。先ほど単調増加について証明したことは単調現象の場合にも当てはまるので、
$$
\bm{P}(\limsup_{k \rightarrow \infty} A_k) = \lim_{n \rightarrow \infty} \bm{P}(B_n)
$$

また、任意の$k \ge n$に対して$A_k \subset B_n$なので、
$$
k \ge n, \bm{P}(A_k) \le \bm{P}(B_n) \Rightarrow \sup_{k \ge n} \bm{P}(A_k) \le \bm{P}(B_n)
$$

これらを合わせれば題意が得られる。
$$
\limsup_{k \rightarrow \infty} \bm{P}(A_k) \le \bm{P}(\limsup_{k \rightarrow \infty} A_k)
$$



## ボレル-カンテリの定理

まずはその定理の主張を見たい。
> *ボレル-カンテリの定理*  
> 任意の可測集合族$\{A_k\}_{k=1}^{\infty}$に対して
$$
\sum_{k=1}^{\infty} \bm{P}(A_k) < \infty \Rightarrow \bm{P}(\limsup_{k \rightarrow \infty} A_k) = 0
$$

ここまで準備してきてあれば、比較的証明は簡単にできる。
$$
\bm{P}(\limsup_{k \rightarrow \infty} A_k) = \lim_{n \rightarrow \infty} \sum_{k=n}^{\infty} \bm{P}(A_k) = \sum_{k=1}^{\infty} \bm{P}(A_k) - \lim_{n \rightarrow \infty} \sum_{k=1}^n \bm{P}(A_k) = 0
$$

今回は$\sum_{k=1}^{\infty} \bm{P}(A_k)$が収束しているから二つ目の式変形ができて引き算の形になったが、もし発散していたらそこの変形ができないので$0$にはならない。

ざっと定理を読んだだけだど演習問題のようで、特に名前がつくようなものに見えなかったので、一つ具体例を調べてみる。
> *無限回のコイントス*  
> 半分の確率で表と裏が出るコインを投げ続けるとする。投げ始めて$k$回連続で表が出るという事象を$A_k$と表せば、$\bm{P}(A_k) = 1/2^k$となる。明らかに
$$
\sum_{k=1}^{\infty} \bm{P}(A_k) < \infty
$$

なので、
$$
\bm{P}(\limsup_{k \rightarrow \infty} A_k) = 0
$$

この例における$\limsup_{k \rightarrow \infty} A_k$とは何かというと、その集合に含まれる標本$\omega$がどのような条件を満たしているかというと
$$
\omega \in \limsup_{k \rightarrow \infty} A_k \iff \forall n \in \mathbb{N}, \exists k \ge n, \omega \in A_k
$$

となるが、これは要するに無限回連続で表が出続けるような事象ということになる。この例においてボレル-カンテリの定理は、無限回連続で表が出る確率は$0$であるということを示しているということになる。
