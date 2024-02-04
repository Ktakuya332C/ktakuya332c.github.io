# A regret bound of UCBID algorithm

In this post, I will explain the main result of the following paper
- J. Weed et al. (2015), [Online learning in repeated auctions](https://arxiv.org/abs/1511.05720)

The paper proposes a model of online advertising auctions and a bidding algorithm for its participants. The model is called the sequential Vickrey auctions, in which bidders compete for multiple goods sequentially, without knowing the exact values they can obtain from the goods. The bidding algorithm they propose is named $ \textrm{UCB}_{ID} $, which is an extension of the well-known UCB algorithm. The algorithm was shown to perform well on the model both in an adversarial case and a non-adversarial case (stochastic case).

The focus of this post is the proof of the regret bound. I will focus only on the simplest case, simpler than theorem 1 of the paper. To show that, I will first summarize the sequential Vickrey auctions and the $ \textrm{UCB}_{ID} $ algorithm. Then, the proof of the regret bound will follow.


## Sequential Vickrey Auctions

The sequential Vickrey auctions is an extension of the Vickrey auction. As far as I know, the Vickrey auction is a synonym for the second price auction. The auction sells a single good for multiple bidders. Let $K$ be the number of bidders, and $b[k]$ be the bid of the $k$ th bidder. The highest bidder $k^* \in \argmax_k{b[k]}$ wins the good and pays the price that is equal to the second-highest bid $m^* = \max_{k \neq k^*}{b[k]}$. Each bidder measures the utility of the outcome by assigning a single real value $v$ to the good. The bidders are assumed to be maximizing the utility $v - m^*$, defined as the difference between the value $v$ and the price $m^*$.

In the sequential Vickrey auctions, the Vickrey auctions are held multiple times. In each round $t \le T$, a homogenous good is sold to bidders, and the auction proceeds exactly the way the Vickrey auction proceeds. Here, we only consider the case of finite-horizon $T < \infty$. The case of infinite-horizon is not discussed in the paper, and I am not sure whether the lemmas and theorems also hold in this case.

In addition, in contrast to the Vickrey auction, the bidders are assumed not to know the value $v$ of the good sold at each auction. The motivation for this assumption comes from the case of online advertising auctions, in which bidders, do not know the value they would obtain if the ad were placed on the page because whether the ad may interest viewers enough to generate revenue for the advertiser is unknown beforehand. The paper examines the two generating processes of the values. Here, I will only focus on the simplest case, the stochastic case, in which the values the bidders obtain are assumed to be sampled from predefined i.i.d. distribution with mean $v$. 

In the paper, the values and bids are restricted to take values in the range $[0, 1]$ to simplify the arguments. The exact value of this upper and lower bound are not necessarily zero and one, but the values and bids must be in a certain bounded interval.

The objective of one bidder participating the sequential Vickrey auctions is to minimize the pseduo regret
$$
\bar{R}_T = \max_{b \in [0, 1]} \sum_{t=1}^T \mathbb{E}[(v_t - m_t) \mathbb{1}\{b > m_t\}] - \sum_{t=1}^T \mathbb{E}[(v_t - m_t) \mathbb{1}\{b_t > m_t\}],
$$
where the first term is the utility the bidder can obtain with the best constant bid $b$, and the second term is the actual utility the bidder obtained. $v_t, b_t, m_t$ are value, bid, highest bid of other bidders, at round $t$, respectively.


# UCBID algorithm

$\textrm{UCB}_{ID}$ algorithm submits a bid with a little offset determined by the history of the outcomes. For the first auction, the algorithm submits $b_t = 1$ to win the auction. At auction $t+1$, it submits a bid defined by
$$
b_{t+1} = \min(\bar{v}_{\omega_t} + \sqrt{\frac{3 \ln(t)}{2 \omega_t}}, 1)
$$
where $\omega_t$ is the number of rounds the bidder won up to round $t$, $\bar{v}_{\omega_t}$ is the average value the bidder obtained from the winning auctions. The $\min$ is introduced to satisfy the constraint $0 \le b_t \le 1$, and is necessary to prove the exact regret bounds proved later. However, I presume that the same order of regret bound can be achieved without the $\min$ as long as the bid is bounded by a finite value.

Theorem 1 of the paper states that the $\textrm{UCB}_{ID}$ algorithm achives the following exact regret bound
$$ \bar{R}_T \le 3 + \frac{12 \ln(T)}{\Delta} \wedge 2 \sqrt{6 T \ln(T)}. $$
In this post, I will prove the simpler version of the regret bound
$$ \bar{R}_T \le 3 + 2 \sqrt{6 T \ln(T)}, $$
to present only the essence of the proof.


# Proof of the regret bound

Almost all the regret bounds of bandit problems are derived from the Hoeffding inequality. First I am going to review the statement of the Hoeffding inequality by citing the wikipedia article. Let $X_1, X_2, \cdots, X_n$ be the independent random variables such that $a_i \le X_i \le b_i$ almost surely. Consider the sum of these random variables 
$$ S_n = X_1 + X_2 + \cdots + X_n $$
Then, Hoeffding's theorem states that, for all $t \ge 0$,
$$ P(S_n - \mathbb{E}[S_n] \le t) \le \exp(- \frac{2t^2}{\sum_{i=1}^n (b_i - a_i)^2}). $$
Because almost all values we will consider are assumed to be in range @inmath{[0, 1]}, we restrict the attention to the case of $a_i=0, b_i=1$. Then, the inequaility becomes
$$ P(S_n - \mathbb{E}[S_n] \ge t) \le \exp(- \frac{2t^2}{n}).$$
We are mostly interested in the means of random variables instead of sums. Define mean of the random variables and its expectation as
$$\begin{aligned}
\bar{\mu}_n &= \frac{1}{n} \sum_{i=1}^n X_i \\
\mu_n &= \mathbb{E}[\bar{\mu}_n],
\end{aligned}$$
Then, the inequality becomes
$$ P(\bar{\mu}_n - \mu_n \ge s) \le \exp(- 2 n s^2) $$
with $s = t/n$. Simplifying the bound with other parameter $1/r^3$ gives 
$$ P(\bar{\mu}_n - \mu_n \ge \sqrt{\frac{3 \ln(r)}{2 n}}) \le \frac{1}{r^3}, $$
which we will use mutliple times in later discussions.

Now, we will prove the regret bound. First, we will simplify the regret bound by removing the $v_t$ from the expression. It is easy because the probability distribution of $v_t$ does not depend any other variables. Therefore,
$$\begin{aligned}
\bar{R}_T &= \max_{b \in [0, 1]} \sum_{t=1}^T \mathbb{E}[(v_t - m_t) \mathbb{1}\{b > m_t\}] - \sum_{t=1}^T \mathbb{E}[(v_t - m_t) \mathbb{1}\{b_t > m_t\}] \\
&= \max_{b \in [0, 1]} \sum_{t=1}^T \mathbb{E}[(v - m_t) \mathbb{1}\{b > m_t\}] - \sum_{t=1}^T \mathbb{E}[(v - m_t) \mathbb{1}\{b_t > m_t\}].
\end{aligned}$$

Next, the term inside the first sum
$$ (v-m_t)\mathbb{1}\{b > m_t\} $$
takes maximum value at $b = v$, regardless of the value of $m_t$. It is easy to see that if we list all possible cases explicitly.

<img src="/20230703-ucbid/figure1.png" width="80%">

Then, the regret now becomes
$$\begin{aligned}
\bar{R}_T &= \mathbb{E}[\sum_{t=1}^T (v - m_t) \mathbb{1}\{v > m_t\}] - \mathbb{E}[\sum_{t=1}^T (v - m_t) \mathbb{1}\{b_t > m_t\}] \\
&= \sum_{t=1}^T \mathbb{E}[(v - m_t) (\mathbb{1}\{v > m_t\} - \mathbb{1}\{b_t > m_t\})].
\end{aligned}$$
Also, the term inside the expectation
$$ (v-m_t) (\mathbb{1}\{v > m_t\} - \mathbb{1}\{b_t > m_t\}) $$
is equivalent to
$$ (v - m_t) \mathbb{1}\{b_t < m_t < v\} + (m_t - v) \mathbb{1} \{v < m_t < b_t\}, $$
which is apparent if we list all possible cases

<img src="/20230703-ucbid/figure2.png" width="60%">

Then, the regret is
$$\bar{R}_T = \sum_{t=1}^T \mathbb{E}[(v - m_t) \mathbb{1}\{b_t < m_t < v\}] + \sum_{t=1}^T \mathbb{E}[(m_t - v) \mathbb{1} \{v < m_t < b_t\}]. $$
The first term is the regret incured by losing the auction even though the expected value the bidder can obtain was higher than the highest bid of other bidders. The second term is, in contrary, the regret incurred by winning the auction when the expected value was lower than the payment.

Because $\textrm{UCB}_{ID}$ algorithm submits a bid with some offset, the bid tends to be higher than the expected value. This implies that the probablity of the event satisfying
$$ b_t < m_t < v $$
is very low. With this intuition, we can bound the first term of the regret with a constant. To show that, we first bound the term with simpler term
$$ \begin{aligned}
\mathbb{E}[(v - m_t)\mathbb{1}\{b_t < m_t < v\}] &\le  \mathbb{E}[\mathbb{1}\{b_t < m_t < v\}] \\
&\le \mathbb{E}[\mathbb{1}\{b_t < v\}] \\
&\le P(b_t < v) \\
&= P(\bar{v}_{\omega_{t-1}} + \sqrt{\frac{3 \ln(t-1)}{2 \omega_{t-1}}} \le v )
\end{aligned}$$
To remove the dependency on $\omega_t$, we use union bound to get
$$\begin{aligned}
P(\bar{v}_{\omega_{t-1}} + \sqrt{\frac{3 \ln(t-1)}{2 \omega_{t-1}}} \le v ) &\le \sum_{s=1}^t P(\bar{v}_{s} + \sqrt{\frac{3 \ln(t-1)}{2 s}} \le v ) \\
&= \sum_{s=1}^t P(\bar{v}_{s} - v \le - \sqrt{\frac{3 \ln(t-1)}{2 s}})
\end{aligned}$$
Then, applying the modified Hoeffding bound, we get
$$\begin{aligned}
\sum_{s=1}^t P(\bar{v}_{s} - v \le - \sqrt{\frac{3 \ln(t-1)}{2 s}}) \le \sum_{s=1}^t \frac{1}{t^3} = \frac{1}{t^2}.
\end{aligned}$$
As a result,
$$ \sum_{t=1}^T \mathbb{E}[(v - m_t) \mathbb{1}\{b_t < m_t < v\}] \le \sum_{t=1}^T \frac{1}{t^2} \le \frac{\pi^2}{6}. $$

The second term
$$ \sum_{t=1}^T \mathbb{E}[(m_t - v) \mathbb{1} \{v < m_t < b_t\}] $$
is a litte harder to bound. First, it is sufficient to sum over all winning rounds
$$\begin{aligned}
\sum_{t=1}^T \mathbb{E}[(m_t - v) \mathbb{1} \{v < m_t < b_t\}] &= \sum_{t \in \mathcal{W}} \mathbb{E}[(m_t - v) \mathbb{1} \{v < m_t < b_t\}] \\
\mathcal{W} &= \{t | m_t < b_t\}.
\end{aligned}$$
Careful rearrangement of the term inside the summation gives
$$\begin{aligned}
\mathbb{E}[(m_t - v) \mathbb{1} \{v < m_t < b_t\}] &= \mathbb{E}[(m_t - v) \mathbb{1} \{0 < m_t -v < b_t -v\}] \\
&\le \mathbb{E}[\mathbb{1} \{0 < m_t -v < b_t -v\}].
\end{aligned}$$
where we used the fact that $m_t - v \le 1$. The expectation is taken over $m_t$ and $b_t$, and they are uncorrelated. Therefore,
$$\begin{aligned}
\mathbb{E}[\mathbb{1} \{0 < m_t -v < b_t -v\}] &= \mathbb{E}_{m_t} \mathbb{E}_{b_t} [\mathbb{1} \{0 < m_t -v < b_t -v\}] \\
&= \int^{\infty}_0 dm_t P(m_t | \{m_s, b_s\}_{s=1}^{t-1}) \mathbb{E}_{b_t} [\mathbb{1} \{0 < m_t -v < b_t -v\}] \\
&\le \int^{\infty}_0 dm_t \mathbb{E}_{b_t} [\mathbb{1} \{0 < m_t -v < b_t -v\}] \\
&= \int^{\infty}_{-v} du \mathbb{E}_{b_t} [\mathbb{1} \{0 < u < b_t -v\}] \\
&= \int^{\infty}_{0} du \mathbb{E}_{b_t} [\mathbb{1} \{0 < u < b_t -v\}] + \int^{0}_{-v} du \mathbb{E}_{b_t} [\mathbb{1} \{0 < u < b_t -v\}] \\
&= \int^{\infty}_{0} du \mathbb{E}_{b_t} [\mathbb{1} \{u < b_t -v\}]
\end{aligned}$$
Then the second term of the regret is now
$$\begin{aligned}
\sum_{t=1}^T \mathbb{E}[(m_t - v) \mathbb{1} \{v < m_t < b_t\}] &= \sum_{t \in \mathcal{W}} \int^{\infty}_{0} du \mathbb{E}_{b_t} [\mathbb{1} \{u < b_t -v\}] \\
&= \sum_{t \in \mathcal{W}} \int^{\infty}_{0} du P\{u < \bar{v}_{\omega_{t-1}} + \sqrt{\frac{3 \ln(t-1)}{2 \omega_{t-1}}}-v\}
\end{aligned}$$
Because $\mathcal{W}$ is all the winning auctions, the value of $\omega_{t-1}$ does not have duplication. Thus,
$$\begin{aligned}
\sum_{t \in \mathcal{W}} \int^{\infty}_{0} du P\{u < \bar{v}_{\omega_{t-1}} + \sqrt{\frac{3 \ln(t-1)}{2 \omega_{t-1}}}-v\} &\le \sum_{t \in \mathcal{W}} \int^{\infty}_{0} du  P\{u < \bar{v}_{\omega_{t-1}} + \sqrt{\frac{3 \ln(T)}{2 \omega_{t-1}}}-v\} \\
&\le \sum_{t=1}^T \int^{\infty}_{0} du P\{u < \bar{v}_{t} + \sqrt{\frac{3 \ln(T)}{2 t}}-v\}
\end{aligned}$$
Using another modification of Hoeffding inequality
$$ P(\bar{v}_t - v > \sqrt{\frac{3 \ln(T)}{2 t}} + u) \le \frac{\exp(-u^2/2)}{T^3}, $$
The integral becomes
$$\begin{aligned}
\int^{\infty}_{0} du P\{u < \bar{v}_{t} + \sqrt{\frac{3 \ln(T)}{2 t}}-v\} &= \int^{\infty}_{0} du P\{\bar{v}_{t} -v > \sqrt{\frac{3 \ln(T)}{2 t}} + u - \sqrt{\frac{6 \ln(T)}{t}}\} \\
&= \int^{\infty}_{- \sqrt{\frac{6 \ln(T)}{t}}} dr P\{r + \sqrt{\frac{3 \ln(T)}{2 t}} < \bar{v}_{t} -v\} \\
&\le \int^{\infty}_{0} dr P\{r + \sqrt{\frac{3 \ln(T)}{2 t}} < \bar{v}_{t} -v\} + \sqrt{\frac{6 \ln(T)}{t}} \\
&\le \int^{\infty}_0 dr \frac{\exp(-r^2/2)}{T^3} + \sqrt{\frac{6 \ln(T)}{t}} \\
&= \frac{1}{T^3}\sqrt{\frac{\pi}{2}} + \sqrt{\frac{6 \ln(T)}{t}}
\end{aligned}$$
Summarizing, the second term is bounded by
$$\begin{aligned}
\sum_{t=1}^T \mathbb{E}[(m_t - v) \mathbb{1} \{v < m_t < b_t\}] &\le \frac{1}{T^2}\sqrt{\frac{\pi}{2}} + \sum_{t=1}^T \sqrt{\frac{6 \ln(T)}{t}} \\
&\le \sqrt{\frac{\pi}{2}} + 2\sqrt{6 T \ln(T)}.
\end{aligned}$$
The last inequality follows from the fact
$$ \sum_{t=1}^T \frac{1}{\sqrt{t}} \le 2 \sqrt{T}. $$

Combining the analysis of the first and second term of the regret, we get
$$\begin{aligned}
\bar{R}_T &\le \frac{\pi^2}{6} + \sqrt{\frac{\pi}{2}} + 2\sqrt{6 T \ln(T)} \\
&\le 3 + 2\sqrt{6 T \ln(T)}
\end{aligned}$$