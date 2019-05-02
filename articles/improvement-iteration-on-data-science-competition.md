データ分析コンペの取り組み方
2018-12-30


久々にkaggleコンペに参加して見たのだが、どうやって順位の改善を行なって行くかとかがわからなくなっていたので、次また思い出すところから始めないように一応メモしておく。


とりあえず自分がkaggleコンペに参加して最初に行うのは、そのコンペの概要と注力点を知ること。とりあえずそのコンペ自体の概要とデータの概説を読むのは当然として、ついでにDiscussionの購読もしておく。Discussionの購読はとても重要な気がしていて、これで朝電車の中とかでどういう感じのことがそのコンペでは重要になっていて、ほかの人がどういうことに注目して順位を上げていっているのかを知ることができるので重要。とりあえずこれで１週間ぐらい購読して入れば、ベースラインとしてどのような手法を参加者が使っていて、どこら
へんの問題を解けばどれくらい順位が上がりそうかみたいなことはわかる。


そしてそれと同時並行でベースラインレベルのモデルを作ることも行っておく。基本的には公開されているKernelを見て、真似してみれば大抵主催者側が出しているベースラインは超えることができる。ここでデータがどのような形をしていて、どういう特徴があって、どのような情報がそこに乗っているかを確かめることができる。ここまでくれば一応多くの参加者と同じスタートラインに立つことはできるはず。あとは簡単に適用できそうな手法がDiscussionで上がっていた場合にはここで使ってしまうかもしれない。これでだいたいKernelが公開されている最高の順位と同じくらいのレベルになれば十分。


