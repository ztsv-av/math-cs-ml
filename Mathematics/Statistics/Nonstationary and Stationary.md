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
