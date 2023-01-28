Unzipされたファイルのpermission
2018-12-15

@p{kaggleからzip化されたトレーニングデータ@incode{train.csv.zip}をダウンロードしてきて、次のようにunzipして}

@blcode{
$ unzip train.csv.zip
}

@p{Rから読み込もうとしたところエラーが出た。}

@blcode{
> library(data.table)
> tr <- fread("../input/train.csv")
Error in fread("../input/train.csv") : file not found: ../input/train.csv
}

@p{少なくともパスが間違ってはいないことは}

@blcode{
> list.files("../input")
[1] "sample_submission.csv.zip"
[2] "test.csv"
[3] "test.csv.zip"
[4] "train.csv"
[5] "train.csv.zip"
}

@p{などとして確かめたので別の原因のはずだ。}

@p{少し調べたところ、なんてことはなく単純にunzipされたファイルのpermissionが適切に設定されていないだけだった。}

@blcode{
$ ls -l
total 19139328
-rw-r--r--  1 ktakuya  staff   140766935 Dec 14 21:50 sample_submission.csv.zip
----------  1 ktakuya  staff  3795687226 Dec 11 15:03 test.csv
-rw-r--r--  1 ktakuya  staff   674683523 Dec 14 21:55 test.csv.zip
----------  1 ktakuya  staff  4384966482 Dec 11 15:03 train.csv
-rw-r--r--@ 1 ktakuya  staff   771141062 Dec 14 22:01 train.csv.zip
}

@p{なのでpermissionを適切に設定して}

@blcode{
$ chmod 644 train.csv
}

@p{再度Rから読み込めば、読み込めた。}

@blcode{
> tr <- fread("../input/train.csv")
|--------------------------------------------------|
|==================================================|
|--------------------------------------------------|
|==================================================|
}
