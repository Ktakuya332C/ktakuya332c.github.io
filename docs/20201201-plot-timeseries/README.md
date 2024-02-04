# 色々な時系列データをプロットしてみる

次の本を読み始めている。
- [経済・ファイナンスデータの計量時系列分析](https://www.amazon.co.jp/dp/4254127928)

この本の最初の方に幾つかの時系列の例を出しているページがあり、読み進めていくにあたって実際に計算してみることのできる対象があると良さげだったので、実際にそれらのデータを取得して、プロットまでやってみることにした。

この本では例としてTOPIX、実効為替レート、鉱工業生産指数、CPI、失業率、コールレートの6つが挙げられていた。今回はTOPIXのデータは残念ながら無料で何の登録もなしにデータを取得できるサイトが見つからなかったので、今回の対象からは除くことにし、それ以外の5つの時系列をプロットしてみることにした。ちなみにTOPIXのデータも、取得しようと思えば、QuandlやYahooFiananceなど登録は必要だが無料でデータを取得できるAPIはいくつか存在する様子。

## 実効為替レート
実効為替レートは次のサイトから取得することができた。
- [主要時系列統計データ表](https://www.stat-search.boj.or.jp/ssi/mtshtml/fm09_m_1.html)、日本銀行

ダウンロードボタンを押してダウンロードしてきたファイルの拡張子はcsvだが、実際の中身はcsvになっていないので、まずはファイルを適当に書き換える
```
$ tail -n +10 fm09_m_1.csv | sponge fm09_m_1.csv
$ (echo 'Date,Nominal,Real' && cat fm09_m_1.csv) | sponge fm09_m_1.csv
```

とりあえず名目実効為替レート指数をプロットしてみる。
```
library(tidyverse)
library(lubridate)

data <- read_csv('fm09_m_1.csv')
plot <- data %>%
  mutate(Date = parse_date_time(Date, '%y/%m')) %>%
  ggplot(aes(Date, Nominal)) +
  geom_line(alpha=0.8)
ggsave('effective_exchange_rate.png', plot)
```

<img src="/20201201-plot-timeseries/effective_exchange_rate.png">

## 鉱工業生産指数
鉱工業生産指数はこのページから取得することができた。
- [関東地域の鉱工業生産動向](https://www.kanto.meti.go.jp/tokei/kokogyo/jikeiretsu.html)、関東経済産業局

全国の値を見つけようと思ったのだが見つけることができなかったので、関東地域のデータを使っている。

月次の季節調整済みの指数のデータをダウンロードして中身を見てみると、やはり中身は単純なテーブルデータにはなっていない様なので、注目したい値だけ手で取り出して別のcsvに書き込んだあと、プロットしてみる。
```
library(tidyverse)
library(lubridate)

data <- read_csv('mineral_industry_production_index.csv', col_types=&quot;cd&quot;)
plot <- data %>%
  mutate(Date = parse_date_time(Date, '%y%m')) %>%
  ggplot(aes(Date, Index)) +
  geom_line(alpha=0.8)
ggsave('mineral_industry_production_index.png', plot)
```

Covid19が流行った後も入っている様なので時系列の最後がものすごく落ち込んでいる様子。
<img src="/20201201-plot-timeseries/mineral_industry_production_index.png">

## 消費者物価指数(CPI)
このページから取得することができた。
- [2015年基準消費者物価指数](https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200573&tstat=000001084976&cycle=1&year=20200&month=11010301&tclass1=000001085955&stat_infid=000031911465&result_back=1&tclass2val=0)

やはりテーブルデータの形になっていないので、ダウンロードしてきたExcelファイルから目的の内容だけ手で取り出してcsvにしておく。今回の場合更に年月が昭和や平成で書かれているので、それも西暦に変換する。
```
data <- read_csv('customer_price_index.csv', col_types=&quot;cd&quot;)
plot <- data %>%
  mutate(Date = parse_date_time(Date, '%y-%m')) %>%
  ggplot(aes(Date, Index)) +
  geom_line(alpha=0.8)
ggsave('customer_price_index.png', plot)
```

<img src="/20201201-plot-timeseries/customer_price_index.png"></figure>

## 失業率
このページから取得できた
- [労働力調査　長期時系列データ](http://www.stat.go.jp/data/roudou/longtime/03roudou.html)、総務省統計局

長期時系列データの主要項目のデータをダウンロードしてきて、完全失業率の男女合計の項目を、毎度のことながら適当に整形する。
```
data <- read_csv('unemployment_rate.csv', col_types=&quot;cd&quot;)
plot <- data %>%
  mutate(Date = parse_date_time(Date, '%y-%m')) %>%
  ggplot(aes(Date, UnemploymentPercent)) +
  geom_line(alpha=0.8)
ggsave('unemployment_rate.png', plot)
```

<img src="/20201201-plot-timeseries/unemployment_rate.png">

## コールレート
このページから取得できた
- [主要時系列統計データ表](https://www.stat-search.boj.or.jp/ssi/mtshtml/fm02_m_1.html)、日本銀行

ダウンロードしてきて整形する。
```
data <- read_csv('fm02_m_1.csv')
plot <- data %>%
  mutate(Date = parse_date_time(Date, '%y/%m')) %>%
  ggplot(aes(Date, EndOfMonth)) +
  geom_line(alpha=0.8)
ggsave('call_rate.png', plot)
```

<img src="/20201201-plot-timeseries/call_rate.png">

## その他
とりあえず色々な政府機関のサイトを漁って、エクセルを手で整形し続ければ、問題なくデータが得られることはわかった。
