# ACF & PACF

## Interpretation of ACF and PACF

- Autocorrelation Function (ACF):
  1. The ACF measures how correlated the time series is with its past values (lags).
  2. If the ACF shows a sharp drop-off (cut-off) after a few lags, it suggests an MA model.
  3. If the ACF decays slowly (tails off), it indicates the presence of AR components.

- Partial Autocorrelation Function (PACF):
  1. The PACF measures the correlation of the time series with its lagged values, controlling for the values of all shorter lags.
  2. If the PACF shows a sharp cut-off after a certain lag, it suggests an AR model.
  3. If the PACF decays slowly, it suggests an MA component.

- General Guidelines for Model Selection:
    - AR(p) Model:
        1. The PACF shows a sharp cut-off after lag p (partial correlations drop to near zero after this point).
        2. The ACF decays slowly over time.
    - MA(q) Model:
        1. The ACF shows a sharp cut-off after lag q.
        2. The PACF decays slowly over time.
    - ARMA(p,q) Model:
        1. Both the ACF and PACF tail off gradually, indicating a mixture of AR and MA components.
