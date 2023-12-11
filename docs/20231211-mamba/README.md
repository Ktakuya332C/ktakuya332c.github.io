# A little memo on Mamba

I found it intriguing to read the paper presenting a new neural network architecture called [Mamba](https://arxiv.org/abs/2312.00752), which was shown to perform comparable to the well-known transformer network. Though most of the contents were easy to read, the most crucial part of the paper describing the S6 algorithm (Algorithm 2) was a little confusing. 

Here, I will describe the details of the algorithm with the subscript notation, instead of conventional matrix notation, to clarify its meaning. Because the algorithm described in Algorithm 2 and its implementation in [github repository](https://github.com/state-spaces/mamba) slightly differs in detail, I chose to rely primarily on the code to show the algorithm.

The algorithm accepts the following input and parameters.
- Input
  - $x$ in size $(L, D)$
- Parameters
  - $A$ in size $(D, N)$
  - $W^B$ in size $(D, N)$
  - $W^C$ in size $(D, N)$
  - $W^{\Delta1}$ in size $(D, R)$
  - $W^{\Delta2}$ in size $(R, D)$

The algorithm calculates the final output $y$ in size $(L, D)$ in the following procedure.

Step 1

$$\begin{aligned}
B_{ln} &= \sum_{d} x_{ld} W^B_{dn} \\
C_{ln} &= \sum_{d} x_{ld} W^C_{dn} \\
\Delta_{ld} &= \ln(1 + \exp(\sum_{r, d'} x_{ld'} W^{\Delta1}_{d'r} W^{\Delta2}_{rd}  )
\end{aligned}$$

Step2

$$\begin{aligned}
\bar{A}_{ldn} &= \exp(\Delta_{ld} A_{dn}) \\
\bar{B}_{ldn} &= \frac{\exp(\Delta_{ld} A_{dn}) - 1}{\Delta_{ld} A_{dn}} \Delta_{ld} B_{ln} \\
&\approx \Delta_{ld} B_{ln}
\end{aligned}$$

Step 3

$$\begin{aligned}
h_{0dn} &= \bar{B}_{0dn} x_{0d} \\
h_{(l+1)dn} &= \bar{A}_{ldn} h_{ldn} + \bar{B}_{ldn} x_{ld}
\end{aligned}$$

Step 4

$$\begin{aligned}
y_{ld} &= \sum_{n} C_{ln} h_{ldn}
\end{aligned}$$
