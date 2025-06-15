# backpropgationのまとめ

色々なネット上の記事が neural network におけるbackpropagationをまとめているが、どの記法の自分が十分に気にいるものではなかったので、自分の気に入る記法でまとめてみる。導出の対象は通常の neural network のみが対象で、convolutionなどをするものは対象外としておく。

まずはnetworkを記述するところから始める。考察の対象とする neural network は第$0$層を入力層とする$N+1$層を持つものとし、各層$i$には$M_i$個のneuronが存在するとする。入力層を除くそれぞれの層$i \in \{1, 2, \cdots, N \}$の$k$番目のneuronの活性度$a^i_k$は一つ下の層のneuronの活性度$a^{i-1}_k$から次のように定まる。

$$
\begin{aligned}
z^i_k &=\sum_{j=1}^{M_{i-1}} w^i_{kj} a^{i-1}_j \\
a^i_k &= \phi_i(z^i_k)
\end{aligned}
$$

ただしここで$w^i_{kj}$は$i$層の$k$番目のneuronと$i-1$層の$j$番目のneuronをつなぐ枝の重みであり、$\phi_i$は$i$層目の活性化関数である。ここで活性化関数が層$i$に依存しているのは、出力層などを統一的に表すためである。最終的な出力$a^N$によってコスト関数$E(a^N)$が定まり、これを最小化することが最急降下法の目的となる。

では早速コスト関数$E$をパラメータで微分してみる。層$i$の枝$w^i_{nm}$に対する勾配は

$$
\begin{aligned}
\frac{\partial E}{\partial w^i_{nm}} &= \frac{\partial E}{\partial a^i_n} \frac{\partial a^i_n}{\partial z^i_n} \frac{\partial z^i_n}{\partial w^i_{nm}} \\
&= \frac{\partial E}{\partial a^i_n} \phi'_i(z^i_n) a^{i-1}_m
\end{aligned}
$$

であるが、ここで先と同様に

$$
\xi^i_n = \frac{\partial E}{\partial a^i_n} \phi'_i(z^i_n)
$$

とすれば、勾配は

$$
\frac{\partial E}{\partial w^i_{nm}} = \xi^i_n a^{i-1}_m
$$

と表せる。

最終層$i=N$については

$$
\begin{aligned}
\frac{\partial E}{\partial w^N_{nm}} &= \xi^N_n a^{N-1}_m \\
\xi^N_n &= \frac{\partial E}{\partial a^N_n} \phi'_i(z^N_n)
\end{aligned}
$$

となるが、$\partial E / \partial a^N_n$が簡単に計算できるので勾配計算は簡単に可能。

最終層以外については

$$
\begin{aligned}
\xi^i_n &= \phi'_i(z^i_n) \frac{\partial E}{\partial a^i_n} \\
&= \phi'_i(z^i_n) \sum_{k=1}^{M_{i+1}} \frac{\partial E}{\partial a^{i+1}_k} \frac{\partial a^{i+1}_k}{\partial a^i_n} \\
&= \phi'_i(z^i_n) \sum_{k=1}^{M_{i+1}} \frac{\partial E}{\partial a^{i+1}_k} \frac{\partial a^{i+1}_k}{\partial z^{i+1}_n} \frac{\partial z^{i+1}_k}{\partial a^i_n} \\
&= \phi'_i(z^i_n) \sum_{k=1}^{M_{i+1}} \frac{\partial E}{\partial a^{i+1}_k} \phi'_i(z^{i+1}_n) w^{i+1}_{kn} \\
&= \phi'_i(z^i_n) \sum_{k=1}^{M_{i+1}} \xi^{i+1}_k w^{i+1}_{kn}
\end{aligned}
$$

として、$\xi^{i+1}_k$を最終層から逆に求めていけば、

$$
\frac{\partial E}{\partial w^i_{nm}} = \xi^i_n a^{i-1}_m
$$

と計算できる。これでbackpropagationの導出ができた。

まとめれば、学習はForwardパスでは入力$a^0$に対して$i=1,2,\cdots,N$層まで

$$
\begin{aligned}
z^i_k &=\sum_{j=1}^{M_{i-1}} w^i_{kj} a^{i-1}_j \\
a^i_k &= \phi_i(z^i_k)
\end{aligned}
$$

として計算をしていくことで出力を得られる。Backwardパスではまず最上層の$\xi^N$を計算し

$$
\xi^N_n = \frac{\partial E}{\partial a^N_n} \phi'_i(z^N_n)
$$

それを元に、$i=N-1,N-2,\cdots,1$層に対して$\xi^i$を計算していく。

$$
\xi^i_n = \phi'_i(z^i_n) \sum_{k=1}^{M_{i+1}} \xi^{i+1}_k w^{i+1}_{kn}
$$

最後に、全ての層$i=1,2,\cdots,N$に対して勾配

$$
\frac{\partial E}{\partial w^i_{nm}} = \xi^i_n a^{i-1}_m
$$

を実際に計算し適用する。以上でコスト$E$を最小化するような学習を行うことができる。
