# javascriptのモジュール機構

javascriptのモジュールの機構として`require`だと`exports`だの同じようで少しづつ違いそうなコードをよくみるので、ここらでまとめてみる。

## commonJSとECMAScript

まずは最初のバージョンのJavascriptにはモジュールやそれに類する機能は存在しなかったという点を認識しておく必要がありそう。基本的にはHTMLの上でいくつかのjsファイルをscriptタグでロードしていく方法
```
<script src="lib1.js"></script>
<script src="lib2.js"></script>
```

でしか他のファイルに存在するjsのコードを参照する方法はなかったらしい[2]

ただしJavascriptは基本的にはブラウザー上で実行される言語だったので、普通のプログラミング言語のようにその開発者が一人でモジュールの作成方法を決めることができない。そこでいろいろな人がそこら中でJavascriptのモジュールはこのようにすると良いのではないかと考えて色々な仕様を策定し始めた結果、今でもそれなりに有名になっているのが次の二つの仕様ということらしい
- [commonJS](https://en.wikipedia.org/wiki/CommonJS)
- [ECMAScript](https://ja.wikipedia.org/wiki/ECMAScript)


commonJSはnodejsに基本的なモジュールの仕様として採用されたので、基本的にはサーバーサイドの開発で使われることになるモジュールの仕様となっているようす。ただし各種ブラウザーに採用されることがなかったので主にはサーバーサイドの開発用のモジュール構成となっている

ECMAScriptはブラウザにおけるJavascriptのモジュール仕様として採用されたようで、基本的には各種ブラウザーで使うことができる。ただし毎年新しいバージョンの仕様が発表されるので、その最新バージョンの仕様にどのブラウザーが追いついているかは逐一確認する必要がある。

ただしいずれにしろバージョンによってサポート状況が違ったりするので、結局は[Babel](https://babeljs.io/)や[Browsify](http://browserify.org/)などでtranspileして使うことが多く、そうなると結局どちらのモジュール仕様を使っても問題なくなり、結果的に色々なモジュールの使い方がmixされているコードを見ることがよくある。

## commonJSのモジュールの使い方

名前付きexportの場合は
```
$ vim module.js
$ cat module.js
const PI = 3.14;
exports.area = (r) => PI * r ** 2;
exports.circumference = (r) => 2 * PI * r;
$ vim index.js
$ cat index.js
const { area } = require('./module.js');
console.log(area(5));
$ node index.js
78.5
```

として使うことができる。
デフォルトexportの場合は
```
$ vim module.js
$ cat module.js
module.exports = class Square {
  constructor(width) {
    this.width = wdith;
  }
  area() {
    return this.width ** 2;
  }
}
$ vim index.js
$ cat index.js
const Square = require('./module.js');
const mySquare = new Square(2);
console.log(mySquare.area());
$ node index.js
4
```

となる。

## ECMAScriptのモジュールの使い方

nodejsでのサポートは十分ではないこともあるのでブラウザで試す。
名前付きexportの場合は
```
$ vim module.js
$ cat module.js
export function cube(x) {
  return x * x * x;
}
export function square(x) {
  return x * x;
}
$ vim index.html
$ cat index.html
<html>
  <head>
    <title>Example</title>
    <script type="module">
      import { square } from './module.js';
      const elem = document.getElementById('main');
      const valueSquare = square(2);
      const squareNode = document.createTextNode(`${valueSquare}`);
      elem.appendChild(squareNode);
    </script>
  </head>
  <body>
    <div id="main"></div>
  </body>
</html>
$ python -m http.server
```

としてそのページにアクセスすると左上に`4`と出てくる。
同じものをデフォルトexportで書き下すと
```
$ vim module.js
$ cat module.js
export default function square(x) {
  return x * x;
}
$ vim index.html
$ cat index.html
<html>
  <head>
    <title>Example</title>
    <script type="module">
      import square from './module.js';
      const elem = document.getElementById('main');
      const valueSquare = square(2);
      const squareNode = document.createTextNode(`${valueSquare}`);
      elem.appendChild(squareNode);
    </script>
  </head>
  <body>
    <div id="main"></div>
  </body>
</html>
$ python -m http.server
```

として同じ結果が得られる。

## 参考
1. [CommonJS と ES6の import/export で迷うなら](https://qiita.com/rooooomania/items/4c999d93ae745e9d8657)
1. [Understanding ES6 Modules](https://www.sitepoint.com/understanding-es6-modules/)
