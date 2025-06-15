# Start using Docsify on my blog

I started using docsify on my blog because it is easy to write math and code without any tricks or tweasks usually needed to write both in one post in another static site genrators. I was using custom-built static site generator before, but the commbination of docsify and docsify-katex gives me a easy 30 lines alternative.

For example, I can write a code block just like I would write in Github.

```
import os
print(os.environ.get("HELLO", default="WORLD"))
```

After integrating [docsify-katex](https://github.com/upupming/docsify-katex), I can write mathematical formulaes just like I would write in LaTeX.
$$\begin{aligned}
\int^{1}_{0} x^2 dx &= [\frac{1}{3} x^3]^1_0 \\
&= \frac{1}{3}
\end{aligned}$$
