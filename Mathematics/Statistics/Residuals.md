# Residuals

## What are Residuals?

**Residuals** represent the difference between the actual observed values and the values predicted by a model. Mathematically, residuals are calculated as:

$$ e = y - \hat{y} $$

Where:
- $e$: Residual (error term)
- $y$: Actual observed value
- $\hat{y}$: Predicted value from the model

Residuals measure how well the model's predictions fit the actual data. Ideally, residuals should be randomly distributed around zero, indicating that the model has captured the underlying patterns of the data accurately. Large or systematic patterns in the residuals can indicate model misspecification or the need for improvement.

## Ljung-Box Test for Residual Autocorrelation

- **Null Hypothesis ($H_0$):** There is no autocorrelation in the residuals.
- **Test Statistic:** 0.90
- **p-value:** 0.34
- **Decision:** Since the p-value is greater than 0.05, we fail to reject the null hypothesis.
- **Conclusion:** This suggests that the model has sufficiently captured the time dependencies in the data, and there is no significant autocorrelation in the residuals.

## Jarque-Bera Test for Normality

- **Null Hypothesis ($H_0$):** The residuals are normally distributed.
- **Test Statistic:** 2.13
- **p-value:** 0.35
- **Decision:** Since the p-value is greater than 0.05, we fail to reject the null hypothesis.
- **Conclusion:** This indicates that the residuals do not show significant deviations from normality. In this test, skewness should be close to 0. Kurtosis reflects how flat or peaked the normal distribution is, while skewness measures the asymmetry or "pushed" nature of the distribution (i.e., how fat the tails are).

## Heteroscedasticity Test

- **Null Hypothesis ($H_0$):** The residuals have constant variance (homoscedasticity).
- **Test Statistic (H-statistic):** 1.05
- **p-value:** 0.63
- **Decision:** Since the p-value is greater than 0.05, we fail to reject the null hypothesis.
- **Conclusion:** This suggests that the residuals exhibit constant variance over time, meaning no heteroscedasticity is detected, and the model is reliable in this aspect.

## Null Hypotheses and Consequences

### Null Hypothesis in the Heteroscedasticity Test

- **$H_0$:** The residuals are homoscedastic (i.e., they have constant variance).
- **Consequence of Rejecting $H_0$:** If heteroscedasticity is present, the model’s standard errors may be unreliable, leading to inaccurate confidence intervals and hypothesis tests.
- **Current Result:** No heteroscedasticity was detected, suggesting the model is reliable in terms of residual variance.

### Null Hypothesis in the Jarque-Bera Test

- **$H_0$:** The residuals are normally distributed.
- **Consequence of Rejecting $H_0$:** If the residuals deviate from normality, it can indicate model misspecification, which may result in biased or inefficient estimates.
- **Current Result:** The test suggests that the residuals are normally distributed, which is desirable for ensuring unbiased and efficient model estimates.

## Additional Checks for Residuals

- **Residual Patterns:** Residuals (calculated as $e = y - \hat{y}$) should show no patterns if the model is well-specified.
- **White Noise Check:** Plot the residuals over time to check for randomness (white noise).
- **Histogram of Residuals:** A histogram can help visually verify whether the residuals resemble a normal distribution.
