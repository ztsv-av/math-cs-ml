# Overfitting & Undefitting

**Undefitting** - a model does not fit the training data very well. There is a trend in data that the algorithm is unable to capture. Another term is - the algorithm has **high bias**. This means that algorithm thinks that the function is, for example, linear, where in reality it looks like a log-function.


**Overfitting** - overfitting happens when a model fits data too well, meaning that it might not generalize to examples that it hasn't seen before. Another term is that an algorithm has **high variance**. The algorithm is trying very-very hard to fit every training example, which is bad for generalization.

The goal of machine learning is to find a model that neither overfits or underfits/ a model has nor high bias nor high variance.

![image](https://user-images.githubusercontent.com/73081144/187054067-bd39325c-56c6-419b-bef0-86e680dd43e4.png)

*Fig. 1. Underfitting, generalization and overfitting. Regression example.*

![image](https://user-images.githubusercontent.com/73081144/187054111-fec7a951-6262-46a8-8eef-c6f320c53f25.png)

*Fig. 2. Underfitting, generalization and overfitting. Classification example.*

## Addressing Overfitting

- collect more data;
- see if you can use fewer/more features; *a lot of features + insufficient data = overfit*;
- reduce size of parameters - use regularization.
