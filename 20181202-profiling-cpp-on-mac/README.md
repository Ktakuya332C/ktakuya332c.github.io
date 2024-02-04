# C++のCUIコードをMacでプロファイリングする

C++で作成したCUIのコードをMacでプロファイリングする方法を調べたので、一応メモしておく。

C/C++で作成したコードをMacでプロファイリングするには、`instruments`コマンドを使用する。C/C++のコードをコンパイルしたのちの実行ファイルを`a.out`として、

```
$ ls
a.out
$ instruments -t "Time Profiler" ./a.out
```


とすれば同じディレクトリに`instrumentscli0.trace`などの、プロファイリング結果が書かれたファイルが生成される。これを

```
$ ls
instrumentscli0.trace
$ open instrumentscli0.trace
```


としてひらけばGUIのinstrumentsアプリが開いて、プロファイリング結果を見ることができる。

ちなみにGoogleでC++をMacでプロファイリングすると検索すると、iprofilerコマンドを使用してプロファイリングする方法が出てくるが、新しめのMacでは[使えなくなっている](http://watson.hatenablog.com/entry/2017/10/03/235305)様子。
