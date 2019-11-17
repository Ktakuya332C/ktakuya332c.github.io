OpenBLASをMacで使う
2018-11-26


OpenBLASをMacで使用する方法のまとめ。


まずはインストールから。インストールは基本的に\a{brew}{https://brew.sh/}を使って行う。
\code{
$ brew search openblas
$ brew install openblas
}
\a{このページ}{http://mayah.jp/posts/2016/blas/}などはどうも\emp{homebrew/science/openblas}などから取ってきている様子だが、自分がローカル環境(MacOS High Sierra)で行ったところ、上記の方法でインストールできた。インストールが終了すると最後に\emp{/usr/local/opt/openblas}以下にソースコードの実態を入れた旨と、そもそもMacにはAccelerateフレームワークによってBLASが入っているので、勝手に/usr/localに何かをsymlinkしたりはしないよというお知らせが出てきた。


また、このインストールを行う際に同時にRのUpdateがかかってしまったので無駄に時間が食われる羽目になった。brewでRをインストールする際に高速化のために、一緒にopenblasに依存させながらインストールしてしまったのでこうなった。あとでRでそれほど大きいデータを扱うことはなくなってきたので、Rからopenblasへの依存性はあとで外しておこう。


では実際に使っていく。以降の実験は\a{このブログ}{https://qiita.com/t--k/items/69c43a667a1283578012}を参考に行なっている。まずは、適当に行列の掛け算を行って見る。とりあえず必要なライブラリをincludeして、適当に行列を作る。
\code{
#include <iostream>
#include <random>
#include <cblas.h>
#include <time.h>

const int m = 1000;
const int k = 2000;
const int n = 3000;

// 行列作成
double* a = new double[m*k];
double* b = new double[k*n];
double* c = new double[m*n];

// 行列初期化
std::random_device rd;
std::mt19937 mt(rd());
std::uniform_real_distribution<> dist(0.0, 1.0);
for (int i=0; i<m*k; i++) a[i] = dist(mt);
for (int i=0; i<k*n; i++) b[i] = dist(mt);
}

まずは、普通にループで行列積をとって見る。
\code{
for (int i = 0; i < m; i++) {
  for (int t = 0; t < k; t++) {
    for (int j = 0; j < n; j++) {
        c[i * n + j] = a[i * k + t] * b[t * n + j];
    }
  }
}
}
次に、OpenBLASを使って行列積をとって見る。
\code{
cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans,
            m, n, k, 1.0, a, k, b, n, 0.0, c, n);
}
以上の作業を行なった後に、それぞれの行列積がどれくらいの時間かかったのかを測るスクリプトを書くと以下のようになった。
\code{
#include <iostream>
#include <random>
#include <cblas.h>
#include <time.h>

const int m = 1000;
const int k = 2000;
const int n = 3000;

int main() {
  // 行列作成
  double* a = new double[m*k];
  double* b = new double[k*n];
  double* c = new double[m*n];
  
  // 行列初期化
  std::random_device rd;
  std::mt19937 mt(rd());
  std::uniform_real_distribution<> dist(0.0, 1.0);
  for (int i=0; i<m*k; i++) a[i] = dist(mt);
  for (int i=0; i<k*n; i++) b[i] = dist(mt);
  
  // ループで行列積
  clock_t start1 = clock();
  for (int i = 0; i < m; i++) {
    for (int t = 0; t < k; t++) {
      for (int j = 0; j < n; j++) {
          c[i * n + j] = a[i * k + t] * b[t * n + j];
      }
    }
  }
  clock_t end1 = clock();
  double elapsed1 = (double)(end1 - start1) / CLOCKS_PER_SEC;
  std::cout << "Ordinary loop took " << elapsed1 << " second" << std::endl;
  
  // BLASで行列積
  clock_t start2 = clock();
  cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans,
              m, n, k, 1.0, a, k, b, n, 0.0, c, n);
  clock_t end2 = clock();
  double elapsed2 = (double)(end2 - start2) / CLOCKS_PER_SEC;
  std::cout << "BLAS loop took " << elapsed2 << " second" << std::endl;
  return 0;
}
}
このスクリプトを\emp{measure.cpp}として保存して次のようにコンパイルして実行すると、計測ができる。
\code{
$ g++ measure.cpp -lopenblas -O2 \
    -I/usr/local/opt/openblas/include -L/usr/local/opt/openblas/lib
$ ./a.out
Ordinary loop took 2.47567 second
BLAS loop took 0.276661 second
}
やはりBLASの行列計算は、普通のループに比べて10倍くらいは早いようだ。
