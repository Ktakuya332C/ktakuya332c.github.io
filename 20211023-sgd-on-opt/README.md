# 条件付き最適化における最急降下法

古いNeurIPSで発表されていた次の論文

- [Constrained differential optimization for neural networks](https://proceedings.neurips.cc/paper/1987/file/a87ff679a2f3e71d9181a67b7542122c-Paper.pdf)

で紹介されている、条件付き最適化問題を最急降下法で解く方法の概要を説明する。

## 問題設定

$n$次元実変数$x$が、ある実関数$g(x)$を用いた式
$$
g(x) = 0
$$

を満たす範囲で、別の実関数$f(x)$の極小値を求めよ。

## 最急降下法による解法

実変数$\lambda$を導入し、ラグランジアン
$$
L = f + \lambda g
$$

を最急降下法
$$
\begin{aligned}
\frac{dx_i}{dt} &= \frac{\partial L}{\partial x_i} = - \frac{\partial f}{\partial x_i} - \lambda \frac{\partial g}{\partial x_i} \\
\frac{d \lambda}{dt} &= \frac{\partial L}{\partial \lambda } = - g(x)
\end{aligned}
$$

から2つ目の式の右辺の符号のみを変えた次のダイナミクスを考える
$$
\begin{aligned}
\frac{dx_i}{dt} &= - \frac{\partial f}{\partial x_i} - \lambda \frac{\partial g}{\partial x_i} \\
\frac{d \lambda}{dt} &= g(x)
\end{aligned}
$$

有用な多くの場合に、このダイナミクスの収束先が求める解になる。

実際、$x_i$に対する$t$の二回微分は次の方程式に従うが
$$
\frac{d^2}{dt^2} x_i = - \sum_{j=1}^n (\frac{\partial^2 f}{\partial x_i \partial x_j} + \lambda \frac{\partial^2 g}{\partial x_i \partial x_j})\frac{d x_j}{dt} - g \frac{\partial g}{\partial x_i}
$$

これは摩擦や空気抵抗などのような非保存力の働く質点に対する運動方程式と解釈できる。この系のエネルギーは
$$
H = \frac{1}{2}(\frac{dx}{dt})^2 + \frac{1}{2}(g(x))^2
$$

と書け、エネルギーの変化率は次の式により決定される
$$
\begin{aligned}
\frac{dH}{dt} &= - \sum_{i=1}^n \sum_{j=1}^n A_{ij} \frac{dx_i}{dt} \frac{dx_j}{dt} \\
A_{ij} &= \frac{\partial^2 f}{\partial x_i \partial x_j} + \lambda \frac{\partial^2 g}{\partial x_i \partial x_j}
\end{aligned}
$$

もしも$A_{ij}$が常に正定値行列であれば、エネルギー$H$が常に減少することから、上記のダイナミクスは次の式を満たす停留点に収束することが示せるが
$$
\begin{aligned}
0 &= - \frac{\partial f}{\partial x_i} - \lambda \frac{\partial g}{\partial x_i} \\
0 &= g(x)
\end{aligned}
$$

これはこの停留点が、ラグランジアン$L$に対する未定乗数法の結果と一致することを示す。

## 適用例

二変数関数
$$
f(x, y) = \frac{1}{2}(x^2 + y^2)
$$

を線形の条件式
$$
x + y = 1
$$

の下で最小化することを考える。

この時行列$A_{ij}$は単位行列となるため明らかに正定値であり、ダイナミクス
$$
\begin{aligned}
\frac{dx}{dt} &= -x - \lambda (x + y - 1) \\
\frac{dy}{dt} &= -y - \lambda (x + y - 1) \\
\frac{d \lambda}{dt} &= x + y - 1
\end{aligned}
$$

に従って停留点を求めることで解が得られる。

ただし実際に数値的な実験を行ってみると数値的な安定性がなく微分方程式を解くことができなかった。

- [条件付き最適化問題を最急降下法で解く](https://gist.github.com/Ktakuya332C/3e2103d876d1bfb19299a3b2662b8c23)

この論文などで述べられているPID制御などを行わないと数値的には不安定な様子。

- [Responsive Safety in Reinforcement Learning by PID Lagrangian Methods](https://arxiv.org/abs/2007.03964)
