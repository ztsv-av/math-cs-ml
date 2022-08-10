# Cost Functions

## Squared Error Cost Function

$J(w,b) = \frac{1}{2m}\sum^{m}_{i=1}(\hat{y}^{(i)}-y^{(i)})^2$, where

- $m$ - number of training examples, 
- $\hat{y}^{(i)}$ - $i^{th}$ prediction, 
- $y^{(i)}$ - $y^{th}$ true value.

```
def mse_cf(y_true, y_pred):
    """
    Mean squared error function.

    parameters
    ----------
        y_true : array
            Array of true output values.

        y_pred : array
            Array of predicted values for each true value.

      returns
      -------
        mse : float
            value of the mse
    """

    mse = np.substract(y_true, y_pred)
    mse = np.mean(mse)
    mse = mse / 2

    return mse
```
