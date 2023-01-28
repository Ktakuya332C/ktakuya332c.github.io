OpenBLASで行列とベクトルの計算
2018-11-30

@p{OpenBLASで行列とベクトルの計算を行うための関数@incode{cblas_dgemv}のドキュメントがあまりなかったので、その使用方法を一応まとめる。}

@p{@incode{cblas_dgemv}が計算することのできる形は次の形に制限される。自然数@inmath{N, M}に対して}

@ul
  {サイズ@inmath{N \times M}の行列@inmath{A}}
  {サイズ@inmath{M}のベクトル@inmath{x}}
  {サイズ@inmath{N}のベクトル@inmath{y}}

@p{の三つを使って}

@blmath{
y = \alpha A x + \beta y
}

@p{と書けるものを計算することができる。ただしここで、@inmath{\alpha, \beta}は適当な実数である。}

@p{例えば、次のような行列@inmath{A}とベクトル@inmath{x}に対して}

@blcode{
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

@p{@inmath{y = Ax}を計算したい場合は}

@blcode{
double y[n_rows];
double alpha = 1.0;
double beta = 1.0;
cblas_dgemv(CblasRowMajor, CblasNoTrans, n_rows, n_cols,
    alpha, A, n_cols, x, 1, beta, y, 1);
}

@p{とすれば計算できる。}
