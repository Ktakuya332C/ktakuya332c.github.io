Markov決定過程とBelleman方程式
2018-10-20

@p{多くの強化学習の理論がベースとしているMarkov決定過程を紹介したのち、その上で定義される価値関数と行動価値関数についての再帰的な性質であるBellmen方程式を導出する。}

@p{強化学習ではエージェントと呼ばれる意思決定者がMarkov決定過程としてモデル化された環境と相互作用を行う。ここではMarkov決定過程はあくまでエージェントと相互作用する環境のみを指定し、エージェントは別に定義する。Markov決定過程の定義は以下のようになる。}

@def{Markov決定過程(Markov Decision Process, MDP)}{
@p{Markov決定過程とは組@inmath{(S,A,P,R)}のことを指す。}

@ul
  {@inmath{S=\{s_{1},s_{2},\cdots,s_{N_{s}}\}}は状態集合と呼ばれる有限の集合。}
  {@inmath{A}はそれぞれの状態に付随する有限集合@inmath{A(s)=\{a_{1}^{s},a_{2}^{s},\cdots,a_{N_{a}}^{s}\}}であり行動集合と呼ばれる。}
  {@inmath{P}は@inmath{S\times A}の要素で条件づけられる@inmath{S}上の確率分布@inmath{P(s'|s,a)}であり遷移確率と呼ばれる。以降@inmath{P(s'|s,a)}を省略して@inmath{P_{ss'}^{a}}と書く。}
  {@inmath{R}は関数@inmath{S\times A\times S\rightarrow\mathbb{R}}であり報酬と呼ばれる。以降@inmath{R(s,a,s')}を省略して@inmath{R_{ss'}^{a}}と書く。}
}

@p{以上の定義に加えて初期状態確率分布@inmath{q:S\rightarrow\mathbb{R}}を今回は仮定する。また、報酬は@inmath{S\times A\times S}で定まる確率変数とすることもあるが今回は決定的に@inmath{S\times A\times S}の要素の一つを指定すれば報酬も一つに定まるとする。また、遷移確率はどの状態に対しても吸収状態とならない場合を想定し吸収状態がある場合(エピソード的な場合)は考えない。さらにMDPと相互作用を行うエージェントは以下のように定義できる。}

@def{エージェント}{
@p{エージェントとは組@inmath{(\pi,\gamma)}のことをさす。}

@ul
  {@inmath{\pi}は状態集合@inmath{S}で条件づけられた行動集合上での確率分布@inmath{\pi(a|s):\ A(s)\rightarrow\mathbb{R}}であり方策と呼ばれる。}
  {@inmath{\gamma}は@inmath{[0,1)}の値をとる実数であり、割引率と呼ばれる。}
}

@p{MDPと相互作用を行うエージェントを定めれば、MDPによって定まる初期状態分布によって最初の状態@inmath{s_{0}}が定まり、エージェントの方策によって行動@inmath{a_{0}}が定まり、MDPの遷移確率により次の状態@inmath{s_{1}}が定まると同時に報酬@inmath{r_{1}}が定まるというように確率的に時間発展が定まる。}

@p{強化学習での問題はエージェントがどのようにすれば最大の報酬を得られるかである。その評価関数として以下を定める。}

@def{期待報酬}{
@p{エージェント@inmath{(\pi,\gamma)}がMDP@inmath{(S,A,P,R)}と相互作用している時の期待報酬を}

@blmath{
J=E_{\pi}[R]=\sum_{\chi}R(\chi)p(\chi)
}

@p{で定める。ただし@inmath{\chi}はエージェントとMDPが取り得る経路@inmath{\chi=s_{0}a_{0}r_{1}s_{1}a_{1}r_{2}\cdots}であり、}

@blmath{
\begin{aligned}
R(\chi) &= \sum_{k=1}^{\infty}\gamma^{k-1}r_{k} \\
p(\chi) &= q(s_{0})\pi_{s_{0}}^{a_{0}}P_{s_{0}s_{1}}^{a_{0}}\pi_{s_{1}}^{a_{1}}P_{s_{1}s_{2}}^{a_{1}}\pi_{s_{2}}^{a_{2}}\cdots
\end{aligned}
}

@p{を示す。}
}

@p{強化学習における問題はこの期待報酬を最大化するためにはどのような方策@inmath{\pi}を取れば良いかという問題となる。ここで最適方策を求める最に重要となる二つの関数を導入する。}

@def{価値関数、行動価値関数}{
@p{エージェント@inmath{(\pi,\gamma)}がMDP@inmath{(S,A,P,R)}と相互作用している時の価値関数を}

@blmath{
V^{\pi}(s)=E_{\pi}[R_{t}|s_{t}=s]=\sum_{\chi_{s_{t}=s}}R(\chi_{s_{t}=s})p(\chi_{s_{t}=s})
}

@p{で定め、行動価値関数を}

@blmath{
Q^{\pi}(s,a)=E_{\pi}[R_{t}|s_{t}=s,a_{t}=a]=\sum_{\chi_{s_{t}=s,a_{t}=a}}R(\chi_{s_{t}=s,a_{t}=a})p(\chi_{s_{t}=s,a_{t}=a})
}

@p{で定める。ただしここで@inmath{\chi_{s_{t}=s}}での和は@inmath{s_{t}=s}となる経路全てをとり、@inmath{\chi_{s_{t}=s,a_{t}=a}}での和は@inmath{s_{t}=s,a_{t}=a}となる経路全ての和をとる。他記号は}

@blmath{
\begin{aligned}
R_{t} &= \sum_{k=1}^{\infty}\gamma^{k-1}r_{t+k}\\
p(\chi_{s_{t}=s}) &= \pi_{s_{t}}^{a_{t}}P_{s_{t}s_{t+1}}^{a_{t}}\pi_{s_{t+1}}^{a_{t+1}}P_{s_{t+1}s_{t+2}}^{a_{t+1}}\pi_{s_{t+2}}^{a_{t+2}}\cdots\\
p(\chi_{s_{t}=s,a_{t}=a}) &= P_{s_{t}s_{t+1}}^{a_{t}}\pi_{s_{t+1}}^{a_{t+1}}P_{s_{t+1}s_{t+2}}^{a_{t+1}}\pi_{s_{t+2}}^{a_{t+2}}\cdots
\end{aligned}
}

@p{と定義している。}
}

@p{以上の定義から期待報酬@inmath{J}と価値関数@inmath{V^{\pi}}は @inmath{J_{\pi}=\sum_{s\in S}V^{\pi}(s)q(s)}の関係にあることがわかる。}

@p{また、価値関数、行動価値関数には次の再帰的な方程式であるBelleman方程式が成立する。}

@def{Belleman方程式}{
@p{任意の方策@inmath{\pi}に付随する価値関数@inmath{V^{\pi}}、行動価値関数@inmath{Q^{\pi}}について次の恒等式が成立する。}

@blmath{
\begin{aligned}
V^{\pi}(s) &= \sum_{a\in A(s)}\pi_{s}^{a}Q^{\pi}(s,a)\\
&= \sum_{a\in A(s)}\pi_{s}^{a}\sum_{s'\in S}P_{ss'}^{a}(R_{ss'}^{a}+\gamma V^{\pi}(s'))\\
Q^{\pi}(s,a) &= \sum_{s'\in S}P_{ss'}^{a}(R_{ss'}^{a}+\gamma V^{\pi}(s'))\\
&= \sum_{s'\in S}P_{ss'}^{a}(R_{ss'}^{a}+\gamma\sum_{a'\in A(s')}\pi_{s'}^{a'}Q^{\pi}(s',a'))
\end{aligned}
}
}

@p{@inmath{V^{\pi}}についてのみ証明する。}

@blmath{
\begin{aligned}
R(\chi_{s_{t}=s}) &= r_{t+1}+\gamma R(\chi_{s_{t+1}})\\
p(\chi_{s_{t}=s}) &= \pi_{s_{t}}^{a_{t}}P_{s_{t}s_{t+1}}^{a_{t}}p(\chi_{s_{t+1}=s})
\end{aligned}
}

@p{より、}

@blmath{
\begin{aligned}
V^{\pi}(s_{t}) &= \sum_{a\in A(s)}\pi_{s}^{a}\sum_{s'\in S}P_{ss'}^{a}\sum_{\chi_{s_{t+1}=s'}}(r_{t+1}+\gamma R(\chi_{s'}))p(\chi_{s_{t+1}=s'})\\
&= \sum_{a\in A(s)}\pi_{s}^{a}\sum_{s'\in S}P_{ss'}^{a}(R_{ss'}^{a}+\gamma V^{\pi}(s'))
\end{aligned}
}

@p{ただしここで@inmath{E_{\pi}[R_{t}|s_{t}=s]=E_{\pi}[R_{t+1}|s_{t+1}=s]}となることを使った。}
