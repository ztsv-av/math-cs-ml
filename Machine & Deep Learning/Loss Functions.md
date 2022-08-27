# Loss Functions

*Note: cost function is the average across all values of loss functions for each example:*

$J(w,b) = \frac{1}{m}\sum_{i=1}^mL(f_{w,b}(x), y)$

## Squared Error Loss Function

$$L(w,b) = (\hat{y}^{(i)}-y^{(i)})^2$$

- $m$ - number of training examples, 
- $\hat{y}^{(i)} = f_{w,b}(x^i)$ - $i^{th}$ prediction, 
- $y^{(i)}$ - $y^{th}$ true value.

```
def mse_loss(y_true, y_pred):
    """
    mean squared error cost function.

    parameters
    ----------
        y_true : array
            array of true output values.

        y_pred : array
            array of predicted values for each true value.

    returns
    -------
        mse : float
            value of the mse
    """

    mse = np.substract(y_true, y_pred)
    mse = mse**2
    mse = np.mean(mse)

    return mse
```

## Logistic Loss Function

$$L(f_{w,b}(x^i), y^i) = \begin{cases} 
    -log(f_{w,b}(x^i)), & \text{if } y^i=1 \\ 
    -log(1 - f_{w,b}(x^i)), & \text{if } y^i=0 \end{cases}$$

$$or$$

$$L(f_{\mathbf{w},b}(\mathbf{x}^{(i)}), y^{(i)}) = (-y^{(i)} \log\left(f_{\mathbf{w},b}\left( \mathbf{x}^{(i)} \right) \right) - \left( 1 - y^{(i)}\right) \log \left( 1 - f_{\mathbf{w},b}\left( \mathbf{x}^{(i)} \right) \right)$$

*Note that $y^i$ can only take two values: 0 and 1*

For the first case, when $y^i = 1$:

![image](https://user-images.githubusercontent.com/73081144/185816661-8dbc7c4e-4c84-4d77-bd08-0ad470861c8f.png)

*Fig. 1. Logistic loss function: case if y=1*

For the first case, when $y^i = 0$:

![image](https://user-images.githubusercontent.com/73081144/185817281-b8330103-e419-484d-ac78-6debeb946037.png)

*Fig. 1. Logistic loss function: case if y=0*

```
def logistic_loss(y_true, y_pred):
    """
    computes logistic cost function.

    parameters
    ----------
        y_true : array
            array of true output values.

        y_pred : array
            array of predicted values for each true value.

    returns
    -------
        logistic : float
            value of the logistic cost function
    """

    logistic = -1 * y_true * np.log(y_pred) - (1 - y_true) * np.log(1 - y_pred)
    logistic = np.mean(logistic)

    return logistic
```
