OpenBLASで行列とベクトルの計算
2018-11-30


OpenBLASで行列とベクトルの計算を行うための関数\emp{cblas_dgemv}のドキュメントがあまりなかったので、その使用方法を一応まとめる。


\emp{cblas_dgemv}が計算することのできる形は次の形に制限される。自然数$N, M$に対して
\ul
{サイズ$N \times M$の行列$A$}
{サイズ$M$のベクトル$x$}
{サイズ$N$のベクトル$y$}
の三つを使って
$$
y = \alpha A x + \beta y
$$
と書けるものを計算することができる。ただしここで、$\alpha, \beta$は適当な実数である。


例えば、次のような行列$A$とベクトル$x$に対して
\code{
const int n_cols = 5;
const int n_rows = 4;
double A[] = {
  8, 4, 7, 3, 5,
  1, 1, 3, 2, 1,
  2, 3, 2, 0, 1,
  1, 2, 3, 4, 1
};
double x[] = { -1, 2, -1, 1, 2 };
}
$y = Ax$を計算したい場合は
\code{
double y[n_rows];
double alpha = 1.0;
double beta = 1.0;
cblas_dgemv(CblasRowMajor, CblasNoTrans, n_rows, n_cols,
    alpha, A, n_cols, x, 1, beta, y, 1);
}
とすれば計算できる。
