# Stationarity and Non-stationarity

## Differencing

To make the series stationary, we can apply differencing. This involves transforming the series by subtracting the previous observation from the current one:

$$\Delta y_t=y_t - y_{t-1}$$
​
## Consequences of Using Non-Stationary Data

For forecasting purposes (FCS), you can continue to use the series in its original form (levels), even if it's non-stationary. However, this has some consequences:

- Spurious regression: If the series is non-stationary, regression models can yield misleading or spurious results (significant relationships that don’t actually exist).
- Incorrect forecasts: Non-stationary series may lead to poor forecast accuracy since the model may struggle to capture the underlying trend or stochastic drift correctly.
- Unstable model coefficients: Model parameters estimated from non-stationary data can be unstable over time, leading to unreliable predictions.

## Stationarity Tests

### ADF (Augmented Dickey-Fuller)

**If we can model something with a random walk, that means that the data is not stationary.**

$$y_t = r\cdot y_{t-1} + \epsilon_t \text{(goes up because of r coeff., e.g. 1\% increase)}$$

$$H_0: \text{The time series has a unit root (is non-stationary)}$$

If the null hypothesis is **rejected** (i.e., the **p-value is less than the chosen significance level**, such as 
$1\%$, $5\%$, or $10\%$), we conclude that the series is **stationary**.

### KPSS (Kwiatkowski-Phillips-Schmidt-Shin)

The null hypothesis in the KPSS (Kwiatkowski-Phillips-Schmidt-Shin) test is the opposite of the Augmented Dickey-Fuller (ADF) test. The KPSS test's null hypothesis is that the time series is stationary around a constant level or a deterministic trend (depending on the version of the test).

$$H_0: \text{The time series is stationary}$$

If the null hypothesis is **rejected** (i.e., the **p-value is less than the chosen significance level**), the test implies that the series is **non-stationary**.

### DF-GLS (Dickey-Fuller Generalized Least Squares) Test

The **DF-GLS test** is an improvement of the **ADF (Augmented Dickey-Fuller)** test. It follows a similar idea but makes the test more powerful by first **detrending** the data.

- **ADF test** directly estimates the model without any transformation of the data.
- **DF-GLS** first **detrends** the data (i.e., removes any deterministic trend) before performing the unit root test. This detrending helps improve the power of the test, especially when the series has a trend.

#### DF-GLS Model

Before testing for the unit root, the time series is transformed by subtracting its estimated trend, making the data closer to stationary:

$$
y_t^{detrended} = y_t - \text{Trend component}
$$

Then the DF-GLS test applies the same principle as the ADF test but on the **detrended** data:

$$
y_t^{detrended} = r \cdot y_{t-1}^{detrended} + \epsilon_t
$$

Where $y_t^{detrended}$ is the time series after removing the trend.

#### Null Hypothesis $H_0$
- $H_0$: The series has a **unit root** (is non-stationary).
  
If the **null hypothesis is rejected** (i.e., the p-value is less than a chosen significance level, like 1%, 5%, or 10%), it means the series is stationary after removing the trend.

#### Key Points
1. **DF-GLS** is more powerful than the ADF test when the series has a trend because it first removes the trend before testing for stationarity.
2. Like the ADF test, the DF-GLS test also has the null hypothesis that the series is **non-stationary** (has a unit root).
3. **If you reject the null hypothesis**, it means the series is **stationary** (without a unit root), even after accounting for any deterministic trends.