# Cheat Sheet of Flow Matching and Diffusion Models

I recently watched the videos of the following lecture.
- [MIT 6.S184 Introduction to Flow Matching and Diffusion Models](https://diffusion.csail.mit.edu/2025/index.html)

In this post, I will summarise key definitions and theorems presented in the lecture, so that I can recall the content easily later.

## Problem statement

Let $p_{data}(X)$ be a probability distribution over $X \in \mathbb{R}^d$. Given

- Samples: $\{x_i\}_{i=1}^N \sim p_{data}$
- Initial Distribution: $p_{init}(X)$ over $X \in \mathbb{R}^d$
- Diffusion Coefficient: $\sigma_t \in \mathbb{R}_{\geq 0}$ where time $t \in [0, 1]$

Find a time dependent vector field $u_t(x) \in \mathbb{R}^d$ such that the final distribution $X_1$of the stochastic differential equation (SDE)

$$\begin{aligned}
X_0 &\sim p_{init}(x) \\
dX_t &= u_t(X_t) dt + \sigma_t dW_t
\end{aligned}$$

matches with distribution $p_{data}(X)$.

The general stochastic case is called diffusion modeling, and the deterministic case ($\sigma_t = 0$) is called flow matching.

## Step 1 : Conditional Vector Field / Score Function
Let's start with one of the simplest cases where $p_{data}(X) = \delta(X - z)$. In this case, we can easily find a "conditional probability path", a time dependent probability distribution $p_t(x | z)$ over $\mathbb{R}^d$ that satisfies

$$\begin{aligned}
p_0(x | z) &= p_{init}(x) \\
p_1(x | z) &= p_{data}(x) = \delta(x - z)
\end{aligned}$$

In case of $p_{init} = \mathcal{N}(0, I_d)$, we can take a conditional probability path $p_t(x | z) = \mathcal{N}(\alpha_t z, \beta_t^2 I_d)$, which obviously satisfies the above conditions.

If we can find a vector field $u_t(x | z)$ such that the final distribution $X_1$ of the following SDE

$$\begin{aligned}
X_0 &\sim p_{init}(x) \\
dX_t &= u_t(X_t | z) dt + \sigma_t dW_t
\end{aligned}$$

matches with distribution $p_1(x | z) = \delta(x-z)$, that is the solution of the problem in this case. To find such a vector field, it is helpful to consider Fokker-Planck equation corresponding to the SDE

$$\begin{aligned}
\frac{\partial}{\partial t} p_t(x | z) &= - \mathrm{div} (u_t(x | z) p_t(x | z)) + \frac{\sigma_t^2}{2} \Delta p_t(x | z) \\
&= - \mathrm{div}(p_t(x | z) [u_t(x | z) - \frac{\sigma_t^2}{2} \nabla \ln p_t(x | z)])
\end{aligned}$$

It is relatively easy to find a solution $u_t^{target}(x | z)$ to this differential equation (See example 11 of the lecture note)

$$ \frac{\partial}{\partial t} p_t(x | z) = - \mathrm{div}(p_t(x | z) u_t^{target}(x | z)) $$

As a result, the vector field $u_t(x | z)$ is a linear combination of "conditional vector field" $u_t^{target}(x | z)$ and "conditional score function" $\nabla \ln p_t(x | z)$

$$ u_t(x | z) = u_t^{target}(x | z) + \frac{\sigma_t^2}{2} \nabla \ln p_t(x | z) $$

This is the solution to this simplest case.

## Step 2: Marginal Vector Field / Score Function

Let's consider the general case. In this case, we can find a "marginal probability path", a time dependent probability distribution $p_t(x)$ over $\mathbb{R}^d$ that satisfies

$$\begin{aligned}
p_0(x | z) &= p_{init}(x) \\
p_1(x | z) &= p_{data}(x)
\end{aligned}$$

by marginalizing $z$

$$ p_t(x) = \int p_t(x | z) p_{data}(z) dz $$

We can also find "marginal vector field" $u_t(x)$ such that the final distribution $X_1$ of the following SDE

$$\begin{aligned}
X_0 &\sim p_{init}(x) \\
dX_t &= u_t(X_t) dt + \sigma_t dW_t
\end{aligned}$$

matches the distribution $p_t(x)$, by considering the corresponding Fokker-Planck equation

$$\begin{aligned}
\frac{\partial}{\partial t} p_t(x) &= \int \frac{\partial}{\partial t} p_t(x | z) p_{data}(z) dz \\
&= \int [- \mathrm{div} (u_t(x | z) p_t(x | z)) + \frac{\sigma_t^2}{2} \Delta p_t(x | z)] p_{data}(z) dz \\
&= - \mathrm{div} (u_t(x) p_t(x)) + \frac{\sigma_t^2}{2} \Delta p_t(x) \\
\end{aligned}$$

$u_t(x)$ can be decomposed into a sum of two terms

$$\begin{aligned}
u_t(x) &= \int u_t(x | z) \frac{p_t(x | z) p_{data}(z)}{p_t(x)} dz \\
&= \int [u_t^{target}(x | z) + \frac{\sigma_t^2}{2} \nabla \ln p_t(x | z)] \frac{p_t(x | z) p_{data}(z)}{p_t(x)} dz \\
&= u_t^{target}(x) + \frac{\sigma_t^2}{2} \nabla \ln p_t(x)
\end{aligned}$$

one is "marginal vector field"

$$ u_t^{target}(x) = \int u_t^{target}(x | z) \frac{p_t(x | z) p_{data}(z)}{p_t(x)} dz $$

and the other is "marginal score function" $\nabla \ln p_t(x) $.

As a result, the solution of the general case is $u_t(x)$, a linear combination of the marginal vector field and the marginal score field.

## Step 3 : Training a model

Since marginal vector field and marginal score function depend on the unknown probability distribution $p_{data}$, we need to estimate both of them using the samples $\{x_i\}_{i=1}^N \sim p_{data}$.

Let $u_t^{\theta}(x) \in \mathbb{R}^d$ be a $\theta$ parametrized function that approximates the marginal vector field $u_t^{target}(x)$. The natural loss function for the training of the parametrized function $u_t^{\theta}$ is a squared error

$$\begin{aligned}
L(\theta) &= \mathbb{E}[ || u_t^{\theta}(x) - u_t^{target}(x) ||^2] \\
&= \mathbb{E}[ || u_t^{\theta}(x) - u_t^{target}(x | z) ||^2] + Const. 
\end{aligned}$$

where the expectation is over $t \sim \mathrm{Unif}[0, 1), z \sim p_{data}(z), x \sim p_t(x| z)$. Since the last expression doesn't depend on $p_{data}$ but only depend on samples of it, we can train the $u_t^{\theta}$ with the samples.

The marginal score function $\nabla \ln p_t(x)$ can also be approximated by training another parametrized function $s_t^{\theta}(x)$ with a loss function
$$ L(\theta) = \mathbb{E}[ || s_t^{\theta} - \nabla \ln p_t(x | z)||^2 ] $$

## Step 4.1 : Deterministic case

It is a little tedious to train both $u_t^\theta$ and $s_t^\theta$ separately. One way to ease up the burden is just ignoring the marginal score function by setting $\sigma_t = 0$ for all $t$. If $\sigma_t = 0$, then $u_t(x | z)$ doesn't depend on marginal score function at all, so we also don't need to care about $s_t^\theta$.

## Step 4.2 : Gaussian case

Another way to ease up the burden is to use gaussian probability path. In this case, the marginal vector field and the marginal score functions are in the following relation

$$ u_t^{target}(x) = (\beta_t^2 \frac{\dot{\alpha_t}}{\alpha_t} - \dot{\beta_t} \beta_t) \nabla \ln p_t(x) + \frac{\dot{\alpha_t}}{\alpha} x $$

Once we can approximate one of them successfully, we can approximate the other by using the above relation.