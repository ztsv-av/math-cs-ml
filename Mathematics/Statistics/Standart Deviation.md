# Standart Deviation

The standard deviation of a sample is a measure of the spread or dispersion of the sample data around the sample mean. The formula for calculating the standard deviation of a sample is:

$$s = \sqrt{\frac{\sum{(x_i - \bar{x})^2}}{n - 1}}$$

where:

- $s$ is the sample standard deviation
- $x_i$ is the ith observation in the sample
- $\bar{x}$ is the sample mean
- $n$ is the sample size
- $\sum$ is the sum of all observations

Here, we first calculate the difference between each observation in the sample and the sample mean, then square each of these differences, add them up, divide the sum by (n-1), and take the square root of the result.

Note that the sample standard deviation is an estimate of the population standard deviation, which is a measure of the spread of the entire population. The formula for calculating the population standard deviation is similar to the above formula, except that we divide by the population size (N) instead of (n-1). However, in practice, we often don't have access to the entire population, and so we use the sample standard deviation as an estimate of the population standard deviation.
