# Covid19の新規感染者数

寒いと風邪は流行りやすいが、Covid19も流行りやすいという話をよく聞く。本当かどうかを見てみるために実際にデータを取ってきてその相関関係を見てみようと思ったのだが、意外と新規感染者数のグラフを出すだけである程度時間が掛かってしまったので、そこで一旦終わりにすることにした。温度との相関はまた別の機会にグラフにしようと思う。

## Covid19の新規感染者数

まずはCovid19の新規感染者数の情報をどこかから持ってくる必要がある。今回は有名な次のデータソースを使うことにした。
- [COVID-19 Data Repository by the CSSE](https://github.com/CSSEGISandData/COVID-19)

今回は国別の感染者数がわかればそれで良い。
```
$ REPO=https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master
$ RPATH=csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
$ wget -q $REPO/$RPATH
$ r
> library(tidyverse)
> library(lubridate)
> data <- read_csv(`time_series_covid19_confirmed_global.csv`)
> data <- data %>%
  mutate(Province = replace_na(`Province/State`, `All`)) %>%
  mutate(Region = paste(Province, `Country/Region`)) %>%
  select(-`Province/State`, -`Country/Region`, -Province)
```

とりあえず国別の新規感染者数をグラフにしてみる。
```
> library(zoo)
> notable_regions <- data %>%
  top_n(10, wt=`11/28/20`) %>%
  select(`Region`) %>%
  deframe
> notables <- data %>% filter(Region %in% notable_regions)
> new_cases <- notables %>%
  select(-Lat, -Long) %>%
  gather(key=Date, value=Cases, -Region) %>%
  mutate(Date = mdy(Date)) %>%
  group_by(Region) %>%
  mutate(LagCases = lag(Cases)) %>%
  drop_na(LagCases) %>%
  mutate(NewCases = Cases - LagCases) %>%
  select(-Cases, -LagCases)
> smoothed_new_cases <- new_cases %>%
  group_by(Region) %>%
  mutate(NewCases7Ave = rollmean(NewCases, k=7, fill=NA)) %>%
  drop_na(NewCases7Ave)
> plot <- ggplot(smoothed_new_cases, aes(Date, NewCases7Ave, color=Region)) +
  geom_line()
> ggsave(`new_cases.png`, plot)
```

<img src="/20201129-covid19/new_cases.png"></figure>

## 温度のデータ

温度のデータとしては次のサイトの情報が使えそうだった。
- [Open Weather](https://openweathermap.org/)

無料でも提供されているAPIを一秒に一回程度までなら叩いても良いらしいので十分に使えるはず。

ちょうど先のデータに経度と緯度の情報が含まれていたので、その情報を使って例えば次のAPIを叩けば
- [Historical weather API](https://openweathermap.org/history)

温度のデータは取れるはず。もちろんその時期の平均などとなると大変だが、簡単にみるだけならその日のデータを取ってくるだけでもある程度の傾向は見ることができるはず。

## 参考
1. [How to calculate a rolling average in R](https://www.storybench.org/how-to-calculate-a-rolling-average-in-r/)
