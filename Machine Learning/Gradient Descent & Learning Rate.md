# Gradient Descent

Gradient descent is used to minimize any function by taking partial derivatives of function's parameters. Our goal is to find values of parameters that minimize the function's value as much as possible. Cost function should decrease after every gradient descent iteration.

Goal outline:
- start with some $w,b$ (set $w=0, b=0$)
- keep changing $w,b$ to reduce $J(w,b)$
- until we settle at or near a minimum (may have >1 minimums).

![image](https://user-images.githubusercontent.com/73081144/183818928-4790b926-c665-4146-8f1c-bcef567272dd.png)

*Fig. 1. Gradient descent process. In the process, you look around and take a step to the direction of the steepest descent until you reach **local minima**.*

## Gradient Descent Algorithm

Repeat these two steps until convergence (until all parameters, for example $w,b$, no longer change much with each additional step):

1. Update parameter $w$ by taking the current value of $w$ and adjusting it a small amount:

    $w=w-\alpha \frac{\partial}{\partial w}J(w,b)$, where
      - $\alpha$ - learning rate, or measure of how big of a step you take down the gradient descent hill;
      - $\frac{\partial}{\partial w}J(w,b)$ - partial derivative term of the cost function $J$ to w. It tells you in which direction you want to the descent step. In combination with $\alpha$ it tells you the size and the direction of the step downhill.


2. Update parameter $b$ by taking the current value of $b$ and adjusting it a small amount:

    $b=b-\alpha \frac{\partial}{\partial b}J(w,b)$, where
      - $\alpha$ - learning rate, or measure of how big of a step you take down the gradient descent hill;
      - $\frac{\partial}{\partial b}J(w,b)$ - partial derivative term of the cost function $J$ to b. It tells you in which direction you want to the descent step. In combination with $\alpha$ it tells you the size and the direction of the step downhill.

Remember to update all parameters **simultaneously**.

![image](https://user-images.githubusercontent.com/73081144/183820365-96c8ab42-8a59-43b9-9d99-258b87f59d30.png)

## Gradient Descent Intuition

Repeat until convergence:

- $w=w-\alpha \frac{\partial}{\partial w}J(w,b)$

- $b=b-\alpha \frac{\partial}{\partial b}J(w,b)$

Intuition example where there is only 1 parameter $w$:

- Derivative is the slope of the tangent line to the function $J$ at the point $w_1$. When tangent line is pointing upwards, the slope is positive, meaning that the derivative is $>0$. If you take $w=w-\alpha \times$(positive number), you decrease the value of $w$, moving it to the left,so the value of $J(w)$ will also decrease, going to the local minima. If the slope is negative, you add the derivative value * learning rate to the current value of w, increasing it.

![image](https://user-images.githubusercontent.com/73081144/183821778-ee8d7d45-38e2-4253-83a4-9f7f6abaeb88.png)

If you are already at local minimum, then gradient descent will not change the value of a parameter, because the slope will be equal to 0.

![image](https://user-images.githubusercontent.com/73081144/183822800-9ad3234b-9469-4ef9-b6fa-4818646fb0eb.png)

The size of the step (value of the partial derivative) will also decrease after each iteration, because, usually, the slope will decrease as we descent towards a local minima.

![image](https://user-images.githubusercontent.com/73081144/183823461-b5e5fad9-0971-4261-9866-4cbd2c5b3d0b.png)

## Learning Rate

If $\alpha$ is too **small**, then gradient descent will take tiny steps towards the local minima, and the whole training process may be **slow**.

If $\alpha$ is too **large**, then gradient descent will take big steps towards the local minima, and the whole training process may be **faster**, but it might constantly **miss** local minima, because steps are too big to descent lower.

![image](https://user-images.githubusercontent.com/73081144/183822563-2d14f851-8315-4e61-a29a-8270b88cbcf9.png)

*Fig. 6. Learning rate: small and large.*

![image](https://user-images.githubusercontent.com/73081144/185274638-bbde62ce-9628-4821-aa43-b199c4cccba8.png)

*Fig. 7. Choosing proper learning rate.*

![image](https://user-images.githubusercontent.com/73081144/185274846-22525b16-89d1-45a8-974b-9376cf2cd9cb.png)

*Fig. 8. Trying out different values of learning rate.*

If you cost function is constantly increasing, try choosing very small learning rate, to see if it still getting larger and larger. If it is, then something is wrong with the model or data or code.

## Batch

"Batch" gradient descent means that each step of gradient descent uses all the training examples.
