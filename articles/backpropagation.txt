backpropgationのまとめ
2018-11-29

@p{色々なネット上の記事が neural network におけるbackpropagationをまとめているが、どの記法の自分が十分に気にいるものではなかったので、自分の気に入る記法でまとめてみる。導出の対象は通常の neural network のみが対象で、convolutionなどをするものは対象外としておく。}

@p{まずはnetworkを記述するところから始める。考察の対象とする neural network は第@inmath{0}層を入力層とする@inmath{N+1}層を持つものとし、各層@inmath{i}には@inmath{M_i}個のneuronが存在するとする。入力層を除くそれぞれの層@inmath{i \in \{1, 2, \cdots, N \}}の@inmath{k}番目のneuronの活性度@inmath{a^i_k}は一つ下の層のneuronの活性度@inmath{a^{i-1}_k}から次のように定まる。}

@blmath{
\begin{aligned}
z^i_k &=\sum_{j=1}^{M_{i-1}} w^i_{kj} a^{i-1}_j \\
a^i_k &= \phi_i(z^i_k)
\end{aligned}
}

@p{ただしここで@inmath{w^i_{kj}}は@inmath{i}層の@inmath{k}番目のneuronと@inmath{i-1}層の@inmath{j}番目のneuronをつなぐ枝の重みであり、@inmath{\phi_i}は@inmath{i}層目の活性化関数である。ここで活性化関数が層@inmath{i}に依存しているのは、出力層などを統一的に表すためである。最終的な出力@inmath{a^N}によってコスト関数@inmath{E(a^N)}が定まり、これを最小化することが最急降下法の目的となる。}

@p{では早速コスト関数@inmath{E}をパラメータで微分してみる。層@inmath{i}の枝@inmath{w^i_{nm}}に対する勾配は}

@blmath{
\begin{aligned}
\frac{\partial E}{\partial w^i_{nm}} &= \frac{\partial E}{\partial a^i_n} \frac{\partial a^i_n}{\partial z^i_n} \frac{\partial z^i_n}{\partial w^i_{nm}} \\
&= \frac{\partial E}{\partial a^i_n} \phi'_i(z^i_n) a^{i-1}_m
\end{aligned}
}

@p{であるが、ここで先と同様に}

@blmath{
\xi^i_n = \frac{\partial E}{\partial a^i_n} \phi'_i(z^i_n)
}

@p{とすれば、勾配は}

@blmath{
\frac{\partial E}{\partial w^i_{nm}} = \xi^i_n a^{i-1}_m
}

@p{と表せる。}


@p{最終層@inmath{i=N}については}

@blmath{
\begin{aligned}
\frac{\partial E}{\partial w^N_{nm}} &= \xi^N_n a^{N-1}_m \\
\xi^N_n &= \frac{\partial E}{\partial a^N_n} \phi'_i(z^N_n)
\end{aligned}
}

@p{となるが、@inmath{\partial E / \partial a^N_n}が簡単に計算できるので勾配計算は簡単に可能。}


@p{最終層以外については}

@blmath{
\begin{aligned}
\xi^i_n &= \phi'_i(z^i_n) \frac{\partial E}{\partial a^i_n} \\
&= \phi'_i(z^i_n) \sum_{k=1}^{M_{i+1}} \frac{\partial E}{\partial a^{i+1}_k} \frac{\partial a^{i+1}_k}{\partial a^i_n} \\
&= \phi'_i(z^i_n) \sum_{k=1}^{M_{i+1}} \frac{\partial E}{\partial a^{i+1}_k} \frac{\partial a^{i+1}_k}{\partial z^{i+1}_n} \frac{\partial z^{i+1}_k}{\partial a^i_n} \\
&= \phi'_i(z^i_n) \sum_{k=1}^{M_{i+1}} \frac{\partial E}{\partial a^{i+1}_k} \phi'_i(z^{i+1}_n) w^{i+1}_{kn} \\
&= \phi'_i(z^i_n) \sum_{k=1}^{M_{i+1}} \xi^{i+1}_k w^{i+1}_{kn}
\end{aligned}
}

@p{として、@inmath{\xi^{i+1}_k}を最終層から逆に求めていけば、}

@blmath{
\frac{\partial E}{\partial w^i_{nm}} = \xi^i_n a^{i-1}_m
}

@p{と計算できる。これでbackpropagationの導出ができた。}


@p{まとめれば、学習はForwardパスでは入力@inmath{a^0}に対して@inmath{i=1,2,\cdots,N}層まで}

@blmath{
\begin{aligned}
z^i_k &=\sum_{j=1}^{M_{i-1}} w^i_{kj} a^{i-1}_j \\
a^i_k &= \phi_i(z^i_k)
\end{aligned}
}

@p{として計算をしていくことで出力を得られる。Backwardパスではまず最上層の@inmath{\xi^N}を計算し}

@blmath{
\xi^N_n = \frac{\partial E}{\partial a^N_n} \phi'_i(z^N_n)
}

@p{それを元に、@inmath{i=N-1,N-2,\cdots,1}層に対して@inmath{\xi^i}を計算していく。}

@blmath{
\xi^i_n = \phi'_i(z^i_n) \sum_{k=1}^{M_{i+1}} \xi^{i+1}_k w^{i+1}_{kn}
}

@p{最後に、全ての層@inmath{i=1,2,\cdots,N}に対して勾配}

@blmath{
\frac{\partial E}{\partial w^i_{nm}} = \xi^i_n a^{i-1}_m
}

@p{を実際に計算し適用する。以上でコスト@inmath{E}を最小化するような学習を行うことができる。}
