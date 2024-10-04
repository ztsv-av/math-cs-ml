# ARIMA

If **underfitted**, tests will show that the **residuals** are not uncorrelated, meaning there is a **pattern** in them that can be predicted.

1. Interpretation of Coefficients:
- Constant (const): The coefficient is 0.5348, but the p-value is 0.131 (greater than 0.05), so it is not statistically significant at the 5% level. This implies that the constant term does not significantly contribute to the model.
- AR(1) coefficient (ar.L1): The coefficient is 0.9402 with a very small p-value (0.000), indicating that the AR(1) term is highly statistically significant. The large coefficient suggests a strong autoregressive relationship in the data.
- MA(1) coefficient (ma.L1): The coefficient is -0.3320, and the p-value (0.000) is also very small, indicating that the MA(1) term is highly statistically significant. This shows that the moving average component significantly contributes to explaining the series.
- Variance of residuals (sigma2): The variance is estimated at 0.9986, and its p-value is 0.000, meaning it is statistically significant.
2. Ljung-Box Test for Residual Autocorrelation:
- Ljung-Box (L1) (Q): The test statistic is 0.90 with a p-value of 0.34. Since the p-value is greater than 0.05, we fail to reject the null hypothesis of no autocorrelation in the residuals. This suggests that the model has sufficiently captured the time dependencies in the data, and there is no significant autocorrelation in the residuals.
3. Jarque-Bera Test for Normality:
- Jarque-Bera (JB): The test statistic is 2.13 with a p-value of 0.35. Since the p-value is greater than 0.05, we fail to reject the null hypothesis that the residuals are normally distributed. This indicates that the residuals do not show significant deviations from normality.
4. Heteroskedasticity Test:
- Heteroskedasticity (H): The H-statistic is 1.05 with a p-value of 0.63. Since the p-value is greater than 0.05, we fail to reject the null hypothesis that the residuals have constant variance (i.e., no heteroscedasticity). This suggests that the residuals have constant variance over time (homoscedasticity).
5. Null Hypotheses and Consequences:
- Null Hypothesis in the Heteroscedasticity Test: The null hypothesis is that the residuals are homoscedastic (i.e., they have constant variance). If we reject the null hypothesis and heteroscedasticity is present, the model's standard errors may be unreliable, leading to inaccurate confidence intervals and hypothesis tests. In this case, no heteroscedasticity was detected, so the model is reliable in this aspect.
- Null Hypothesis in the Jarque-Bera Test: The null hypothesis is that the residuals are normally distributed. In your case, the test suggests that the residuals are normally distributed, which is a positive result because normally distributed residuals help ensure that the model’s estimates are unbiased and efficient.

```
y_hat = res.fittedvalues
e = y - y_hat
```

- The residuals ($e = y - y_{hat}$) should show no patterns if the model is well-specified. Plot the residuals - should show a white noise. Plot a histogram to check if the residuals resemble a normal distribution.

## Interpretation of the Ljung-Box and Box-Pierce Test Results

- Null Hypothesis:
    1. The null hypothesis for both the Ljung-Box (LB) test and the Box-Pierce (BP) test is that the residuals are uncorrelated (i.e., they are white noise).
    2. We want the p-values to be greater than 0.05 to fail to reject the null hypothesis, which would indicate that the residuals do not exhibit significant autocorrelation (i.e., they are "white").
- Result Interpretation:
    1. Lag 1:
        - LB p-value: 0.344 (greater than 0.05).
        - BP p-value: 0.345 (greater than 0.05).
        - Conclusion: At lag 1, there is no significant autocorrelation in the residuals.
    2. Lags 2, 3, and 4:
        - At lag 2, the p-values for both tests drop to 0.008 (less than 0.05).
        - Similarly, at lag 3, the p-values are 0.022, and at lag 4, they are 0.045.
        - Conclusion: For lags 2 to 4, the tests indicate significant autocorrelation in the residuals, meaning the model may not have fully captured all the autocorrelation in the data.
    3. Lags 5 through 10:
        - From lag 5 onward, the p-values are greater than 0.05. This suggests that there is no significant autocorrelation in the residuals after lag 4.

## Next Steps

Since the model's residuals exhibit significant autocorrelation at lags $2$ through $4$, this implies that the current $\text{ARIMA}(1, 0, 1)$ model may not fully capture the time dependencies in the data.
