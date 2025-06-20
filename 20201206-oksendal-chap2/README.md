# エクセンダールの第二章のブラウン運動周辺のまとめ

次の本を読み始めている。

- [確率微分方程式](https://www.amazon.co.jp/dp/4621061763)、B.エクセンダール

今回は2章のブラウン運動周辺の内容についてまとめる。この本では各種の定理を紹介しながらブラウン運動の定義を導く様な形をとっているが、ここでは今後の章を読み進めていくにあったっての参考文書になる様に、ブラウン運動が結果的にどの様に定義されどの様な性質を持つかに着目してまとめていくことにする。

## ブラウン運動の定義

この本で紹介されているブラウン運動の定義を簡潔にまとめると以下の様になる。
> *ブラウン運動*  
> 任意の$x \in \mathbb{R}^n$に対して、ある確率空間$(\Omega, \mathcal{F}, \textbf{P}^x)$とその上の連続な$\mathbb{R}^n$-値確率過程$\{B_t\}_{t\ge0}$で次の条件を満たすものが取れる。すなわち、任意の$k \in \mathbb{N}$と$0=t_0 \le t_1 \le,\cdots \le t_k$、$F_1,F_2,\cdots,F_k \in \mathcal{B}(\mathbb{R}^n)$に対して
$$
\textbf{P}^x(B_{t_1} \in F_1, \cdots, B_{t_k} \in F_k) = \int_{F_1 \times \cdots \times F_k} \prod_{i=1}^k p(t_k - t_{k-1}, x_{k-1}, x_k) dx_1 \cdots dx_k
$$

ただしここで、$x=sx_0 \in \mathbb{R}^n$であり、$p$はガウス分布
$$
p(t, x, y) = (2 \pi t)^{-n/2} \exp(-\frac{|x-y|^2}{2t})
$$

である。この時、確率過程$\{B_t\}_{t \ge 0}$を$x$を出発するブラウン運動と呼ぶ。

重要なのはブラウン運動が連続であることと、上記の$P$に関する式、有限次元分布に関する式、を満たすことの二つである。
また、少なくともこの本で紹介されている限りでは、標本空間$\Omega$やそれに付随する完全加法族$\mathcal{F}$が具体的にどの様なものであるかは示されず、単に上記の様な条件を満たす確率空間を取ることができる、ということのみがわかっている。

## ブラウン運動の性質

ブラウン運動に関してのいくつかの性質を可能な限り簡潔に紹介していく。

$\{B_t\}_{t \ge 0}$はガウス過程である。よってその特性関数に関して次が成り立つ。
> *特性関数に関する性質*  
> 任意の$0 \le t_1 \le \cdots \le t_k$に対応する確率変数$Z=(B_{t_1}, \cdots, B_{t_k}) \in \mathbb{R}^{nk}$に対して、次の関係を満たすような$C_{ij}$と$M_j$が存在する。
$$
\textbf{E}^x[\exp(i \sum_{j=1}^{nk} u_j Z_{t_j})] = \exp(-\frac{1}{2} \sum_{i,j} u_i C_{ij} u_j + i \sum_{j} u_j M_j)
$$

この時、$M_i$と$C_{ij}$は以下の関係を満たすことが確認できる。
$$
\begin{aligned}
M_j &= \textbf{E}^x[Z_j] \\
C_{ij} &= \textbf{E}^x[(Z_i - M_i)(Z_j - M_j)]
\end{aligned}
$$

である。

ここから平均や共分散について次の性質が成り立つことがわかる。
> *ブラウン運動の平均や共分散*  
> 次が成り立つ。
$$
\begin{aligned}
\textbf{E}^x[B_t] &= x \\
\textbf{E}^x[(B_t - \textbf{E}[B_t])^2] &= nt \\
\textbf{E}^x[(B_t - \textbf{E}[B_t])(B_s - \textbf{E}[B_s])] &= n \min(s, t)
\end{aligned}
$$

さらに、$t \ge s$の時以下が成り立つ。
$$
\textbf{E}^x[(B_t - B_s)^2] = n(t-s)
$$

また、ブラウン運動$\{B_t\}_{t \ge 0}$は独立な増分を持つ。
> *ブラウン運動の増分の独立性*  
> 任意の$0 \le t_1 \le \cdots \le t_k$に対して
$$
B_{t_1}, B_{t_2} - B_{t_1}, \cdots, B_{t_k} - B_{t_{k-1}}
$$

は全て独立である。

## 備考

- ブラウン運動として常に連続な関数のみではなく、至るところ連続な関数を取る場合もあるようだが、今回は議論を簡潔にしていくために常に連続な場合をとった。
- ブラウン運動の裏にある標本空間$\Omega$はコルモゴロフの拡張定理によって存在が確認されるもので、この本を読む限りではその内容がどの様なものかは紹介されていない。基本的には分布で考えるのだろうなと思いつつ、少し気持ち悪さも抱えている。
