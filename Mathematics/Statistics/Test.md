# Stationarity Tests

## ADF (Augmented Dickey-Fuller)

$$H_0: \text{The time series has a unit root (is non-stationary)}$$

If the null hypothesis is **rejected** (i.e., the **p-value is less than the chosen significance level**, such as 
$1\%$, $5\%$, or $10\%$), we conclude that the series is **stationary**.

## KPSS (Kwiatkowski-Phillips-Schmidt-Shin)

The null hypothesis in the KPSS (Kwiatkowski-Phillips-Schmidt-Shin) test is the opposite of the Augmented Dickey-Fuller (ADF) test. The KPSS test's null hypothesis is that the time series is stationary around a constant level or a deterministic trend (depending on the version of the test).

$$H_0: \text{The time series is stationary}$$

If the null hypothesis is **rejected** (i.e., the **p-value is less than the chosen significance level**), the test implies that the series is **non-stationary**.
