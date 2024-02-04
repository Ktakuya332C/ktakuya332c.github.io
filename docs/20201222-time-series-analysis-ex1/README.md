# 計量時系列分析の1章の数値計算

次の本を読んでいる。
- [経済・ファイナンスデータの計量時系列分析](https://www.amazon.co.jp/dp/4254127928)、	沖本竜義著

今回は1章の演習問題のうち、数値計算部分を次の記事を参考にしながら解いてみる。
- [【第1章】pythonで「経済・ファイナンスデータの計量時系列分析」の章末問題を解く](https://qiita.com/mckeeeen/items/666e14c94e1548130646)


## 問題1.5
まずはデータをダウンロードしてくる。書かれているリンクからはデータが取得できないので、次のページからダウンロードする。
- [朝倉書店｜経済・ファイナンスデータの 計量時系列分析](http://www.asakura.co.jp/books/isbn/978-4-254-12792-8/)


### 問題(1)
まずはそれぞれのデータを単純にプロットしていく。
```
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_excel('economicdata.xls')
data.rename(columns={'Unnamed: 0': 'date'}, inplace=True)

_, ax = plt.subplots(nrows=3, ncols=2)
for i in range(3):
  for j in range(2):
    idx = 2*(i+1) + j
    ax[i, j].plot(data.iloc[:,idx])
    ax[i, j].set_title(data.columns[idx])
plt.subplots_adjust(wspace=0.2, hspace=0.6)
plt.savefig('figure-1-5-1.png')
plt.close()
```

<img src="/20201222-time-series-analysis-ex1/figure-1-5-1.png">

### 問題(2)と(3)
topix、exrate、indprodの対数差分系列を計算する。
```
import numpy as np

date = data.date.values[1:]
topix_cr = np.diff(np.log(data.topix.values))
exrate_cr = np.diff(np.log(data.exrate.values))
indprod_cr = np.diff(np.log(data.indprod.values))

_, ax = plt.subplots(nrows=3, ncols=1)
ax[0].plot(date, topix_cr)
ax[0].set_title('topix')
ax[1].plot(date, exrate_cr)
ax[1].set_title('exrate')
ax[2].plot(date, indprod_cr)
ax[2].set_title('indprod')
plt.subplots_adjust(hspace=0.6)
plt.savefig('figure-1-5-2.png')
plt.close()
```

<img src="/20201222-time-series-analysis-ex1/figure-1-5-2.png">

### 問題(4)
まずは標本自己相関をプロットする
```
from statsmodels.tsa.stattools import acf
autocorr, confint, qstat, pvalues = acf(indprod_cr, nlags=20, qstat=True, alpha=0.95)
plt.bar(np.arange(20), autocorr[1:])
plt.savefig('figure-1-5-4-1.png')
plt.close()
```

<img src="/20201222-time-series-analysis-ex1/figure-1-5-4-1.png">

次にLjung-BoxのQ統計量とそのp値をプロットする。
```
_, ax = plt.subplots(nrows=2, ncols=1)
ax[0].plot(qstat)
ax[0].set_title('Q-value')
ax[1].plot(pvalues)
ax[1].set_title('p-value')
plt.subplots_adjust(hspace=0.3)
plt.savefig('figure-1-5-4-2.png')
plt.close()
```

<img src="/20201222-time-series-analysis-ex1/figure-1-5-4-2.png">

常にp値は$10^{-8}$程度であり自己相関がないという帰無仮説は棄却できる。
