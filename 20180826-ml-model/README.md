# 機械学習モデルはデータ+形式知+暗黙知で成り立っている

 ある教師付きのデータを渡されたとして、そのデータからそれぞれのデータ点に対するラベルを予測するような機械学習モデルを作成することを考える。このような時にまず一番初めに考える点の一つとして、そのデータに対してどのような情報を仮定して良いかということがある。もし自分がそのデータについてほとんど何も知らないのならば、あるデータ点のラベルはある程度その近傍の点と同じようなラベルを持っているだろうと考えて K Nearest Neighbors 法を適用しておくのが一番無難だろう。しかしそのような手法がうまく働く為には膨大な量のデータが必要になる。ここでもし、そのデータが二つのGaussian分布からサンプルされたもので、ラベルはそのどちらの分布からサンプルされたものかを示しているなどという情報を事前に持っていたならば、そのような情報を生かした手法(Linear Regression などで十分な場合が多そう)を使うことができるだろう。このような手法はデータ数が少なくてもうまく動くことが多い。このように、機械学習モデルの予測精度は「データの量+データに対する正しい知識の量」に比例することが多い。

ここでデータに対する正しい知識とはなんだろうか。例えばいろいろな物を投げたときの軌道のデータ与えられて、その軌道を予測するような機械学習モデルを作成する場合を考える。このとき、物体は基本的に放物線を描いて飛んでいくという「データに対する正しい知識」を持っていれば予測精度を上げることは造作もないだろう。このような場合には「データに対する正しい知識」というのは言葉で表せるし、なんなら数式でも表すことができる。そしてその数式をもとに予測モデルを作成することができる。しかし例えばMNISTデータを分類するような機械学習モデルを考えるに当たって必要となりそうな「データに対する正しい知識」とはなんだろうか。なんとなく二次元であることというのは効きそうなきがするが、このような直感的な印象をどのように機械学習モデルに組み込めば良いのだろうか。これらのように、「データに対する正しい知識」というのは大抵二つに分けることができる。一つは「放物線を描いて飛ぶ」のように明確に言葉にできるもの、形式知、であり、もう一つは「二次元であることが効きそう」などの明確には言葉にできないもの、暗黙知、だ。

形式知は機械学習モデルに組み込みやすいが、暗黙知はとても組み込みにくい。例えば画像に対して効きそうだなと直感的に感じていた「二次元であること」などの特徴はどのように機械学習に組み込めばいいかはとても曖昧だ。もちろん、そのような直感を数式にまで落としたものは存在し、それがいま猛威をふるっている Convoluional Neural Network などなのだが、そのようなデータを見てからすぐに得られるものでもなく、実際そのモデルが発見されるまでには長い研究の歴史がある。

Kaggleで扱われる問題に対して自分たちは物理学に対してほど形式知を持ってはいないが、画像や言語に対するほど暗黙知が多いわけでもない。例えばCTR予測問題などについて、自分たちは誰に対してどのような広告を見せるとクリックをするかを明確に判断できるような形式知を持ちわせてはいないが、それぞれの人間がなにかしらの性向を持っていてそれに合致するような広告が出てくればクリックをするなどの知識は持ち合わせている。このような問題に対して自分たちは形式知と暗黙知のどちらもを使用して予測モデルを作成する必要がある。

もちろんそのどちらもを含むような統一モデルを作れるのならそれが一番だ。例えばmathetakeさんの[この発表](https://speakerdeck.com/mathetake/yusaxing-dong-falseshu-li-moteruto-gao-su-tui-jian-sisutemu)では数理的に明らかなことから出発して推薦システムを作成している。このように「データに対する正しい知識」を綺麗に取り入れて予測モデルを作れるのならそれが一番だが、そのようなモデルを作成することは難しい。特に暗黙知の部分は数式に落とすことが難しいので、一昼夜で作成できるようなものではない場合が多い。

この統一モデル作成の代替手段としてKaggleなどで選ばれている手段が特徴量生成とXgboostなどを合わせて使用する方法だろう。Xgboostなどのよく知られたモデルがうまく暗黙知の部分をカバーしてくれるので、自分たちは形式知の部分を特徴量生成として埋め込むだけで良い性能を得ることができる。数式に落とし込むことが難しい暗黙知の部分はとりあえず出来合いのものを使って、それ以外の部分だけをカスタマイズするような使い方をしている形になる。よってモデル作成の手順としてはまずXgboostや Neural Network など様々な出来合いのモデルを使っていまモデリングをしているデータの暗黙知に合うモデルを選択し、そのあとに可能な限りデータに関する形式知を使って特徴量生成を行うという手順になる。出来合いのモデルを使っている部分は暗黙知を表現したものなのであまり検証はできないが、特徴量については形式知を表現したものなので検証ができる。
