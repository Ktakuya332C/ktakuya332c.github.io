# DL関連文献調査

最近一年くらい deep learning 関連の文献を漁っていなかったので久しぶりに見てみる。フォーマットとしては、なぜかよくみる[落合教授の論文まとめフォーマット](http://lafrenze.hatenablog.com/entry/2015/08/04/120205)に沿ってまとめていくことにする。あまり他の人が読むようには書いていないが、消えてしまうのももったいない気がしたのでここで供養しておく。

> *BERT: Pre-training of Deep Bidirectional Transformers for　Language Understanding*  
> - どんなもの?
>   - 言語モデルにおけるあるpre-trainedモデルを作成した
> - 先行研究と比べてどこがすごい?
>   - いくつもの精度指標でstate-of-artを達成した
> - 技術や手法のキモはどこ?
>   - GPTなどの既存手法が一方向に文章を読み込むモデルなのに対して、文章中の単語を周囲のコンテクストから予測するようにモデルを変更することで性能を向上することができた点。
> - どうやって有効だと検証した?
>   - すでに存在する検証用データセットで検証
> - 議論はある?
> - 次に読むべき論文は?



> *Efficient Net: Rethinking Model Scaling for Convolutional Neural Networks*  
> - どんなもの?
>   - 畳み込みニューラルネットワークのサイズを大きくする際の指針を示している
> - 先行研究と比べてどこがすごい?
>   - サイズを大きくする際の指針を体系的な調査によって導き出している点
> - 技術や手法のキモはどこ?
>   - 深さと解像度を色々な値で止めたまま画像幅を変化させると、深さと解像度が同じくらいの時に最も精度が良くなったという観察から同じスケーリングをした方が良いのではないかと思いついたとある。
> - どうやって有効だと検証した?
>   - 様々なタスクでこのサイズの変更方法と他の方法を比べることによって検証した
> - 議論はある?
>   - 実験による観察から導かれた経験則である点が少し懸念
> - 次に読むべき論文は?


> *Big Transfer (BiT): General Visual Representation Learning*  
> - どんなもの?
>   - 画像認識におけるBERTにあたるpre-trainedモデルの作成
> - 先行研究と比べてどこがすごい?
>   - 多くのタスクでの精度が驚異的
> - 技術や手法のキモはどこ?
>   - 単純にpre-train時の学習データを多く使用しモデルサイズを大きくした
>   - pre-train時に Group Normalization と Weight Standardization を使用していること
>   - train時にMixUp正則化を使用していること
> - どうやって有効だと検証した?
>   - モデルサイズ、Group Normalization、Weight Standardiztion をそれぞれ変化させた時のパフォーマンスを比較した。
> - 議論はある?
>   - ILSVRC-2012のデータに対してもすでにラベリングのミスなどによって精度が下がっている可能性がある
> - 次に読むべき論文は?
>   - Group Normalization
>   - Weight standardization
>   - Fixing the train-test resolution discrepancy
>   - RetinaNet: Focal Loss for Dense Object Detection</pre></div>


> *Group Normalization*  
> - どんなもの?
>   - batch norm の計算コストを削減した group norm の提案
> - 技術や手法のキモはどこ?
>   - instance norm や layer norm とは異なり、channel方向にgroupingをして、それぞれに対して normalizationをかけている点
> - どうやって有効だと検証した?
>   - batch size を変化させて batch norm と group norm を比較することで検証
> - 議論はある?
>   - group size が32と定められているが、それが良いかどうかは不明
> - 次に読むべき論文は?


> *Weight standardization*  
> - どんなもの?
>   - batch size がとても小さくても group norm と使用すれば batch size が大きいときのパフォーマンスを上回ることのできる手法 weight standardization を提案
> - 技術や手法のキモはどこ?
>   - batch norm や group norm ではactivationに対して正規化をしていたが、この手法はweightに正規化をかける
> - どうやって有効だと検証した?
>   - 実際に幾つかのタスクで精度を検証する
>   - 理論的に予測される Lipshitz constant の減少を実験的に確かめる
> - 議論はある?
> - 次に読むべき論文は?
>   -  How does batch normalization help optimization?</pre></div>


> *Fixing the train-test resolution discrepancy*  
> - どんなもの?
>   - train時の data augmentation の方法を誤ると精度が逆に落ちることを示した
>   - その欠点を克服するようなネットワークの学習方法の提案
> - 技術や手法のキモはどこ?
>   - 写真を撮る際のメカニズムをざっくりとモデル化することでtrainとtestで対象物のサイズが異なって提示されてしまうことを指摘した
>   - その点に基づいて、train時における画像の random crop のサイズとtest時のcropサイズを少し変化させることで問題が消えることを示した
> - どうやって有効だと検証した?
>   - いくつかのスタンダードタスクでの精度が上昇することを見た
> - 議論はある?
> - 次に読むべき論文は?
>   - Aggregated Residual Transformations for Deep Neural Networks
>   - MultiGrain: a unified image embedding for classes and instances</pre></div>


> *Full-Gradient Representation for Neural Network Visualization*  
> - どんなもの?
>   - CNNに対する良い saliency map の作成方法FullGradを作成した
> - 技術や手法のキモはどこ?
>   - saliency map が満たすべき性質を weak dependence とcompletnessの二つとして明確に定義した
>   - 中間レイヤーのbiasのgradientをinputのgradientをどちらも考えることでそれらの性質を満たした
> - どうやって有効だと検証した?
>   - 重要だとFullGradが示したpixelを消して予測が変わるかどうか
>   - その他見分など
> - 議論はある?
> - 次に読むべき論文は?


> *Emergence of Object Segmentation in Perturbed Generative Models*  
> - どんなもの?
>   - 教師なしでsegmentationする方法を開発した
> - 技術や手法のキモはどこ?
>   - GANの手法を使ってbackgroundとtargetを分離させるような学習方法を提案したこと
> - どうやって有効だと検証した?
>   - visual inspection
> - 議論はある?
> - 次に読むべき論文は?
>   - A Style-Based Generator Architecture for Generative Adversarial Networks


> *A Style-Based Generator Architecture for Generative Adversarial Networks*  
> - どんなもの?
>   - style transfer 周辺領域の研究結果を援用してさらに現実的な画像を作成できるGANを作った
> - 技術や手法のキモはどこ?
>   - 通常のGANの生成部分のように latent space から直接画像を生成するのではなくて、latent space の情報を階層ごとに徐々に入れながら生成していく構造に変形させている点
> - どうやって有効だと検証した?
>   - 生成した画像を見て確認
>   - 画像の平均がそれらしいかを見て確認
>   - 言葉で表現できる特徴が latent space 上で線形に分離できるかどうか
> - 議論はある?
> - 次に読むべき論文は?
>   - GANs trained by a two time-scale update rule converge to a local Nash equilibrium


> *GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism*  
> - どんなもの?
>   - サイズが大きくてメモリに乗り切らないようなネットワークの学習を手助けする一般的なフレームワークを作成した
> - 技術や手法のキモはどこ?
>   - mini-batchをmicro-batchに分解して、一つのmini-batch内での計算を比較的並行に計算できるようにしたこと
> - どうやって有効だと検証した?
>   - 実際に大きいサイズのネットワークの学習を行なって速度を測ることで検証した
> - 議論はある?
> - 次に読むべき論文は?
