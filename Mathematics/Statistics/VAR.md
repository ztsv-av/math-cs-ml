# VAR

## Companion Form

Companion forms are used to make the VAR formula easier. It converts VAR($m$) to VAR(1).

Let's say $m=2$ number of variables and we have VAR(2). The companion form for VAR(1) would be VAR(1) with $m=4$.

$$\begin{bmatrix}y_{1t}\\y_{2t}\end{bmatrix}=\begin{bmatrix}\phi^1_{11}&\phi^1_{12}\\\phi^1_{21}&\phi^1_{22}\end{bmatrix}\begin{bmatrix}y_{1t-1}\\y_{2t-1}\end{bmatrix}+\begin{bmatrix}\phi^2_{11}&\phi^2_{12}\\\phi^2_{21}&\phi^2_{22}\end{bmatrix}\begin{bmatrix}y_{1t-2}\\y_{2t-2}\end{bmatrix}+\begin{bmatrix}e_{1t}\\e_{2t}\end{bmatrix}$$

$$\to$$

$$\begin{bmatrix}y_{1t}\\y_{2t}\\y_{1t-1}\\y_{2t-1}\end{bmatrix}=\begin{bmatrix}\phi^1_{11}&\phi^1_{21}&\phi^2_{11}&\phi^2_{12}\\\phi^1_{21}&\phi^1_{22}&\phi^2_{21}&\phi^2_{22}\\1&0&0&0\\0&1&0&0\end{bmatrix}\begin{bmatrix}y_{1t-1}\\y_{2t-1}\\y_{1t-2}\\y_{2t-2}\end{bmatrix}+\begin{bmatrix}e_{1t}\\e_{2t}\\0\\0\end{bmatrix}$$

## Expressing VAR in Past Error Terms

$$y_t=Ay_{t-1}+\epsilon_t$$

$$y_t=(I-AL)^{-1}\epsilon_t$$

$$y_t=((AL)^0+(AL)^1+(AL)^2+\dots)\epsilon_t$$

$$y_t = \epsilon_t + A\epsilon_{t-1} + A^2\epsilon_{t-2} + \dots$$

### Impulse Response Analysis

#### Errors are NOT Cross-Correlated

Shocking economy in 1 term (interest rate):

$$t=0: \epsilon_t=\begin{bmatrix}\epsilon_{1t}\\\epsilon_{2t}\\\epsilon_{3t}\end{bmatrix}=\begin{bmatrix}0\\0\\\epsilon_{3t}\end{bmatrix}, y_0=\begin{bmatrix}0\\0\\\epsilon_{3t}\end{bmatrix}+\begin{bmatrix}\text{inflation}\\\text{rGDP}\\\text{IR}\end{bmatrix}$$

$$t=1: y_{1}=\epsilon_1+A\epsilon_0=A\begin{bmatrix}0\\0\\\epsilon_{30}\end{bmatrix}=\begin{bmatrix}a_{13}\epsilon_{30}\\a_{23}\epsilon_{30}\\a_{33}\epsilon_{30}\end{bmatrix}$$

$$t=2: y_{2}=A^2\begin{bmatrix}0\\0\\\epsilon_{30}\end{bmatrix}$$

Plot matrix values for each time stamp $t$ and for each variable $1,2,3$.

#### Errors ARE Cross-Correlated

$$\epsilon_t=\begin{bmatrix}\epsilon_{t1}\\\epsilon_{t2}\\\epsilon_{t3}\end{bmatrix}=P\cdot v_t$$

- $P$: Cholesky decomposition of $\Sigma$, variance-covariance matrix of $\epsilon_t$
- $v_t$: Structural shocks, follows $N(0,1)$.
- $\epsilon_t$: 

**Univariate example**:

$$\epsilon_t \sim N(0, 2.5) \iff v_t=\frac{\epsilon_t}{\sqrt{2.5}}, v_t\sim N(0,1)$$

$$\text{Then: }\epsilon_t=\sqrt{2.5}v_t, \text{where }\sqrt{2.5} \text{ is an element of }P\text{ in multivariate case}$$

**Multivariate example**:

$$y_t=Pv_t+APv_{t-1}+A^2Pv_{t-2}$$

$$\epsilon_t=\begin{bmatrix}\epsilon_{1t}\\0\\0\end{bmatrix}$$

$$t=0: y_0=P\begin{bmatrix}v_{10}\\0\\0\end{bmatrix}=\begin{bmatrix}p_{11}&0&0\\p_{21}&p_{22}&0\\p_{31}&p_{32}&p_{33}\end{bmatrix}\begin{bmatrix}v_{10}\\0\\0\end{bmatrix}=\begin{bmatrix}p_{11}v_{10}\\p_{21}v_{10}\\p_{31}v_{10}\end{bmatrix}$$

$$t=1: y_{1}=Pv_1+APv_0$$

#### Choice of Decomposition is Important

$$\begin{bmatrix}\text{inflation}\\\text{rGDP}\\\text{IR}\end{bmatrix}=\dots+\begin{bmatrix}p_{11}&0&0\\p_{21}&p_{22}&0\\p_{31}&p_{32}&p_{33}\end{bmatrix}\begin{bmatrix}v_{1t}\\v_{2t}\\v_{3t}\end{bmatrix}$$

$$\begin{bmatrix}p_{11}&0&0\\p_{21}&p_{22}&0\\p_{31}&p_{32}&p_{33}\end{bmatrix}\begin{bmatrix}v_{1t}\\v_{2t}\\v_{3t}\end{bmatrix}=\begin{bmatrix}\epsilon_{t1}\\\epsilon_{t2}\\\epsilon_{t3}\end{bmatrix}$$

If `IR` blows up, it takes one $t$ (next timestamp) to impact `inflation` and `rGDP`. However, if `inflation` blows up, `IR` will be impacted immediately. Thus, **ordering of variables is important**. First in order means it affects all other variables immediately.

#### Why Impulse Response Analysis?

What share of forecast error variance for horizon `h` is due to uncertainty driven by a specific shock. There we compute matrix $\Psi$. $\Psi_{h_{it}}$ element of resulting matrix represents the contribution of $j$-th variable in explaining the $h$-step ahead forecast error variance for $i$-th variable $y_i$.

## Advanced VAR Models

