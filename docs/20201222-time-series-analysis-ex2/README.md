# 計量時系列分析の2章の数値計算

引き続き次の本を読んでいる。
- [経済・ファイナンスデータの計量時系列分析](https://www.amazon.co.jp/dp/4254127928)、	沖本竜義著

今回は2章の演習問題のうち、数値計算部分を次の記事を参考にしながら解いてみる。
- [【第2章】pythonで「経済・ファイナンスデータの計量時系列分析」の章末問題を解く](https://qiita.com/mckeeeen/items/a0126a20116dd27ecba9)


## 問題2.5
データは引き続き以下の記事でダウンロードしたものを使う
- [計量時系列分析の1章の数値計算](/20201222-time-series-analysis-ex1/)


まずはindprodの対数差分系列の標本自己相関と標本偏自己相関関数を計算する。
```
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.stattools import acf, pacf

data = pd.read_excel('economicdata.xls')
data.rename(columns={'Unnamed: 0': 'date'}, inplace=True)

indprod_cr = np.diff(np.log(data.indprod.values))

acf_ind = acf(indprod_cr, nlags=20)
pacf_ind = pacf(indprod_cr, nlags=20)

_, ax = plt.subplots(nrows=2, ncols=1)
ax[0].bar(np.arange(len(acf_ind[1:])), acf_ind[1:])
ax[0].set_title('acf')
ax[1].bar(np.arange(len(pacf_ind[1:])), pacf_ind[1:])
ax[1].set_title('pacf')
plt.tight_layout()
plt.savefig('figure-2-5-1.png')
plt.close()
```

<img src="/20201222-time-series-analysis-ex2/figure-2-5-1.png">

次に、AR(4)モデルとARMA(1,2)モデルの、モデル残差のLjung-BoxのQ統計量とそのp値を計算する。
```
from statsmodels.tsa.arima_model import ARMA

ar_4 = ARMA(indprod_cr, [4, 0]).fit()
arma_1_2 = ARMA(indprod_cr, [1, 2]).fit()

_, ar_4_qvalues, ar_4_pvalues = acf(ar_4.resid, qstat=True, nlags=10)
_, arma_1_2_qvalues, arma_1_2_pvalues = acf(arma_1_2.resid, qstat=True, nlags=10)

_, ax = plt.subplots(nrows=2, ncols=1)
ax[0].plot(ar_4_pvalues)
ax[0].set_title('ar_4_pvalues')
ax[1].plot(arma_1_2_pvalues)
ax[1].set_title('arma_1_2_pvalues')
plt.tight_layout()
plt.savefig('figure-2-5-2.png')
plt.close()
```

<img src="/20201222-time-series-analysis-ex2/figure-2-5-2.png">

自己相関がないという帰無仮説に対してP値が大きいので、その帰無仮説を棄却することができない。よってAR(4)モデルとARMA(1,2)モデルのどちらに対しても、この検定においては特に矛盾は検出されない。

## 問題2.6
標本自己相関と標本偏自己相関を計算する。
```
data = pd.read_excel('arma.xls')
acf_y1 = acf(data.y1.values, nlags=41)[1:]
pacf_y1 = pacf(data.y1.values, nlags=41)[1:]
confint = 1.96/np.sqrt(len(data.y1.values))

_, ax = plt.subplots(nrows=2, ncols=1)
ax[0].bar(np.arange(len(acf_y1)), acf_y1)
ax[0].hlines([-confint, confint], 0, 40, linestyles='dashed')
ax[0].set_title('acf_y1')
ax[1].bar(np.arange(len(pacf_y1)), pacf_y1)
ax[1].hlines([-confint, confint], 0, 40, linestyles='dashed')
ax[1].set_title('pacf_y1')
plt.tight_layout()
plt.savefig('figure-2-6-1.png')
plt.close()
```

<img src="/20201222-time-series-analysis-ex2/figure-2-6-1.png">

標本自己相関が徐々に減少しているのに対して標本偏自己相関は差が3程度までしか値がない。

よって、候補としてはAR(p)過程なので、幾つかのpに対して推定をしてAICとSICを比べてみる。
```
aics = list()
sics = list()
prange = range(2, 9)
for p in prange:
  model = ARMA(data.y1.values, [p, 0]).fit()
  aics.append(model.aic)
  sics.append(model.bic)

_, ax = plt.subplots(nrows=2, ncols=1)
ax[0].plot(prange, aics)
ax[0].set_title('aic')
ax[1].plot(prange, sics)
ax[1].set_title('sic')
plt.tight_layout()
plt.savefig('figure-2-6-2.png')
plt.close()
```

<img src="/20201222-time-series-analysis-ex2/figure-2-6-2.png">

両方の指標を考慮すると$p=3$が最適となりそうだ。

AR(3)過程に対する残差のLjung-BoxのQ統計量とそのp値を計算する。
```
model = ARMA(data.y1.values, [3, 0]).fit()
acfvalues, qvalues, pvalues = acf(model.resid, qstat=True, nlags=20)
```

`pvalues`の値は大体0.8程度となり、残差の自己相関が存在するとは言えない。よってAR(3)モデルが妥当でない根拠はない。
