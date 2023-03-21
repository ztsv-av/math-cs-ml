# Hölder's Inequality

Let $p, q > 1, \frac{1}{p} + \frac{1}{q} = 1$. Then, $\forall$ $u$ $\in$ $R^{n}$ and $\nu$ $\in$ $\R^n$:

$|\sum_{i=1}^{n}u_i\nu_i| \le ||u||_{p}||\nu||_q$ 

# Convergence of Newton's Method

Suppose that $f$ is continous real-valued function with continous second derivative $f''$, defined on closed interval $I_\gamma = [\epsilon - \gamma; \epsilon + \gamma], \gamma > 0$ such that $f(\epsilon)=0$ and $f''(\epsilon) \neq 0$. Suppose there exists $A>0$, where

$\frac{f''(x)}{f(y)} \le A, \forall x,y \in I_\gamma$

If $|\epsilon - x_0| \le h$, where h is the smaller of $\gamma$ and $\frac{1}{A}$, then the sequence $(x_k)$ defined by Newton's method converges quadratically to $\epsilon$.
