# Information Criteria

Information criteria is a statistic that helps select models. It combines **goodness of fit** and **model complexity** into one number:

$$\text{IC} = \log{\sigma_\epsilon^2} + g(k, T)$$

- $\sigma_\epsilon^2$ - model error variance, **goodness of fit**;
- $g(k, T)$ - function increasing in the number of parameters ($k$) relative to the number of observations ($T$), **model complexity**.

1. Worse fit: $\sigma_\epsilon^2 \uparrow \to \uparrow \text{IT}$.
2. More parameters increases the penalty function: $\uparrow k \to \uparrow g(k,T) \to \uparrow \text{IC}$

## Steps

1. Estimate $\text{IC}$ for all models up to $\text{ARMA}(p_{max}, q_{max})$, where $p_{max} > p_{true}$ and $q_{max} > q_{true}$.
2. Select model with min $\text{IC}$.
3. Caution: ICs should be estimated over the same period (think lags).

## Popular ICs

1. Akaike (AIC):

$$g(k,T)=\frac{2k}{T}$$

2. Schwarz of Bayesian IC (BIC):

$$g(k, T) = \frac{k\log{T}}{T}$$

- Good when sample size is small.

3. Hannan-Quinn IC (HIC):

$$g(k, T)=\frac{2k\log{\log{T}}}{T}$$

## Cautions

- When $T \to \infty$, IC selects correct model with probability approaching to 1 (BIC, HIC).
- In finite samples no uniformly valid ranking of ICs exist.
- In practice and in small samples BIC is preffered over AIC, since it selects more parsimonious models (better for forecasting).

## Code

- Code
```
# estimate AR(1)-AR(3) and display information criteria
# estimate ICs
IC = sm.tsa.stattools.arma_order_select_ic(y, max_ar=5, max_ma=5, ic=['aic','bic','hqic'], trend='c')
# display optimal lags
print(f"min AIC at (p,q): {IC.aic_min_order}")
print(f"min BIC at (p,q): {IC.bic_min_order}")
print(f"min HQIC at (p,q): {IC.hqic_min_order}")
```
- Result
```
min AIC at (p,q): (2, 0)
min BIC at (p,q): (2, 0)
min HQIC at (p,q): (2, 0)
```
