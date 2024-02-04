# エクセンダールの第三章のまとめ

次の本を読み進めている。
- [確率微分方程式](https://www.amazon.co.jp/dp/4621061763)

今回は第三章についてまとめていく。少し確率過程一般の前提知識を紹介した後に、伊藤積分の定義とその性質を紹介していく章である。

## 確率過程に関する前提知識
伊藤積分の紹介に入る前に、いくつか確率過程を語る上で欠かせない概念の紹介をする。
> *フィルトレーション*  
> 可測空間$(\Omega, \mathcal{F})$上のフィルトレーションとは$\mathcal{F}$の部分完全加法族の増大列のことである。すなわち、$\mathcal{M}_t \subset \mathcal{F}$であって、
$$
0 \le s \le t \Rightarrow \mathcal{M}_s \subset \mathcal{M}_t
$$

を満たす列$\{\mathcal{M}_t\}_{t \ge 0}$のことを指す。

フィルトレーションと確率過程の関係については次の定義を紹介する必要がある。
> *適合*  
> 確率空間$(\Omega, \mathcal{F}, \textbf{P})$上の確率過程$\{X_t\}_{t \ge 0}$とフィルトレーション$\{\mathcal{M}_t\}_{t \ge 0}$を考える。各$t \ge 0$において、写像
$$
\omega \rightarrow X_t(\omega)
$$

が$\mathcal{M}_t$-可測となる時、確率過程$\{X_t\}$は$\{\mathcal{M}_t\}$-適合であるという。

さらに強く確立過程とフィルトレーションの関係を見ることができるのはマルチンゲールの定義においてである。
> *マルチンゲール*  
> 確率空間$(\Omega, \mathcal{F}, \textbf{P})$上の確率過程$\{X_t\}_{t \ge 0}$がフィルトレーション$\{\mathcal{M}_t\}_{t \ge 0}$に対して次の3条件を満たす時マルチンゲールであるという。
1. $\{X_t\}$は$\{\mathcal{M}_t\}$-適合である
1. 全ての$t \ge 0$について$\{X_t\}$は可積分
1. $0 \le s \le t$ならば$\textbf{E}[X_t | \mathcal{M_s}] = X_s$

マルチンゲール性の重要性はまずブラウン運動に見て取れる
> *ブラウン運動はマルチンゲール*  
> ブラウン運動$\{B_t\}_{t \ge 0}$は、$\{B_s | s \le t\}$から生成されるフィルトレーション$\{\mathcal{M_t}\}_{t \ge 0}$に対してマルチンゲールである。

また、マルチンゲールであれば次のような不等式も成立する
> *マルチンゲール不等式*  
> 確率過程$\{X_t\}_{t \ge 0}$がほとんど確実に連続かつマルチンゲールであれば、全ての$p \ge 1$と$T \ge 0$、$\lambda > 0$に対して以下が成立する
$$
\textbf{P}[\sup_{0 \le t \le T} |M_t| \ge \lambda] \le \frac{1}{\lambda^p} \textbf{E}[|M_T|^p]
$$


## 伊藤積分の定義
結論から言えば、伊藤積分は次の様な確率過程に対してのみ定義される。
> *伊藤積分可能性*  
> 確率空間$(\Omega, \mathcal{F}, \textbf{P})$上の確率過程$\{X_t\}$で、次の三つの条件を満たすものの集合を$\mathcal{V}(S, T)$と表す。
1. $(t, \omega) \rightarrow X_t(\omega)$は$\mathcal{B} \times \mathcal{F}$-可測
1. あるフィルトレーション$\{\mathcal{H}_t\}$が存在し、ブラウン運動$\{B_t\}$が$\{\mathcal{H}_t\}$-マルチンゲールであり、かつ$\{X_t\}$が$\{\mathcal{H}_t\}$-適合
1. $\textbf{E}[\int_S^T X_t^2 dt] < \infty$

まずは簡単な確率過程に対して伊藤積分を定義する。
> *初等的な確率過程*  
> 確率過程$\{X_t\} \in \mathcal{V}(S, T)$で、次の形に表現できるものは初等的であるという。
$$
X_t(\omega) = \sum_{j} e_j(\omega) \chi_{[t_j, t_{j+1})}(t)
$$

ただしここで$e_j$は確率変数であり、$\chi$は定義関数。

> *初等的な確率過程に対する伊藤積分*  
> 初等的な確率過程
$$
X_t(\omega) = \sum_{j} e_j(\omega) \chi_{[t_j, t_{j+1})}(t)
$$

に対して伊藤積分を以下の確率変数
$$
\int_S^T X_t dB_t(\omega) = \sum_{j} e_j(\omega) [B_{t_{j+1}} - B_{t_j}](\omega)
$$

として定義する。

一般の確率過程$\{X_t\} \in \mathcal{V}$に対する伊藤積分はそれらの極限によって定義される。
> *伊藤積分*  
> 任意の確率過程$\{X_t\} \in \mathcal{V}$に対して、ある初等的な確率過程の列$\{\{Y_t^n\}\}$が存在し、
$$
\lim_{n \rightarrow \infty} \textbf{E}[\int_S^T |X_t - Y_t|^2 dt] = 0
$$

を満たす。$\{X_t\}$に対する伊藤積分を
$$
\int_S^T X_t dB_t = \lim_{n \rightarrow \infty} \int_S^T Y^n_t dB_t
$$

として定義する。ただし極限は$L^2(\textbf{P})$の意味でとる。


## 伊藤積分の性質
いくつかの基本的な性質を列挙する。
> *基本的な性質*  
> 確率空間$(\Omega, \mathcal{F}, \textbf{P})$上の確率過程$\{X_t\},\{Y_t\} \in \mathcal{V}(0, T)$とした時、$0 \le S \le T$として
- ほとんど確実に$\int_S^T X_t dB_t = \int_S^U X_t dB_t + \int_U^T X_t dB_t$
- ほとんど確実に$\int_S^T (cX_t + Y_t) dB_t = c \int_S^T X_t dB_t + \int_S^T Y_t dB_t$
- $\textbf{E}[\int_S^T X_t dB_t] = 0$
- $\int_S^T X_t dB_t$は$\mathcal{F}_T$-可測

また、次の様な特徴もある。
> *伊藤積分の等長性*  
> 全ての$\{X_t\} \in \mathcal{V}(S, T)$に対して以下が成り立つ。
$$
\textbf{E}[(\int_S^T X_t dB_t)^2] = \textbf{E}[\int_S^T X_t^2 dt]
$$

そして、伊藤積分は積分領域に関して連続となるものが取れる。
> *伊藤積分の積分領域に関する性質*  
> 確率空間$(\Omega, \mathcal{F}, \textbf{P})$上の確率過程$\{X_t\} \in \mathcal{V}(0, T)$に対する伊藤積分
$$
\int_0^t X_s dB_s
$$

のt-連続修正が必ず存在する。すなわち、t-連続な確率過程$\{J_t\}$で、
$$
\textbf{P}[J_t = \int_0^t X_t dB_t] = 1
$$

となるものが存在する。

そして、マルチンゲールとなる。
> *伊藤積分のマルチンゲール性*  
> 確率過程$\{X_t\} \in \mathcal{V}(0, T)$に対する伊藤積分
$$
Y_t = \int_0^t X_s dB_ss
$$

はマルチンゲールである。
