Berry's inversion
2018-11-15

@p{相変わらずこの論文}

@ul
  {M.Igami (2015), @a{Estimating the Innovotr's Dilemma: Structual Analysis of Creative Destruction in the Hard Disk Drive Industry}{https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1733174}}

@p{を読もうとしているのだが、この論文の途中で需要を推定するために Berry's inversion という方法を使用しているらしいことがわかった。Berry's inversion という手法はこの論文}

@ul
  {S.T. Berry (1994), @a{Estimating Discrete-Choice Models of Product Differentiation}{https://www.jstor.org/stable/2555829}}

@p{で発表された手法で、寡占市場における消費者の選好を離散選択モデルで表現した場合の、そのパラメータの推定方法のことを指している。論文を読む限りでは、それまでの手法においては分析者は分析対象の寡占市場で売られている商品の特徴を全て知っている必要があったが、Berry's inversion を使用すれば分析者が商品の特徴を一部知らない場合でもパラメータをきちんと推定できることが特徴らしい。この文献の先行文献に当たりそうなものを一つも知らないので、この手法の発明がどれほどすごいものだったかはよくわからないが、とりあえず色々なところで見るので一応まとめておこうと思う。}

@section{仮定する寡占市場のモデル}

@p{ある市場を考える。この市場では@inmath{N}社の企業がそれぞれ一つの商品を販売していると仮定する。具体的には今現在の車市場のようなものを考えるとイメージがしやすい。トヨタや日産など大きな会社が凌ぎを削っていて寡占市場となっており、食品市場のような無数の企業が互いに競争していて完全競争に近い状態にはなっていない市場を考えている。ただし現在の車市場を見てもわかるように、いくら寡占市場といえども完全にいくつかの企業が独占することは少なく、ニッチなニーズに応えられるような小さい企業もいくつか存在している状況を考える。}

@p{それぞれの企業@inmath{j \in \{1, 2, \cdots, N \}}は全く同じものを売っているわけではなく、それぞれある程度差別化されたものを販売している。それぞれの商品の特徴を例えばベクトル@inmath{z_j}として表す方法もあるわけだが、ここで少し注意する必要がある。消費者はそれぞれの商品の特徴をみてどの商品を買うかを決めるわけだが、その市場を分析しようとしている人にとってはそれら商品の全ての特徴を観察することができない場合が多々ある。例えば車を買おうとする消費者の意思決定に影響を与えそうな車の特徴としては、その値段、燃費など定量化しやすくかつその市場の分析者が手に入れやすそうな情報もあるが、その車の形のかっこよさやその企業がその車にかける売り込みの意気込みなどは分析者がその情報を手に入れにくい。よって各商品の特徴ベクトル@inmath{z_j}を二つに分け、分析者が観察できる要素のみを集めたベクトル@inmath{x_j}と分析者が観察できない要素のみを集めたベクトル@inmath{\xi_j}と分けて記述することとする。}

@p{ある特定の消費者@inmath{i}は各商品@inmath{j \in \{1, 2, \cdots, N \}}の性質@inmath{(x_j, \xi_j)}に応じて線形的に効用@inmath{u_{ij}}を変化させると仮定する。ただしここでその商品の値段@inmath{p_j}だけは重要な変数であるため、分析者が観察できる商品の特徴ベクトル@inmath{x_j}から外して少し特別扱いしておく。}

@blmath{
\begin{aligned}
u_{ij} &= \delta_j + \nu_{ij} \\
\delta_j &= x_j \beta - \alpha p_j + \xi_j
\end{aligned}
}

@p{ただしここで@inmath{\nu_{ij}}は消費者毎の差異を表す項であり、のちの分析が容易になるようにガンベル分布をとると仮定する。また、@inmath{\alpha, \beta}はパラメータであり、これらを推測することがのちの目的となる。さらに、消費者はその市場における大きい企業@inmath{N}社だけでなく、その他にその市場に存在するいくつかの小さい企業からも商品を買うことができる。これらの企業をまとめて企業番号@inmath{0}と記述することとし、これらの企業によって販売される商品から得られる効用はベースラインとして値@inmath{0}を取ると仮定する。}

@blmath{
u_{i0} = 0
}

@p{消費者毎の差異を表す項@inmath{\nu_{ij}}がガンベル分布をとるという仮定を置いたことで、その分布の性質から消費者が商品@inmath{j \in \{ 1, 2, \cdots, N\}}を選択する確率を次のように比較的簡単な式で表すことができる。}

@blmath{
P(j | x, p, \xi) = \frac{\exp(\delta_j(x_j, p_j, \xi_j))}{1 + \sum_{k=1}^N \exp(\delta_k(x_k, p_k, \xi_k))}
}

@p{各消費者は上記の確立に沿って商品@inmath{j \in \{ 1, 2, \cdots, N\}}を購入することになるため、消費者の数が十分に大きいとすれば商品@inmath{j}がその市場で占めている売上個数の割合@inmath{s_j}は}

@blmath{
s_j = P(j | x, p, \xi)
}

@p{となるはずである。}

@section{パラメータの推定}

@p{上記の効用@inmath{u_{ij}}のパラメータを推定することを考える。特に重要なのは値段に対してどの程度効用が変化するかを測る変数@inmath{\alpha}であるから、特に以下ではこの値を推測することを考える。}

@p{パラメータの推定に使用できるデータとして、いくつかの時点@inmath{t}における次のデータが存在することを仮定する。}

@ul
  {考察対象以外の企業集団の市場シェア@inmath{s_0^t}}
  {特定の企業@inmath{j}の市場シェア@inmath{s_j^t}}
  {特定の企業@inmath{j}の商品の観測可能な性質@inmath{x_j^t}}
  {特定の企業@inmath{j}の商品の値段@inmath{p_j^t}}
  {特定の企業@inmath{j}の商品の値段とのみ因果関係があるが、その企業の商品の特徴@inmath{x_j, \xi_j}とは関係のない何らかの操作変数@inmath{c^t}}

@p{ここで@inmath{c_j^t}の具体例としては、例えば企業@inmath{j}が商品を生産する際に必要となる材料の値段や従業員へ支払う給料などが挙げられる。これらは製品の特徴へは直接は関係ないことが多いため操作変数として使えることが多い。他には他の企業@inmath{i \in \{ 1, 2, \cdots, N\}}の商品の観察可能な特徴@inmath{x_i^t}などが挙げられる。このような他企業@inmath{j}の製品の性質は直接値段に影響することはあるが、企業@inmath{j}の商品の性質にまで影響があるかというと比較的無視できると仮定することが多い。}

@p{時刻@inmath{t}での企業@inmath{j}の市場シェア@inmath{s_j^t}と、考察対象以外の企業集団の市場シェア@inmath{s_0^t}は以下のように書ける。}

@blmath{
\begin{aligned}
s_j^t &= \frac{\exp(\delta_j^t)}{1 + \sum_{k=1}^N \exp(\delta_k)} \\
s_0^t &= \frac{1}{1 + \sum_{k=1}^N \exp(\delta_k)}
\end{aligned}
}

@p{どちらの式についても両辺についてlogをとれば}

@blmath{
\begin{aligned}
\log(s_j^t) &= \delta_j^t - \log(1 + \sum_{k=1}^N \exp(\delta_k)) \\
\log(s_0^t) &= 0 - \log(1 + \sum_{k=1}^N \exp(\delta_k))
\end{aligned}
}

@p{となる[2]。よって上の式から下の式を引けば}

@blmath{
\log(s_j^t) - \log(s_0^t) = \delta_j^t = x_j^t \beta - \alpha p_j^t + \xi_j^t
}

@p{とかけることになる。最後に操作変数@inmath{c^t}を使用して、両辺との相関をとれば、操作変数の性質として@inmath{x_j^t}と@inmath{\xi_j^t}との相関は排除されているはずである}

@blmath{
\begin{aligned}
\mathrm{Cov}(c, x_j) &= 0 \\
\mathrm{Cov}(c, \xi_j) &= 0
\end{aligned}
}

@p{であるから、}

@blmath{
\mathrm{Cov}(c, \log(s_j) - \log(s_0)) = - \alpha \mathrm{Cov}(c, p_j)
}

@p{より、}

@blmath{
\alpha = \frac{\mathrm{Cov}(c, \log(s_j) - \log(s_0))}{\mathrm{Cov}(c, p_j)}
}

@p{と計算することができる。ただし、Covは全て時間@inmath{t}方向でとっている。}

@section{参考文献}

@ol
  {@a{Lecture notes: Discrete Choice Demand Models}{http://www.its.caltech.edu/~mshum/gradio/berry.pdf}}
  {@a{Cross Validted, Berry inversion}{https://stats.stackexchange.com/questions/86715/berry-inversion}}
  {@a{Empirical Model of Differentiated Products}{https://www.cemmap.ac.uk/uploads/cemmap/resources%20(slides)/Steven%20Berry%20-%20slides%2018.06.15.pdf}}
