# "Derivation" of PPO algorithm

In this post, I will summarize a "derivation" of the proximal policy optimization algorithm (PPO). Since PPO is not an algorithm that can be deduced from a first principle, I quoted the term "derivation" with double quotes. The following will outline some points that I think are critical to understanding the algorithm, but other nitty-gritty details will be left unexplained.

## References
If you want to learn PPO algorithm in depth, please see these articles and videos instead of my rough note. These were really helpful for me to understand not only the high level intuition of the algorithm but also its implementation details.
- Kevin Murphy, [Reinforcement Learning: An Overview](https://arxiv.org/abs/2412.05265)
  - To put PPO into the context of reinforcement learning history
- Ruifan Yu, [CS85 Lecture 15b Proximal Policy Optimization](https://www.youtube.com/watch?v=wM-Sh-0GbR4)
  - To learn the intuition behind the algorithm
- Lilian Weng, [Policy Gradient Algorithms](https://lilianweng.github.io/posts/2018-04-08-policy-gradient/)
  - To learn the proof of the policy gradient theorem
- John Schulman et al. [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)
  - Original Paper
- Shengyi Huan et al. [The 37 Implementation Details of Proximal Policy Optimization](https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/)
  - To know the nitty-gritty details
- John Schulman [Approximating KL Divergence](http://joschu.net/blog/kl-approx.html)
  - To understand KL approximation used in various implementations

## Overview
"Derivation" of the PPO algorithm consists of 4 or 5 steps.
1. Take the gradient of the objective (policy gradient theorem)
2. Reduce the variance of the estimate (baseline)
3. Importance of sampling to reuse trajectory sample
4. Clipping to reduce erratic behaviors
5. Major tricks (KL regularization, entropy bonus)

See article like [this one](https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/) for the rest of the tricks required to actually implement PPO algorithtm.

## Take the gradient of the objective
Since the PPO algorithm is one of the policy gradient algorithms, we will take the gradient of the objective function, expected cumulative reward $J_\pi$. The gradient will settle in this easy-to-understand form
$$ \partial J_\pi = \mathbb{E}_\pi[Q \partial \ln \pi]. $$
This fact is called the policy gradient theorem. "Just taking gradient" of $J_\pi$ seems like an easy step, but without some neat notations, it is a little hard to see this result. See [this article](https://lilianweng.github.io/posts/2018-04-08-policy-gradient/) for the details.

## Reduce variance of the estimate
To reduce the variance of the gradient estimate, we introduce baseline $b(s)$ to the estimate like this
$$ \partial J_\pi = \mathbb{E}_\pi[(Q - b) \partial \ln \pi]. $$
We usually take value function $V_\pi$ as a baseline, so the gradient is now
$$ \partial J_\pi = \mathbb{E}_\pi[A \partial \ln \pi] $$
where $A_\pi$ is an advantage function. The baseline does not have any effect on the gradient estimate because
$$ \mathbb{E}_\pi[b \partial \ln \pi] = 0. $$

## Importance sampling to reuse trajectory samples
To reuse sample trajectories from the previous iteration of the policy, we use importance sampling to adjust the weight of each sample
$$ \partial J_\pi = \mathbb{E}_{\pi'}[A \partial \ln \pi \frac{\pi}{\pi'}] = \mathbb{E}_{\pi'}[A \frac{ \partial \pi}{\pi'}] $$
where $\pi'$ is a policy that was used to take sample trajectories. With an implicit stop gradient on the advantage function, we can rewrite the gradient as
$$ \partial J_\pi = \partial \mathbb{E}_{\pi'}[A \frac{\pi}{\pi'}] $$

## Clipping to reduce erratic behaviors
$\pi / \pi'$ can be very unstable, so just clip them to stabilize the training. 
$$ J'_\pi = \mathbb{E}_{\pi'}[\text{clip}(\frac{\pi}{\pi'}, 1-\epsilon, 1+\epsilon)A ]. $$
But clipping can make this surrogate objective $J'_\pi$ larger than the original one $J_\pi$. This may possibly end up being a vulnerability the algorithm tries to exploit. To prevent that, we make another surrogate objective that is definitively an upper bound by the original one.
$$ J'_\pi = \mathbb{E}_{\pi'}[\text{min}(\frac{\pi}{\pi'} A, \text{clip}(\frac{\pi}{\pi'}, 1-\epsilon, 1+\epsilon)A) ]. $$

## Major tricks
Add KL regularization to make importance sampling effective
$$ J'_pi - \beta KL(\pi' || \pi). $$
Usually, KL divergence is approximated by a Monte Carlo sample with [some tricks](http://joschu.net/blog/kl-approx.html).

Another major trick is to add an entropy bonus that encourages the agents to diversify their actions
$$ J'_pi - \beta KL(\pi' || \pi) + Entropy(\pi) $$

## My Implementations
- [Classic CartPole with PPO](https://gist.github.com/Ktakuya332C/2dd558a5573030a4897e6c78737b87db)
- [Arithmetic Problem Solving with GPT2](https://gist.github.com/Ktakuya332C/0f9e7f554c60a23f253b3d676e5d49fd)
