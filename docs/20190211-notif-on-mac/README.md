# Macで簡単に定期通知をする

座りっぱなしは良くないので、Mac上で一時間に一回くらいお知らせをしてくれるようなアプリがないかなと探していたら、デフォルトの機能で簡単にできることがわかったのでメモ。主にこのページを参考にしている。

- [MACにオリジナルの通知アラートを設定!遊びながらcrontabの使い方を習得しよう](https://liginc.co.jp/295876)


デスクトップへの通知はosascriptと呼ばれるコマンドを使えばいいらしい。基本的には Apple Script を呼び出すためのコマンドらしいのだが、とりあえず気にせず使ってみる。Terminalで次のコマンドを打つと、確かに右上からnotificationが出てくる。

```
$ osascript -e 'display notification "一時間経ちました" with title "お疲れ様です"'
```


これをcrontabに設定してしまえば良いらしい。とりあえず座っていることの多い時間帯、10時から18時まで一時間に一回通知をしてみよう

```
$ crontab -e
$ crontab -l
0 10-18 * * * osascript -e 'display notification "一時間経ちました" with title "お疲れ様です"' > /tmp/hourly-notification.log 2>&1
```


これで10時から18時の間毎時通知がくるはず。このnotificationで座りっぱなしが解消されればありがたい。
