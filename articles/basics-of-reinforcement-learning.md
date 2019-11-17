強化学習の基礎
2018-10-20

@section{所感}

@p{院生のころは強化学習の分野に関係の深い研究をやっていたので日常的にその数式をいじっていたのだが、最近またその分野関連の論文をよく見るようになった。主な原因としては二つあって、一つは業務関連なのだがそれは社外秘が色々入ってくるので話せず、もう一つは趣味で見ている産業組織論系の論文によくBelleman方程式とかが出てくる。日常的にやっていた時なら理論の細かいところまで当然覚えていたのだが、離れると細かいところが頭から飛んで行くので何かしら参考文献が欲しいなとは思っていたが良い参考文献が意外と見当たらなかった。ちょうど過去にその分野の基礎の基礎をまとめたものを作った記憶があったので引っ張り出してまとめてみた。}

@ol
  {@a{Markov決定過程とBelleman方程式}{@rel{/build/mdp-and-belleman-equation.html}}}
  {@a{モデルありの強化学習}{@rel{/build/model-dependent-reinforcement-learning.html}}}
  {@a{モデルなしの強化学習}{@rel{/build/model-free-reinforcement-learning.html}}}

@p{今の所は適当に基礎をまとめてあるだけなので、最近の発展の内容は書いていない。ただし比較的重要な基礎はまとめてあるつもり。このブログ全体に言えることだが、自分用にまとめてあるだけなので他の人が見て面白いかはよくわからない。これらをまとめる時に参考にした文献を一応並べておく。}

@section{参考文献}

@ul
  {Richard S. Sutton and Andrew G. Barto (2000), @a{Reinforcement Learning}{https://mitpress.mit.edu/books/reinforcement-learning}, MIT Press}
  {Tommi Jaakkola and Michael I. Jordan (2008) @a{On the Convergence of stochastic iteration dynamic program- ming algorithms}{https://www.mitpressjournals.org/doi/abs/10.1162/neco.1994.6.6.1185?journalCode=neco}}
  {Pieter Abeel, @a{Markov Decision Process and Exact Solution Method slide}{https://people.eecs.berkeley.edu/~pabbeel/cs287-fa12/slides/mdps-exact-methods.pdf}, 2018年10月20日閲覧}