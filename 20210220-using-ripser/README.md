# Ripserを使ってパーシステント図を作る

次の本を読んだ。

- 平岡裕章著、[タンパク質構造とトポロジー](https://www.kyoritsu-pub.co.jp/bookdetail/9784320110021)

とりあえずパーシステント図を書いてみたくなったので、Ripserライブラリを使って書いてみた。

## 直線データ

とりあえずは簡単に2次元上の直線のデータを作ってみて

```
import numpy as np
from matplotlib import pyplot as plt

# データ生成
line = np.empty((100,2))
line[:,0] = np.linspace(0,1,100)
line[:,1] = np.linspace(0,1,100)
plt.scatter(line[:,0],line[:,1])
plt.savefig('line.png')
plt.close()
```

<img src="/20210220-using-ripser/line.png" width="60%" alt="line">

そのパーシステント図を書いてみる。

```
from ripser import Rips
rips = Rips()
diagrams = rips.fit_transform(line)
rips.plot(diagrams)
plt.savefig('line-ripser.png')
plt.close()
```

<img src="/20210220-using-ripser/line-ripser.png" width="60%" alt="line-risper">

このパーシステント図から読み取れることとしては以下の二つ。

- H0の要素が対角線から離れた左上にあるので、連結成分が存在する
- H1の要素が一つも生成されていないので一元ループは存在しない

確かにどちらも直線の特性に一致するが、同時にパーシステント図からは

- H0の要素が二つ存在し、連結成分が二つ存在する

ことになっており、こうなってしまっている原因はよくわからない。この線分の真ん中らへんで、数値誤差によって少し他より離れている点があり、その影響で二つの線分が認識されているのかもしれない。

## 円形データ

円形のデータを作ってみて

```
import numpy as np
from matplotlib import pyplot as plt

# データ生成
circle = np.empty((100,2))
thetas = np.linspace(0,2*np.pi,100)
circle[:,0] = np.cos(thetas)
circle[:,1] = np.sin(thetas)
plt.scatter(circle[:,0],circle[:,1])
plt.savefig('circle.png')
plt.close()
```

<img src="/20210220-using-ripser/circle.png" width="60%" alt="circle">

そのパーシステント図を書いてみる。

```
from ripser import Rips
rips = Rips()
diagrams = rips.fit_transform(circle)
rips.plot(diagrams)
plt.savefig('circle-ripser.png')
plt.close()
```

<img src="/20210220-using-ripser/circle-ripser.png" width="60%" alt="circle-ripser">

このパーシステント図から読み取れることとしては以下の二つ。

- H0の要素が1つ対角線から離れた位置にあるので、一つの連結成分が存在する
- H0の要素が1つ対角線から離れた位置にあるので、一つの一次元ループが存在する

今回は円形データの直感と合う結果が得られた。

## 二つの円データ

二つの円データを作ってみて

```
import numpy as np
from matplotlib import pyplot as plt

# データ生成
two_circles = np.empty((100,2))
thetas = np.linspace(0,2*np.pi,50)
two_circles[0:50,0] = np.cos(thetas) + 1
two_circles[0:50,1] = np.sin(thetas)
two_circles[50:100,0] = (np.cos(thetas) - 1) * 0.5
two_circles[50:100,1] = np.sin(thetas) * 0.5
plt.scatter(two_circles[:,0],two_circles[:,1])
plt.savefig('two-circle.png')
plt.close()
```

<img src="/20210220-using-ripser/two-circle.png" width="60%" alt="two circles">

そのパーシステント図を書いてみる。

```
from ripser import Rips
rips = Rips()
diagrams = rips.fit_transform(two_circles)
rips.plot(diagrams)
plt.savefig('two-circle-ripser.png')
plt.close()
```

<img src="/20210220-using-ripser/two-circle-ripser.png" width="60%" alt="two circle ripser">

このパーシステント図から読み取れることとしては以下の二つ。

- H0の要素が1つ対角線から離れた位置にあるので、一つの連結成分が存在する
- H0の要素が2つ対角線から離れた位置にあるので、二つの一次元ループが存在する

今回は円形データの直感と合う結果が得られた。

## 備考

- risperが含まれているscikit-tdaパッケージをインストールしたらいきなりコンパイルで落ちた。べつのTDAライブラリも似たような感じだったので、まともに使う時は自分で開発するかC++などで書かれているもう少しメンテナンスがしっかりしているものを使うべきかもしれない。
- 二つの円データを試す際には二つの円の半径をことなるようにしたが、同じ半径だとパーシステント図上で同じところに点が打たれてしまって二つの点を認識できない。ライブラリ側で少しくらいずらしてくれれば良いなと思いつつ、特に本質的ではないので今回は半径を異なるようにすることで対応した。
