C++のCUIコードをMacでプロファイリングする
2018-12-02

@p{C++で作成したCUIのコードをMacでプロファイリングする方法を調べたので、一応メモしておく。}

@p{C/C++で作成したコードをMacでプロファイリングするには、@incode{instruments}コマンドを使用する。C/C++のコードをコンパイルしたのちの実行ファイルを@incode{a.out}として、}

@blcode{
$ ls
a.out
$ instruments -t "Time Profiler" ./a.out
}

@p{とすれば同じディレクトリに@incode{instrumentscli0.trace}などの、プロファイリング結果が書かれたファイルが生成される。これを}

@blcode{
$ ls
instrumentscli0.trace
$ open instrumentscli0.trace
}

@p{としてひらけばGUIのinstrumentsアプリが開いて、プロファイリング結果を見ることができる。}

@p{ちなみにGoogleでC++をMacでプロファイリングすると検索すると、iprofilerコマンドを使用してプロファイリングする方法が出てくるが、新しめのMacでは@a{使えなくなっている}{http://watson.hatenablog.com/entry/2017/10/03/235305}様子。}