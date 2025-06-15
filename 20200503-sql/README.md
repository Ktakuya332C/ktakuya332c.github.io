# 少し複雑なSQLクエリ

こんな記事を見つけた}

- [The best medium-hard data analyst SQL interview quetions](https://quip.com/2gwZArKuWk7W)

紹介されているクエリはすぐには思いつかなさそうなものばかりだったので、手元で少し試してみようと思う。

## 事前準備

とりあえずMySQLを使って試してみようと思うので、MySQLをインストールして実行してみる。

```
$ brew install mysql
$ mysql.server start
$ mysql -u root
mysql> CREATE DATABASE example;
mysql> USE example;
```

使えることは確認できた。

## MoM Percent Change

実際に試してみるためにデータを用意する。

```
$ vim gen.py
$ cat gen.py
import datetime
import random
fout = open('data.csv', 'w')
n_users = 10000
dau_max = 5000
cur_date = datetime.date(2019, 1, 1)
end_date = datetime.date(2020, 1, 1)
buf = ''
buf_max = 10000
while cur_date < end_date:
    date_str = cur_date.strftime('%Y-%m-%d')
    dau = random.randint(0, dau_max)
    users = random.sample(range(n_users), dau)
    for user in users:
        fout.write(f'{user},{date_str}\n')
    cur_date += datetime.timedelta(days=1)
fout.close()
$ python gen.py
$ mysql -u root
mysql> USE example;
mysql> CREATE TABLE logins (
user_id INT NOT NULL,
date DATE NOT NULL
);
mysql> LOAD DATA INFILE 'path/to/data.csv'
INTO TABLE logins
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';
mysql> SELECT * FROM logins LIMIT 2;
+---------+------------+
| user_id | date       |
+---------+------------+
|    7511 | 2019-01-01 |
|    8744 | 2019-01-01 |
+---------+------------+
```

データはできた。

今回の課題はMAUの変化を見ること。とりあえず回答例をMySQLに書き直してみる。

```
WITH maus AS (
  SELECT
    MONTH(date) AS month,
    COUNT(DISTINCT user_id) AS mau
  FROM
    logins
  GROUP BY
    month
)
SELECT
  prev.month AS previous_month,
  next.month AS next_month,
  (next.mau - prev.mau) / prev.mau AS mom
FROM
  maus AS prev
INNER JOIN
  maus AS next
ON
  prev.month = next.month - 1
;
```

実行してみると

```
+----------------+------------+---------+
| previous_month | next_month | mom     |
+----------------+------------+---------+
|              1 |          2 |  0.0001 |
|              2 |          3 |  0.0002 |
|              3 |          4 | -0.0004 |
|              4 |          5 |  0.0004 |
|              5 |          6 | -0.0002 |
|              6 |          7 |  0.0002 |
|              7 |          8 | -0.0001 |
|              8 |          9 | -0.0002 |
|              9 |         10 |  0.0000 |
|             10 |         11 |  0.0003 |
|             11 |         12 |  0.0000 |
+----------------+------------+---------+
```

となった。データの作り方的に毎月ほとんど同じMAUになってしまっていたのが残念だが、とりあえず計算はできた。

## Tree Structure Labeling

まずはデータの準備から行う。今回はデータが大きくても確認しづらいだけなので、適当に手で作成する。

```
$ vim data.csv
$ cat data.csv
1,2
2,5
3,5
4,3
5,NULL
$ mysql -u root
mysql> USE example;
mysql> CREATE TABLE tree (
node INT NOT NULL,
parent INT
);
mysql> LOAD DATA INFILE 'path/to/data.csv'
INTO TABLE tree
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(node, @parent)
SET parent = NULLIF(@parent, '');
mysql> SELECT * FROM tree;
+------+--------+
| node | parent |
+------+--------+
|    1 |      2 |
|    2 |      5 |
|    3 |      5 |
|    4 |      3 |
|    5 |   NULL |
+------+--------+
```

今回の目的はそれぞれのノードをLeafとInnerとRootにラベルづけすること。

```
WITH join_table AS (
  SELECT
    cur.node,
    cur.parent,
    COUNT(next.node) AS n_child
  FROM
    tree AS cur
  LEFT OUTER JOIN
    tree AS next
  ON
    cur.node = next.parent
  GROUP BY
    cur.node,
    cur.parent
)
SELECT
  node,
  CASE
    WHEN parent IS NULL THEN 'Root'
    WHEN n_child = 0 THEN 'Left'
    ELSE 'Inner'
  END AS label
FROM
  join_table
;
```

クエリの結果は次のようになった。

```
+------+-------+
| node | label |
+------+-------+
|    2 | Inner |
|    5 | Root  |
|    3 | Inner |
|    1 | Left  |
|    4 | Left  |
+------+-------+
```

確かにきちんとラベルづけできていそう。

## Retained users per month

対象の月と前の月に連続してログインしているユーザーの数を計算する。

```
WITH logins_month AS (
  SELECT
    MONTH(date) AS month,
    user_id
  FROM
    logins
)
SELECT
  current.month AS month,
  COUNT(DISTINCT current.user_id) AS n_retained
FROM
  logins_month AS current
LEFT JOIN
  logins_month AS prev
ON
  current.user_id = prev.user_id
  AND current.month = prev.month + 1
GROUP BY
  current.month
;
```

クエリの書き方が悪かったのか、投げても結果が返ってこない。@incode{DISTINCT}が悪いのかなと思ってそれを取ってみてもうまく動かないので原因は良く分からない。

## その他

その他にもいくつか問題が書いてあるので、気になったらやってみても面白そうだが、今回はそろそろ飽きてきたのでここまでにしておくことにする。どの例も実際に使いそうなクエリ例だったので、単に索引としても使えそうな気がした。
