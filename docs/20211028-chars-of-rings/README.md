# 様々な可換環の具体例

今読み進めているガロア理論の教科書
- [今度こそわかるガロア理論](https://www.kspub.co.jp/book/detail/1566026.html)

の3章で紹介されている可換環の性質についてまとめる。

## 可換環の分類
可換環はそれらが持つ代表的な性質で下図のように分類できる([ref](https://en.wikipedia.org/wiki/Integral_domain))

<img src="/20211028-chars-of-rings/various-rings.png">

以下ではそれらの具体例を列挙していく。

### 可換環
$\mathbb{Z}_6$は可換環だが整域ではない。例えば$2$と$3$は零元ではないが、その積は$0$になる。

### 整域
次の環$A$は整域ではあるが素元分解整域ではない
$$
A = \{f(x) \in \mathbb{Q}[x] | f(0) \in \mathbb{Z}\}
$$

整域であることは、$\mathbb{Q}$が整域であることから導かれる([ref](https://math.stackexchange.com/questions/2187381/prove-that-if-a-commutative-ring-r-is-integral-domain-then-the-polynomial-rin))。
素元分解整域でないことは、素元$x$が次の$f(x)$と$g(x)$の積$f(x)g(x)$を割り切るが
$$
f(x) = \frac{1}{2}x, \quad g(x) = 2
$$

そのどちらも割り切れないことからわかる([ref](https://math.stackexchange.com/questions/3999158/is-there-an-integral-domain-containing-an-element-having-no-factorization-into-i))。ここで$1/2 \not \in A$に注意する。

### 素元分解整域
$\mathbb{Z}[x]$は素元分解整域だが単項イデアル整域ではない。
素元分解整域であることはガウスの補題を使うと証明できるが([ref](https://math.stackexchange.com/questions/2884646/gauss-lemma-prove-mathbbzx-ufd))、長いので記載しない。
単項イデアル整域でないことは、次のイデアルが単項イデアルでないことからわかる([ref](https://math.stackexchange.com/questions/500254/is-mathbbzx-a-principal-ideal-domain))
$$
\{f(x)x + 2g(x) | f, g \in \mathbb{Z}[x]\}
$$


### 単項イデアル整域
$\mathbb{Z}$上では任意のイデアルが単項イデアルである。

## 素元と既約元について
素元と既約元は次のような定義域を持ち、共に定義される場合それらは一致する。

<img src="/20211028-chars-of-rings/various-elements.png">

## 素イデアルと極大イデアルについて
任意の極大イデアルは素イデアルだが、特に単項イデアル整域においてそれらは一致する。

<img src="/20211028-chars-of-rings/various-ideals.png">

ここで$\mathbb{Z}[x]$には素イデアルだが極大イデアルではないようなイデアルが存在するはずだが、確かに次の素イデアルが極大イデアルではない([ref](https://yutsumura.com/examples-of-prime-ideals-in-commutative-rings-that-are-not-maximal-ideals/))
$$
\{xf(x) | f \in \mathbb{Z}[x]\} \subset \{2f(x) | f \in \mathbb{Z}[x]\}
$$
