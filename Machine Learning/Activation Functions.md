# Activation Functions

We need activation function at each unit in a neural network. Otherwise, neural network will become no different than just linear regression. So this would defeat the entire purpose of using a neural network because it would then just not be able to fit anything more complex than the linear regression model (linear function of a linear function is itself a linear function).

![image](https://user-images.githubusercontent.com/73081144/189246556-fb8b3c6e-e576-4ca8-87bd-d163d41b3450.png)

*Fig. 1. Why use activation functions?*

If we use sigmoid activation function only at output layer (hidden layers still linear), then the model becomes equivalent to logistic regression.

![image](https://user-images.githubusercontent.com/73081144/189246775-e70bc27e-88f2-4a26-86aa-fb3fef655aa2.png)

*Fig. 2. Sigmoid activation function only at output layer.*

Activation functions are usually written as:

$g(z) = ...$ , where

- $z = \vec{w} * \vec{x} + b$

## Linear

$g(z) = z = \vec{w} * \vec{x} + b$

![image](https://user-images.githubusercontent.com/73081144/189245030-89d76023-c2f5-45f1-954c-895495d90e6a.png)

*Fig. 3. Linear function.*

Use linear activation function at output layer when dealing with regression problem ($y=+/-$).

## Sigmoid

$g(z) = \frac{1}{1 + e^{-z}}$

![image](https://user-images.githubusercontent.com/73081144/185814392-63bd4fa9-2952-4a4e-939c-f2ba861b5276.png)

*Fig. 4. Sigmoid function.*

Use sigmoid activation function at output layer when dealing with binary classification problem ($y=0/1$).

## Softmax

The softmax regression algorithm is a generalization of logistic regression, which is a binary classification algorithm to the **multiclass** classification contexts.

In both softmax regression and neural networks with softmax outputs, N outputs are generated and one output is selected as the predicted category. In both cases a vector $z$ is generated by a linear function which is applied to a softmax function. The softmax function converts $z$ into a probability distribution (see below). After applying softmax, each output will be between 0 and 1 and the outputs will add to 1, so that they can be interpreted as probabilities. The larger inputs will correspond to larger output probabilities.

$a_j=\frac{e^{z_j}}{\sum_{k=1}^Ne^{z_k}}=P(y=j|\vec{x})$

*Note: $a_1 + a_2 + ... + a_N = 1$*

![image](https://user-images.githubusercontent.com/73081144/189250686-3d0a6bcb-b8b3-49a5-ae89-799d08e543a2.png)

*Fig. 5. Idea behind softmax regression.*

![image](https://user-images.githubusercontent.com/73081144/191154666-dfbd2968-8561-4062-8066-e7dfc505adcf.png)

*Fig. 6. Forward propagation with softmax.*

## ReLU (Rectified Linear Unit)

$g(z) = max(0, z)$

![image](https://user-images.githubusercontent.com/73081144/189244867-e88256f1-d777-447d-97a6-a850859ef083.png)

*Fig. 7. ReLU function.*

**ReLU is the most common choise for hidden layers. This is because it is (1) fast to compute, and (2) it is not flat, so gradient descent will not get stuck and will be easier and faster to compute (activation function is a piece of what goes into computing the loss function). It provides faster learning among other activation functions. The "off" or disable feature of the ReLU activation ($>= 0$) enables models to stitch together linear segments to model complex non-linear functions.**

![image](https://user-images.githubusercontent.com/73081144/189248560-5a5073c6-8ca3-47db-830c-ca666c808f11.png)

*Fig. 8. Why use non-linear ReLU in hidden layers.*

Use ReLU activation function at output layer when dealing with regression problem where output value can only be $>=0$ ($y >= 0$).

![image](https://user-images.githubusercontent.com/73081144/191398781-0129887b-9583-43c5-99c2-1b606658ab4f.png)

*Fig. 9. Comparison between different activation functions.*