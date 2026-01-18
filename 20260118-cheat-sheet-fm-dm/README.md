# Cheat Sheet for Flow Matching and Diffusion Models

I recently watched the following lecture videos
- [MIT 6.S184 Introduction to Flow Matching and Diffusion Models](https://diffusion.csail.mit.edu/2025/index.html)

In this post, I will summarise key definitions and theorems presented in the lecture, so that I can easily recall the content later.

## Problem statement

Let $p_{data}(X)$ be a probability distribution over $X \in \mathbb{R}^d$. Given

- Samples: $\{x_i\}_{i=1}^N \sim p_{data}$
- Initial Distribution: $p_{init}(X)$ over $X \in \mathbb{R}^d$
- Diffusion Coefficient: $\sigma_t \in \mathbb{R}_{\geq 0}$ where time $t \in [0, 1]$

Find a time-dependent vector field $u_t(x) \in \mathbb{R}^d$ such that the final distribution $X_1$ of the stochastic differential equation (SDE)

$$\begin{aligned}
X_0 &\sim p_{init}(x) \\
dX_t &= u_t(X_t) dt + \sigma_t dW_t
\end{aligned}$$

matches the distribution $p_{data}(X)$.

The general stochastic case is called diffusion modeling, and the deterministic case ($\sigma_t = 0$) is called flow matching.

## Step 1 : Conditional Vector Field / Score Function

We begin with one of the simplest cases, where $p_{data}(x) = \delta(x - z)$. In this setting, we can easily construct a conditional probability path: a time-dependent probability distribution $p_t(x | z)$ over $\mathbb{R}^d$ satisfying

$$\begin{aligned}
p_0(x | z) &= p_{init}(x) \\
p_1(x | z) &= p_{data}(x) = \delta(x - z).
\end{aligned}$$

When $p_{init} = \mathcal{N}(0, I_d)$, one possible choice is $p_t(x | z) = \mathcal{N}(\alpha_t z, \beta_t^2 I_d)$, which clearly satisfies the above conditions.

If we can find a vector field $u_t(x | z)$ such that the final distribution $X_1$ of the SDE

$$\begin{aligned}
X_0 &\sim p_{init}(x) \\
dX_t &= u_t(X_t | z) dt + \sigma_t dW_t
\end{aligned}$$

matches the distribution $p_1(x | z) = \delta(x-z)$, then this vector field solves the problem in this special case.

To find such a vector field, it is helpful to consider the Fokker-Planck equation corresponding to the SDE

$$\begin{aligned}
\frac{\partial}{\partial t} p_t(x | z) &= - \mathrm{div} (u_t(x | z) p_t(x | z)) + \frac{\sigma_t^2}{2} \Delta p_t(x | z) \\
&= - \mathrm{div}(p_t(x | z) [u_t(x | z) - \frac{\sigma_t^2}{2} \nabla \ln p_t(x | z)]).
\end{aligned}$$

It is relatively straightforward to find a vector field $u_t^{target}(x | z)$ satisfying (See Example 11 of the lecture note)

$$ \frac{\partial}{\partial t} p_t(x | z) = - \mathrm{div}(p_t(x | z) u_t^{target}(x | z)) .$$

As a result, the vector field $u_t(x | z)$ can be written as a linear combination of "conditional vector field" $u_t^{target}(x | z)$ and "conditional score function" $\nabla \ln p_t(x | z)$

$$ u_t(x | z) = u_t^{target}(x | z) + \frac{\sigma_t^2}{2} \nabla \ln p_t(x | z) .$$

This gives the solution in the simplest case.

## Step 2: Marginal Vector Field / Score Function

We now consider the general case. Here, we define a "marginal probability path", a time-dependent probability distribution $p_t(x)$ over $\mathbb{R}^d$, satisfying

$$\begin{aligned}
p_0(x | z) &= p_{init}(x) \\
p_1(x | z) &= p_{data}(x)
\end{aligned}$$

by marginalizing over $z$

$$ p_t(x) = \int p_t(x | z) p_{data}(z) dz . $$

We can also define a "marginal vector field" $u_t(x)$ such that the final distribution $X_1$ of the following SDE

$$\begin{aligned}
X_0 &\sim p_{init}(x) \\
dX_t &= u_t(X_t) dt + \sigma_t dW_t
\end{aligned}$$

matches the distribution $p_t(x)$. This follows from the corresponding Fokker-Planck equation:

$$\begin{aligned}
\frac{\partial}{\partial t} p_t(x) &= \int \frac{\partial}{\partial t} p_t(x | z) p_{data}(z) dz \\
&= \int [- \mathrm{div} (u_t(x | z) p_t(x | z)) + \frac{\sigma_t^2}{2} \Delta p_t(x | z)] p_{data}(z) dz \\
&= - \mathrm{div} (u_t(x) p_t(x)) + \frac{\sigma_t^2}{2} \Delta p_t(x).
\end{aligned}$$

$u_t(x)$ can be decomposed as

$$\begin{aligned}
u_t(x) &= \int u_t(x | z) \frac{p_t(x | z) p_{data}(z)}{p_t(x)} dz \\
&= \int [u_t^{target}(x | z) + \frac{\sigma_t^2}{2} \nabla \ln p_t(x | z)] \frac{p_t(x | z) p_{data}(z)}{p_t(x)} dz \\
&= u_t^{target}(x) + \frac{\sigma_t^2}{2} \nabla \ln p_t(x).
\end{aligned}$$

Here, $u_t^{target}$ is the marginal vector field
$$ u_t^{target}(x) = \int u_t^{target}(x | z) \frac{p_t(x | z) p_{data}(z)}{p_t(x)} dz, $$

and $\nabla \ln p_t(x) $ is the "marginal score function"

$$ \ln p_t(x) = \int \nabla \ln p_t(x | z) \frac{p_t(x | z) p_{data}(z)}{p_t(x)} dz. $$

Thus, the solution in the general case $u_t(x | t)$ is given a linear combination of the marginal vector field $u_t^{target}$ and the marginal score field $\nabla \ln p_t(x)$.

## Step 3 : Training a model

Since both the marginal vector field and the marginal score function depend on the unknown distribution $p_{data}$, we need to estimate them using samples $\{x_i\}_{i=1}^N \sim p_{data}$.

Let $u_t^{\theta}(x) \in \mathbb{R}^d$ be a $\theta$ - parameterized function that approximates the marginal vector field $u_t^{target}(x)$. The natural loss function for the training $u_t^{\theta}$ is a squared-error loss

$$\begin{aligned}
L(\theta) &= \mathbb{E}[ || u_t^{\theta}(x) - u_t^{target}(x) ||^2] \\
&= \mathbb{E}[ || u_t^{\theta}(x) - u_t^{target}(x | z) ||^2] + const. 
\end{aligned}$$

The expectation is taken over $t \sim \mathrm{Unif}[0, 1), z \sim p_{data}(z), x \sim p_t(x| z)$. Since the last expression depends only on samples of $p_{data}$, we can train the $u_t^{\theta}$ using the available data.

Similary, the marginal score function $\nabla \ln p_t(x)$ can also be approximated by training another parametrized function $s_t^{\theta}(x)$, trained using the loss
$$ L(\theta) = \mathbb{E}[ || s_t^{\theta} - \nabla \ln p_t(x | z)||^2 ]. $$

## Step 4.1 : Deterministic case

Training both $u_t^\theta$ and $s_t^\theta$ can be cumbersome. One way to ease the burden is to ignore the marginal score function by setting $\sigma_t = 0$ for all $t$. In the deterministic case, $u_t(x | z)$ does not depend on the marginal score function, and we therefore do not need to model $s_t^\theta$.

## Step 4.2 : Gaussian case

Another way to reduce the training burden is to use Gaussian probability path. In this setting, the marginal vector field and the marginal score functions satisfy the following relation

$$ u_t^{target}(x) = (\beta_t^2 \frac{\dot{\alpha_t}}{\alpha_t} - \dot{\beta_t} \beta_t) \nabla \ln p_t(x) + \frac{\dot{\alpha_t}}{\alpha} x $$

Once one of these quantities is successfully approximated, the other can be obtained using this relation.
