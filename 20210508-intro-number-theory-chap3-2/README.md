# 数論入門第3章2節のまとめ

次の本を読んでいる
- 山本芳彦著、[数論入門](https://www.iwanami.co.jp/book/b259041.html)、岩波書店

入門者向けの本なので、数論の本筋以外の話を紹介するにあたって学部で習うような代数学の基礎的な事項も並べて紹介されている。学習する分には忘れている内容などの復習にもなるのでとても良いのだが、後から内容を思い出そうとすると復習の部分の内容とあわさって本筋がどのような内容だったかが思い出しにくい。ここではその本筋の内容だけを取り出してまとめていくことにする。

## 合同類
3章1節では合同類$\mathbb{Z}/m\mathbb{Z}$の性質の紹介がなされている。ほとんどが代数学の復習なので、実質本筋としては紹介されている内容は次の3つに絞られるように見える。
1. $\mathbb{Z}/m\mathbb{Z}$が整域であることと、$m$が素数であることは同値
1. $m$が素数の時、$\mathbb{Z}/m\mathbb{Z}$は体
1. $(m,n)=1$の時、$\mathbb{Z}/mn\mathbb{Z} \cong \mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/m\mathbb{Z}$

最後の内容については次のような環準同型写像$f$を考えて
$$
f: a \in \mathbb{Z} \rightarrow (a + n\mathbb{Z}, a + m\mathbb{Z})
$$

環準同型定理より証明できる。

## 既約剰余類
3章2節では合同類$\mathbb{Z}/m\mathbb{Z}$から得られる既約剰余類の性質とオイラー関数とのつながりが紹介されている。
> *既約剰余類*  
> 法$m$に関する既約剰余類とは次の集合のことを指す
$$
(\mathbb{Z}/m\mathbb{Z})^{\times} = \{\bar{a} \in \mathbb{Z}/m\mathbb{Z} | (a, m) = 1\}
$$

既約剰余類はアーベル群である。実際、$(1,m) = 1$であるから
$$
\bar{1} \in (\mathbb{Z}/m\mathbb{Z})^{\times}
$$

となり単位元が確保できる。逆元の存在は任意の$\bar{a} \in \mathbb{Z}/m\mathbb{Z}$に対して
$$
ax + bm = 1
$$

となるような$x, b \in \mathbb{Z}$が存在することから
$$
\bar{a} \bar{x} = \bar{1}
$$

となり、$\bar{x}$が逆元である。群であることを意識して以降は既約剰余類群と呼ぶ。

既約剰余類群の要素数はオイラー関数と呼ばれる。
> *オイラー関数*  
> 法$m$に関する既約剰余類群の要素数は$m$に関するオイラー関数と呼ばれる
$$
\phi(m) = \# (\mathbb{Z}/m\mathbb{Z})^{\times} = \{a = 1,2,\cdots, m-1 | (a, m) = 1\}
$$

オイラー関数については次の定理と合わせれば
> *ラグランジュの定理*  
> 位数$g$の有限群$G$において
- 部分群$H$の位数$h$は$g$の約数
- $G$の各元$a$の位数は$g$の約数

2つ目の提言は特に次の内容も意味する
$$
a^g = 1
$$

$(a,m)=1$となるような$a$に対して
$$
a^{\phi(m)} = 1 \quad (\textrm{mod} \ m)
$$

が成り立つことも意味する。