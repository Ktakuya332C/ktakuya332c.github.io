# 不完備情報ゲームの均衡概念

オークション理論に関する本を読み始めた
- V.クリシュナ、[オークション理論](https://www.amazon.co.jp/dp/4502237612)

この本の数学補論Fに書かれている不完備情報ゲームの均衡概念についてまとめておく。

## 完備情報ゲームの均衡概念
まずは高校で学んだ支配戦略均衡やナッシュ均衡などを復習しておく。この本では対象がオークションであることもあり、戦略形ゲームに絞って理論を展開しており、展開形ゲームについては考慮していない。まずは完備情報ゲームの定義を復習する。
> *完備情報ゲーム*  
> 完備情報ゲーム$G$は次の3つの要素で構成される。
1. プレイヤーの集合$\mathcal{N}$
1. 各プレイヤー$i \in \mathcal{N}$に関する非空の行動集合$\mathcal{A}_i$
1. 各プレイヤー$i$の利得関数$u_i: \times_j \mathcal{A}_j \rightarrow \mathbb{R}$


### 支配戦略均衡
この本には書かれていないが、完備情報ゲームにおける支配戦略均衡は以下のようになるはずである。
> *支配戦略均衡*  
> 完備情報ゲーム$G$の支配戦略均衡とは、行動ベクトル$\bm{a}^* \in \times_j \mathcal{A}_j$で次を満たすものである。
$$
u_i(a^*_i, \bm{a}_{-i}) \ge u_i(a_i, \bm{a}_{-i})
\quad\forall i \in \mathcal{N}
\quad \forall \bm{a} \in \times_j \mathcal{A}_j
$$

支配戦略均衡の条件は次の条件と同値であり、
$$
a^*_i = \argmax_{a_i} u_i(a_i, \bm{a}_{-i})
\quad\forall i \in \mathcal{N}
\quad \forall \bm{a}_{-i} \in \times_{j \neq i} \mathcal{A}_j
$$

ここで特に
$$
\argmax_{a_i} u_i(a_i, \bm{a}_{-i}) \in \mathcal{A}_i
$$

は、他のプレイヤーの行動$\bm{a}_{-i}$に対するプレイヤー$i$の最適反応とよばれる。
よって、支配戦略均衡は次の手順で求められる。
```
FOR それぞれのプレイヤーiに対して次を行う
  FOR プレイヤーi以外の他のプレイヤーが取りうる行動の組a_minus_iそれぞれに対して次を行う
    プレイヤーiによる最適反応を計算
  ENDFOR
  IF 全てのa_minus_iに対して計算した最適反応が同じ行動である
    プレイヤーiの支配戦略はその一意な最適反応となる
  ELSE
    プレイヤーiの支配戦略が存在しない
  ENDIF
ENDFOR
```


### ナッシュ均衡
完備情報ゲームにおけるナッシュ均衡は次のように定義される。
> *ナッシュ均衡*  
> 完備情報ゲーム$G$のナッシュ均衡とは、行動ベクトル$\bm{a}^* \in \times_j \mathcal{A}_j$で次を満たすものである。
$$
u_i(a^*_i, \bm{a}^*_{-i}) \ge u_i(a_i, \bm{a}^*_{-i})
\quad\forall i \in \mathcal{N}
\quad \forall a_i \in \mathcal{A}_i
$$

この条件は次の条件と同値なので
$$
a^*_i = \argmax_{a_i} u_i(a_i, \bm{a}^*_{-i})
\quad\forall i \in \mathcal{N}
\quad \forall a_i \in \mathcal{A}_i
$$

ナッシュ均衡は次の手順で求められる
```
FOR それぞれのプレイヤーiに対して次を行う
  FOR プレイヤーi以外の他のプレイヤーが取りうる行動の組a_minus_iそれぞれに対して次を行う
    プレイヤーiによる最適反応a_iを計算
    計算した行動の組(a_i, a_minus_i)を保存しておく
  ENDFOR
ENDFOR
IF 全てのiにおいて特定の行動の組が現れている
  その行動の組がナッシュ均衡(複数存在しうる)
ELSE
  ナッシュ均衡は存在しない
ENDIF
```

高校の時に習ったような、プレイヤーが二人の場合に利得行列を描きその要素に[下線を引いていくようなやり方](http://nabenavi.net/solving-nash-equilibria/)はこの手順を表の上で実際に行うわかりやすいやり方と言える。

## 不完備情報ゲームの均衡概念
オークションにおいては他のプレイヤーがオークション対象のものに対してどれだけの価値を置いているかが分からないため、完備情報ゲームの形で議論しようとすると利得関数がわからずゲーム自体の定義ができない。不完備情報はそのような場合に対処するため、ゲーム自体の構造がゲームが始まる前にランダムに定まるという仮定を置くことで議論を進める。
> *不完備情報ゲーム*  
> 不完備情報ゲーム$\Gamma$は次の3つの要素で構成される。
1. プレイヤーの集合$\mathcal{N}$
1. 各プレイヤー$i \in \mathcal{N}$に関する非空の行動集合$\mathcal{A}_i$
1. 各プレイヤー$i \in \mathcal{N}$に関するシグナル集合$\mathcal{X}_i$
1. 各プレイヤー$i$に関する利得関数$u_i: \times_j \mathcal{A}_j \times_j \mathcal{X}_j \rightarrow \mathbb{R}$
1. シグナルの積集合$\times_j \mathcal{X}_j$の上の確率密度関数$f$

各プレイヤー$i$は純粋戦略$\alpha_i: \mathcal{X}_i \rightarrow \mathcal{A}_i$を調整して最大の利得を得ようとする。

ゲームの時間発展としては次のような流れを考えると理解しやすい。
1. 各プレイヤー$i$に対するシグナル$x_i \in \mathcal{X}_i$が$f$からサンプルされる
1. 各プレイヤーはシグナル$x_i$の情報をもとに戦略$\alpha_i$に従って行動$a_i = \alpha_i(x_i)$を選ぶ
1. それぞれのプレイヤーに対する利得が利得関数$u_i(\bm{a}, \bm{x})$から定まる


### 支配戦略均衡
非完備情報ゲームにおける支配戦略均衡は次のように定義される。
> *支配戦略均衡*  
> 非完備情報ゲーム$G$の支配戦略均衡とは、戦略$\bm{\alpha}^*$で次を満たすものである。
$$
u_i(\alpha^*_i(x_i), \bm{a}_{-i}, \bm{x}) \ge u_i(\alpha_i(x_i), \bm{a}_{-i}, \bm{x})
\quad \forall i \in \mathcal{N}
\quad \forall \bm{x} \in \mathcal{X}
\quad \forall \bm{a}_{-i} \in \times_{j \neq i} \mathcal{A}_j
\quad \forall \alpha_i
$$

ここで戦略$\bm{\alpha}$の値域として取れる行動が制限されていないことから、上の不等式は次と同値である。
$$
u_i(\alpha^*_i(x_i), \bm{\alpha}_{-i}(\bm{x}_{-i}), \bm{x}) \ge u_i(\alpha_i(x_i), \bm{\alpha}_{-i}(\bm{x}_{-i}), \bm{x})
\quad \forall i \in \mathcal{N}
\quad \forall \bm{x} \in \mathcal{X}
\quad \forall \bm{\alpha}
$$

さらに、完備情報ゲームの場合と同じく次のように変形できる
$$
\alpha^*_i = \argmax_{\alpha_i} u_i(\alpha_i(x_i), \bm{\alpha}_{-i}(\bm{x}_{-i}), \bm{x})
\quad \forall i \in \mathcal{N}
\quad \forall \bm{x} \in \mathcal{X}
\quad \forall \bm{\alpha}_{-i}
$$

よって、支配戦略均衡は次の手順で求められる。
```
FOR それぞれのプレイヤーiに対して次を行う
  FOR プレイヤーi以外の他のプレイヤーが取りうる戦略の組alpha_minus_iそれぞれに対して次を行う
    FOR それぞれのシグナルの組xに対して次を行う
      プレイヤーiによるシグナルの組xと戦略alpha_minus_iに対する最適反応を計算
    ENDFOR
  ENDFOR
  IF 全てのxとalpha_minus_iに対して計算した最適反応が同じ戦略である
    プレイヤーiの支配戦略はその一意な戦略となる
  ELSE
    プレイヤーiの支配戦略が存在しない
  ENDIF
ENDFOR
```

### 事後均衡
非完全情報ゲームにおける[ナッシュ均衡に対応する均衡概念の一つ](https://www.econexp.org/hitoshi/keisemi1212.pdf)である。
> *事後均衡*  
> 非完備情報ゲーム$G$の事後均衡とは、戦略$\bm{\alpha}^*$で次を満たすものである。
$$
u_i(\alpha^*_i(x_i), \bm{\alpha}^*_{-i}(\bm{x}_{-i}), \bm{x}) \ge u_i(a_i, \bm{\alpha}^*_{-i}(\bm{x}_{-i}), \bm{x})
\quad \forall i \in \mathcal{N}
\quad \forall \bm{x} \in \mathcal{X}
\quad \forall a_i \in \mathcal{A}_i
$$

この条件は次の条件と同値なので
$$
\alpha^*_i(x_i) = \argmax_{a_i} u_i(a_i, \bm{\alpha}^*_{-i}(\bm{x}_{-i}), \bm{x})
\quad \forall i \in \mathcal{N}
\quad \forall \bm{x} \in \mathcal{X}
$$

事後均衡は次の手順で求められる
```
FOR それぞれのプレイヤーiに対して次を行う
  FOR プレイヤーi以外の他のプレイヤーが取りうる戦略の組alpha_minus_iそれぞれに対して次を行う
    FOR それぞれのシグナルxに対して次を行う
      プレイヤーiによるシグナルの組xと戦略alpha_minus_iに対する最適反応行動a_iを計算
    ENDFOR
    IF 最適反応a_iがプレイヤーiが知らないシグナルの組x_minus_iに依存しない
      x_iとa_iの組をプレイヤーiの最適反応alpha_iとして保存する
      計算した戦略の組(alpha_i, alpha_minus_i)を保存しておく
    ELSE
      事後均衡は存在しない
    ENDIF
  ENDFOR
ENDFOR
IF 全てのiにおいて特定の戦略の組が現れている
  その行動の組が事後均衡(複数存在しうる)
ELSE
  ナッシュ均衡は存在しない
ENDIF
```

### ベイジアンナッシュ均衡
非完全情報ゲームにおけるナッシュ均衡に対応する均衡概念のもう一つであり、ここで初めてシグナルの密度関数$f$が意味を持ってくることになる。
> *ベイジアンナッシュ均衡*  
> 非完備情報ゲーム$G$のベイジアンナッシュ均衡とは、戦略$\bm{\alpha}^*$で任意の$i \in \mathcal{N}$、$x_i \in \mathcal{X}_i$、$a_i \in \mathcal{A}_i$に対して次を満たすものである。
$$
E[u_i(\alpha^*_i(X_i), \bm{\alpha}^*_{-i}(X_{-i}), X) | X_i = x_i] \ge E[u_i(a_i, \bm{\alpha}^*_{-i}(X_{-i}), X) | X_i = x_i]
$$

この条件は任意の$i \in \mathcal{N}$、$x_i \in \mathcal{X}_i$に対して次が成り立つことと同値である。
$$
\alpha^*_i(x_i) = \argmax_{a_i} E[u_i(a_i, \bm{\alpha}^*_{-i}(X_{-i}), X) | X_i = x_i]
$$

よってベイジアンナッシュ均衡は次の手順で求められる
```
FOR それぞれのプレイヤーiに対して次を行う
  FOR プレイヤーi以外の他のプレイヤーが取りうる戦略の組alpha_minus_iそれぞれに対して次を行う
    FOR それぞれのシグナルx_iに対して次を行う
      プレイヤーiによるシグナルの組x_iと戦略alpha_minus_iに対する期待最適反応行動a_iを計算
    ENDFOR
    最適反応戦略alpha_iとして上で計算したx_iとa_iの組を保存
  ENDFOR
  計算した戦略の組(alpha_i, alpha_minus_i)を保存しておく
ENDFOR
IF 全てのiにおいて特定の戦略の組が現れている
  その行動の組がベイジアンナッシュ均衡(複数存在しうる)
ELSE
  ナッシュ均衡は存在しない
ENDIF
```
