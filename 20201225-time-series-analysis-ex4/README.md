# 計量時系列分析の4章の数値計算

引き続き次の本を読んでいる。

- [経済・ファイナンスデータの計量時系列分析](https://www.amazon.co.jp/dp/4254127928)、 沖本竜義著

今回は4章の演習問題のうち、数値計算部分を次の記事を参考にしながら解いてみる。

- [【第4章】pythonで「経済・ファイナンスデータの計量時系列分析」の章末問題を解く](https://qiita.com/mckeeeen/items/4afa1167008c1f315d0b)

## 問題4.5

### データの取得

データは以前と同じく

- [朝倉書店｜経済・ファイナンスデータの 計量時系列分析](http://www.asakura.co.jp/books/isbn/978-4-254-12792-8/)

からダウンロードしてきて使用する。

```
import pandas as pd
data = pd.read_excel('msci_day.xls')
data = data[['Date', 'jp', 'uk', 'us']]
```

まずは変化率の列を作成する。

```
import numpy as np
from matplotlib import pyplot as plt

data['jp_cr'] = np.log(data['jp']).diff()
data['uk_cr'] = np.log(data['uk']).diff()
data['us_cr'] = np.log(data['us']).diff()
data.dropna(inplace=True)

_, ax = plt.subplots(nrows=3, ncols=1)
ax[0].plot(data.Date, data.jp_cr)
ax[0].set_title('jp_cr')
ax[1].plot(data.Date, data.uk_cr)
ax[1].set_title('uk_cr')
ax[2].plot(data.Date, data.us_cr)
ax[2].set_title('us_cr')
plt.tight_layout()
plt.savefig('figure-4-5-1.png')
plt.close()
```

<img src="/20201225-time-series-analysis-ex4/figure-4-5-1.png" alt="figure-4-5-1">

定常的に見えるのでVAR関連の分析を行うことができそう。

これ以降VARモデルの当てはめをする際にはdataframeのindexをtimeseriesに変換しておく必要がある。

```
data.index = pd.DatetimeIndex(data.Date)
data.drop(columns='Date', inplace=True)
```

### VARモデルの推定

変化率のデータを使ってVARモデルの推定を行う。

```
from statsmodels.tsa.vector_ar.var_model import VAR

aics = list()
for p in range(1, 11):
  model = VAR(data[['jp_cr', 'uk_cr', 'us_cr']], dates=data['Date'], freq='B').fit(maxlags=p)
  aics.append(model.aic)

plt.plot(np.arange(1, 11), aics)
plt.savefig('figure-4-5-2.png')
plt.title('AIC')
plt.close()
```

<img src="/20201225-time-series-analysis-ex4/figure-4-5-2.png" alt="figure-4-5-2">

AICが一番低いのはVAR(4)かVAR(6)あたりという感じになりそう。

### グレンジャー因果の検定

教科書と同じVAR(3)モデルを今一度推定する。

```
model = VAR(data[['jp_cr', 'uk_cr', 'us_cr']], dates=data['Date'], freq='B').fit(maxlags=3)
```

この結果を使ってグレンジャー因果を検定してみる。

```
uk2jp = model.test_causality('jp_cr', 'uk_cr', kind='f', signif=0.05)
uk2jp.test_statistic // 12.012495863151996
uk2jp.pvalue // 7.917449229649696e-08
```

再現できていそう。

### インパルス応答関数

```
model.irf(periods=10).plot()
plt.savefig('figure-4-5-3.png')
plt.close()
```

<img src="/20201225-time-series-analysis-ex4/figure-4-5-3.png" alt="figure-4-5-3">

全体的な傾向は教科書とかは変わらなさそうだが、細かい計算結果はだいぶ異なる様に見える。

### 相対的分散寄与率

```
model.fevd(periods=10).plot()
plt.savefig('figure-4-5-4.png')
plt.close()
```

<img src="/20201225-time-series-analysis-ex4/figure-4-5-4.png" alt="figure-4-5-4">

## 問題4.6

問題4.6でやることは問題4.5でやることとほぼ同じなので、わざわざ繰り返すことはしない。