次にLeaderboardでのスコアをsubmitしなくても再現できるような環境を可能な限り整える。とりあえず Cross Validation (CV) をして見るのは当然だが、最近のコンペだと\a{Covariate Shift}{https://www.kaggle.com/pavansanagapati/covariate-shift-what-is-it}が効いているようなコンペも多いので、それ用の対策を立てる必要があるかもしれない。まあ、Covarite Shift がある場合でもCVで出てきたスコアが低い場合には大抵Leaderboardでのスコアも低いので、正確なValidationをする方に注力するのはスコアの改善ループを少し回した後でも良いかもしれない。


そしてここから改善のループに入って行く。基本的に先に作ってみたベースラインモデルはあまり domain knowledge を入れない汎用的なモデルにとりあえずデータを入れて見ましたみたいなものが多いはずなので、そこにCVのスコアを見ながら徐々に domain knowledge を入れて行く作業を行なって行くことになるはず。基本的な戦略としては、そのデータの複雑性みたいなものに対してデータが十分に大きいのならば、比較的汎用的なモデルを使っても十分にその特徴を勝手に読み取ってくれる可能性が高いので、比較的汎用的な手法を使って feature learning らへんまでやって見るのが良いだろうし、複雑性に対してデータ量が比較的少ないのならば多分 domain knowledge を使ってデータが足りない分の情報を保管してやらないとうまく動かない可能性が高い。


例えばデータの複雑性に対して比較的データの量が多い場合には、人が domain knowledge を駆使してfeatureを色々と作るよりはデータから機械に勝手に学ばせてしまった方が良いことが多い。多分多くの画像系コンペはその分類に入るし、tabular data のコンペでも \a{representation learning を駆使した手法で優勝した例}{https://www.kaggle.com/c/porto-seguro-safe-driver-prediction/discussion/44629}などもあるので、機械に学ばせてしまう方が早いことも多い。もちろん \a{architecture engineering is the new feature engineering}{https://smerity.com/articles/2016/architectures_are_the_new_feature_engineering.html}という人もいるくらいなので、こういう手法を使ったところでどのようにその学習機に domain knowledge を入れるかという問題は解かなければならない。このような architecture engineering もやはり最初は domain knowledge があまり入っていない汎用のモデルで試して見て、そこから徐々にCVの結果を見ながら domain knowledge をその学修機の構造に入れて行くという作業を行なって行くことで徐々に改善して行くことができるはず。このfeatureとこのfeatureの間に相互作用はないからその間の相互作用項の係数は0にしておくかとか、このfeatureはそもそもあんまり関係ないからモデルから落とすかとか、そういう感じの大雑把な関係性みたいなものを学習機の構造に入れて行って、CVが上がったら採用、CVが下がったら不採用とするような作業を繰り返していけばいい。


他にはデータの複雑性に対して比較的データの量が少ない場合には、機械に勝手に学んでもらうことは難しいので、人が domain knowledge を駆使して良いfeatureを作ってあげたり、そもそもそのfeature間の関係性に対して　domain knowledge を駆使したモデルを作って見てfitさせるみたいなことが必要なはず。kaggleコンペでは本当に複雑性に対してデータ量が少なくて勝手に機械に学んでもらえそうなところがないみたいなコンペが出てくることは少ないのであんまりこのパターンに陥ることはないが、実際現実世界で突き当たるデータはそういうもの多い。こういう場合のイメージとしては物理学とかそこらへんのイメージで、とりあえずモデルを作ってみてそのパラメータをデータにfitさせることで計算するくらいのイメージの方がいい。データが多い場合にそれをやると、モデルが間違っていた場合に大変なのであまりよろしくないが、データが少ない場合にはそこまで指定しないと十分に意味のある結果を読み取ることができないので、とりあえずモデルを決めうちで作ってしまってパラメータだけ読み取る方が良いことが多い。


そして多くのコンペは上で述べた両極端、データの複雑性に対してデータ量が十分にあるときとない時の中間地点に散らばっているような感じになる。このような場合は基本的には上で述べた両極端の手法を組み合わせて分析して行くことにはなるが、どちらの極端から始めるかで少しアプローチが異なる。
\ol
{データ量が大きい場合のアプローチから初めて、データ量が少ない場合の手法を取り入れて行く感じのアプローチを取る場合は、とりあえず汎用的なモデルを立てて、そこに徐々に domain knowledge を組み込んで行く感じになる。とりあえずデータをxgboostにぶち込んでから、徐々に domain knowledge を駆使したfeatureを組み込んで行くのはこのアプローチに分類されるはず。多くのコンペの参加者は大抵この方法をとってくるはず。しっかりとCVを監視ししてその時に入れた domain knowledge が現実と間違っていないかを確認しつつ改善していけば、最初に使用した汎用モデルに、そのデータに適した良い感じの domain knowledge が組み込まれたようなものが出来上がってくるはず。}
{データ量が少ない場合の手法をもとに、データ量が大きい場合の手法を取り入れて行くアプローチを取る場合には、とりあえずざっくりと重要な特徴だけ捉えたモデルを自分で立てて見て、そのモデルに対して徐々に汎用性を持たせて行くアプローチを取ることになるはず。これは\a{TrackMLコンペの一位解法}{https://www.kaggle.com/c/trackml-particle-identification/discussion/63249}がとても参考になる。このコンペで扱われている対象が物理学の実験ということもあって、比較的シンプルな現象に対していくつかのノイズが乗っているようなデータセットとなっていたため、解法もそれに合わせてまず比較的シンプルなモデルを作って、そのモデルの自由度を徐々に上げていくことでノイズの部分に対応するという手法を取っている。}


基本的にはどのようなアプローチを取ろうとも、コンペ中の多くの時間はCVの結果を見ながら次のような調整を徐々に行ってモデルの純度みたいなものを高めて行くことになる。
\ul
{モデルに自分が知りうる限りの domain knowledge を入れる。ただし自分が入れた domain knowledge が間違って入ればモデルのパフォーマンスは下がるので、いま手元にあるモデルに対して間違った domain knowledge が入っている場合は取り除き、正しい domain knowledge が入っていればそれを入れ込むという作業を行う。そうして徐々に正しい domain knowledge だけを持ったモデルを構築して行く。}
{データから読み取れるだけの情報をモデルに読み取ってもらうようにモデルを変更する。データから読み取れないような情報をモデルに読み取ってもらおうとしてもモデルは読み取れないし、最悪ノイズによって変なパターンを読み取って悪影響を及ぼす。いま手元にあるモデルが、データから読み取りすぎているようなら domain knowledge でその点を保管してやる、データから読み取らなさすぎている場合にはモデルの自由度を上げて読み取れるようにする。}


自分でも考えをまとめながら書いているので散文になっている気がするが、とりあえずもう少し綺麗にまとまりそうならいつか別記事として出す日も来るかもしれない。