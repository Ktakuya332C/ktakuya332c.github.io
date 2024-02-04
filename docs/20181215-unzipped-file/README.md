# Unzipされたファイルのpermission

kaggleからzip化されたトレーニングデータ`train.csv.zip`をダウンロードしてきて、次のようにunzipして

```
$ unzip train.csv.zip
```


Rから読み込もうとしたところエラーが出た。

```
> library(data.table)
> tr <- fread("../input/train.csv")
Error in fread("../input/train.csv") : file not found: ../input/train.csv
```


少なくともパスが間違ってはいないことは

```
> list.files("../input")
[1] "sample_submission.csv.zip"
[2] "test.csv"
[3] "test.csv.zip"
[4] "train.csv"
[5] "train.csv.zip"
```


などとして確かめたので別の原因のはずだ。

少し調べたところ、なんてことはなく単純にunzipされたファイルのpermissionが適切に設定されていないだけだった。

```
$ ls -l
total 19139328
-rw-r--r--  1 ktakuya  staff   140766935 Dec 14 21:50 sample_submission.csv.zip
----------  1 ktakuya  staff  3795687226 Dec 11 15:03 test.csv
-rw-r--r--  1 ktakuya  staff   674683523 Dec 14 21:55 test.csv.zip
----------  1 ktakuya  staff  4384966482 Dec 11 15:03 train.csv
-rw-r--r--@ 1 ktakuya  staff   771141062 Dec 14 22:01 train.csv.zip
```


なのでpermissionを適切に設定して

```
$ chmod 644 train.csv
```


再度Rから読み込めば、読み込めた。

```
> tr <- fread("../input/train.csv")
|--------------------------------------------------|
|==================================================|
|--------------------------------------------------|
|==================================================|
```
