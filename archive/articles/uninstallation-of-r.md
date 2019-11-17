Rのuninstall方法
2018-12-14


自分の持っているMacOS上にRを公式サイトからpkgファイルを取ってきて導入した。そうして少し立った時に他の用事で\emp{brew doctor}をやったらひどいことになっていた。
\code{
$ brew doctor
Please note that these warnings are just used to help the Homebrew maintainers
with debugging if you file an issue. If everything you use Homebrew for is
working fine: please don't worry or file an issue; just ignore this. Thanks!

Warning: Unbrewed dylibs were found in /usr/local/lib.
If you didn't put them there on purpose they could cause problems when
building Homebrew formulae, and may need to be deleted.

Unexpected dylibs:
  /usr/local/lib/libtcl8.6.dylib
  /usr/local/lib/libtk8.6.dylib

Warning: Unbrewed header files were found in /usr/local/include.
If you didn't put them there on purpose they could cause problems when
building Homebrew formulae, and may need to be deleted.

Unexpected header files:
  /usr/local/include/fakemysql.h
  /usr/local/include/fakepq.h
  /usr/local/include/fakesql.h
  /usr/local/include/itcl.h
  /usr/local/include/itcl2TclOO.h
  /usr/local/include/itclDecls.h
  /usr/local/include/itclInt.h
  /usr/local/include/itclIntDecls.h
  /usr/local/include/itclMigrate2TclCore.h
  /usr/local/include/itclTclIntStubsFcn.h
  /usr/local/include/mysqlStubs.h
  /usr/local/include/odbcStubs.h
  /usr/local/include/pqStubs.h
  /usr/local/include/tcl.h
  /usr/local/include/tclDecls.h
  /usr/local/include/tclOO.h
  /usr/local/include/tclOODecls.h
  /usr/local/include/tclPlatDecls.h
  /usr/local/include/tclThread.h
  /usr/local/include/tclTomMath.h
  /usr/local/include/tclTomMathDecls.h
  /usr/local/include/tdbc.h
  /usr/local/include/tdbcDecls.h
  /usr/local/include/tdbcInt.h
  /usr/local/include/tk.h
  /usr/local/include/tkDecls.h
  /usr/local/include/tkPlatDecls.h

Warning: Unbrewed .pc files were found in /usr/local/lib/pkgconfig.
If you didn't put them there on purpose they could cause problems when
building Homebrew formulae, and may need to be deleted.

Unexpected .pc files:
  /usr/local/lib/pkgconfig/tcl.pc
  /usr/local/lib/pkgconfig/tk.pc

Warning: Unbrewed static libraries were found in /usr/local/lib.
If you didn't put them there on purpose they could cause problems when
building Homebrew formulae, and may need to be deleted.

Unexpected static libraries:
  /usr/local/lib/libtclstub8.6.a
  /usr/local/lib/libtkstub8.6.a
}
仕方ないので一度uninstallして、再度brewからインストールしようと思う。


uninstallは基本的には\a{このRの公式ページ}{https://cran.r-project.org/doc/manuals/r-release/R-admin.html#Uninstalling-under-macOS}に乗っている記事にしたがって削除して行けばいいはずだ。まずはR本体を消す
\code{
$ sudo rm -Rf /Library/Frameworks/R.framework /Applications/R.app \
   /usr/local/bin/R /usr/local/bin/Rscript
}
次にAppleパッケージを削除する。
\code{
$ sudo pkgutil --forget org.r-project.R.el-capitan.fw.pkg
$ sudo pkgutil --forget org.r-project.R.el-capitan.GUI.pkg
$ sudo pkgutil --forget org.r-project.x86_64.tcltk.x11
$ sudo pkgutil --forget org.r-project.x86_64.texinfo
}
あとはwarningに出ているファイルを全て消していくだけで良さそう。少なくともRを直接公式サイトのpkgファイルからインストールするまでは\emp{brew doctor}はなんのエラーも履いていなかったので、エラーが吐かれているファイルは全てRが原因だと思って良さそうなので。

これでやっと正常に戻った。
\code{
$ brew doctor
Your system is ready to brew.
}
