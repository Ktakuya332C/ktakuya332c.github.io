# hdr-histogramの基本的な発想

レスポンスタイムの99パーセンタイルなどを正確に監視する方法を探していたらHdrHistogramという方法に出会った。残念ながらHdrHistogramについての詳しい説明はどこにも載っていなかったので、とりあえずcppで書かれた簡単な[ライブラリ](https://github.com/mikeb01/HdrHistogramCpp)を漁ってみて基本的な発想だけは理解した気がするのでまとめておく。

## シンプルな例

形式的にきちんと定義しようと思うと比較的難しくなりがちなので、まずは簡単な例を考えて肩慣らしをしてみる。とあるサーバーのレスポンスタイムが大抵は10ms程度なのだが、たまに何かしらの不具合のせいで1sかかってしまったりすることがあるとする。取りたい値の精度としてはとりあえず有効数字が2桁くらいあれば十分だと考え、測定できる最大の値はとりあえず余裕を持って10s(=10000ms)としておく。

HdrHistogramはその名の通り内部的にはHistogramを作成する。そのHistogramのbinは有効数字2桁、最大10000msという制限から、次のようにとる。

```
[0, 1)
[0, 2)
...
[9, 10)
[10, 11)
[11, 12)
...
[99, 100)
[100, 110)
[110, 120)
...
[990, 1000)
[1000, 1100)
[1100, 1200)
...
[9900, 10000)
[10000, 無限)
```

あまり見ない奇妙な分割方法だが、とりあえず全ての負でない整数がどこかのbinに入ることがわかると思う。また、有効数字は2桁と指定されているのでこれらのbinの端の値は全て有効数字が2桁存在するようになっていて、同じbinに分類される数字は全て有効数字2桁が同じ値を持っているようになる。

レスポンスタイムを計測するにつれて上のbinで構成されるヒストグラムのカウントを上昇させていく。通常はレスポンスタイムはある程度のwindowの中での値を測定することが多いので、その場合にはある程度時間が経ったらそのヒストグラムからその値は削除していく。

ある程度値が貯まったら実際に99percentileを計算することができる。ヒストグラムに入っている値の個数の99パーセンタイルに当たるのはいくつ目の値かを計算して、その値がいくつ目のbinに入っているかを探していけばいい。binが見つかったら、そのbinに入っている値はいずれも有効数字2桁は同じなので、そのbinの最小の値を返せば有効数字2桁の正確性は保たれる。

## 実装例

上記のアルゴリズムを明確に数式に落とすのは比較的手間なので実装令を用意して逃げることにする。

```
#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>

int calc_n_digits(int value, int base) {
  int count = 0;
  while(value) {
    count++;
    value /= base;
  }
  return count;
}

int calc_pow(int value, int n) {
  int ret = 1;
  for (int i=0; i<n; i++) ret *= value;
  return ret;
}

int calc_index(int value, int n, int base) {
  int n_digits = calc_n_digits(value, base);
  if (n_digits < n) {
    return value;
  } else {
    int base_range = calc_pow(base, n-1);
    int range = calc_pow(base, n) - base;
    int large_index = base_range + range * (n_digits - n);
    int small_index = (value - calc_pow(base, n_digits-1)) / calc_pow(base, n_digits - n);
    return large_index + small_index;
  }
}

int calc_value(int ind, int n, int base) {
  int base_range = calc_pow(base, n-1);
  if (ind < base_range) {
    return ind;
  } else {
    int range = calc_pow(base, n) - base;
    int ext_n_digits = (ind - base_range) / range;
    int n_digits = n + ext_n_digits;
    int base_value = calc_pow(base, n_digits - 1);
    int base_index = base_range + range * (n_digits - n);
    int ext_value = (ind - base_index) * calc_pow(base, ext_n_digits);
    return base_value + ext_value;
  }
}

int calc_percentile_index(const std::vector<int>&amp; hist, float percentile) {
  int total = std::accumulate(hist.begin(), hist.end(), 0);
  int target = std::ceil(percentile * total);
  int cumsum = 0;
  int ind = 0;
  while(target > cumsum) {
    cumsum += hist[ind];
    ind++;
  }
  return --ind;
}

int main() {
  // prepare
  int n = 2;
  int m = 20000;
  int base = 10;
  int size = calc_index(m, n, base) + 1;
  std::vector<int> hist(size, 0);

  // record data
  for (int i=1; i<=10000; i++) {
    int ind = calc_index(i, n, base);
    hist[ind]++;
  }

  // calculate percentiles
  float percentile = 0.99;
  int ind = calc_percentile_index(hist, percentile);
  int value = calc_value(ind, n, base);
  std::cout << percentile << "p: " << value << std::endl; // 0.99p: 9900
}
```

## その他

- 実際に実装する際には10進数ではなく2進数で計算を行った方がbit-shiftが使えるので早くなるはず
- 実際に適用する際には移動平均ならぬ移動分位点を計算するはずなので、何かしらの方法でヒストグラムから値を消す方法が必要になる。追加した値をどこか別の場所に、例えばcircular-bufferなどに持っておいて、後から消していくとかの方法が必要になるはず。
