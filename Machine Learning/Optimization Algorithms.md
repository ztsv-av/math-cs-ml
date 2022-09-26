# Optimization Algorithms

Optimization algorithm is used to update parameters of a network.

## Gradient Descent

Gradient descent is used to minimize any function by taking partial derivatives of function's parameters. Our goal is to find values of parameters that minimize the function's value as much as possible. Cost function should decrease after every gradient descent iteration.

Goal outline:
- start with some $w,b$ (set $w=0, b=0$)
- keep changing $w,b$ to reduce $J(w,b)$
- until we settle at or near a minimum (may have >1 minimums).

![image](https://user-images.githubusercontent.com/73081144/183818928-4790b926-c665-4146-8f1c-bcef567272dd.png)

*Fig. 1. Gradient descent process. In the process, you look around and take a step to the direction of the steepest descent until you reach **local minima**.*

### Gradient Descent Algorithm

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

*Fig. 2. Gradient descent intuition.*

### Gradient Descent Intuition

Repeat until convergence:

- $w=w-\alpha \frac{\partial}{\partial w}J(w,b)$

- $b=b-\alpha \frac{\partial}{\partial b}J(w,b)$

Intuition example where there is only 1 parameter $w$:

- Derivative is the slope of the tangent line to the function $J$ at the point $w_1$. When tangent line is pointing upwards, the slope is positive, meaning that the derivative is $>0$. If you take $w=w-\alpha \times$(positive number), you decrease the value of $w$, moving it to the left,so the value of $J(w)$ will also decrease, going to the local minima. If the slope is negative, you add the derivative value * learning rate to the current value of w, increasing it.

![image](https://user-images.githubusercontent.com/73081144/183821778-ee8d7d45-38e2-4253-83a4-9f7f6abaeb88.png)

*Fig. 3. Role of derivative in gradient descent.*

If you are already at local minimum, then gradient descent will not change the value of a parameter, because the slope will be equal to 0.

![image](https://user-images.githubusercontent.com/73081144/183822800-9ad3234b-9469-4ef9-b6fa-4818646fb0eb.png)

*Fig. 4. Gradient descent at local minimum.*

The size of the step (value of the partial derivative) will also decrease after each iteration, because, usually, the slope will decrease as we descent towards a local minima.

![image](https://user-images.githubusercontent.com/73081144/183823461-b5e5fad9-0971-4261-9866-4cbd2c5b3d0b.png)

*Fig. 5. Role of a learning rate in gradient descent.*

## Adaptive Moment Estimation (Adam)

The Adam algorithm is almost the same as gradient descent, but it doesn't use a single global learning rate $\alpha$. It uses a different learning rates for every single parameter of your model.

![image](https://user-images.githubusercontent.com/73081144/191166838-38ac4b62-5e2d-46ca-a022-423216a48a1f.png)

*Fig. 6. Individual learning rate for each trainable parameter in Adam optimization algorithm.*

The intuition behind the Adam algorithm is, if a parameter $w_j$, or $b$ seems to keep on moving in roughly the same direction. This is what we see on the first example in the *Fig. 7*. But if it seems to keep on moving in roughly the same direction, let's increase the learning rate for that parameter. Let's go faster in that direction. Conversely, if a parameter keeps oscillating back and forth, this is what we see in the second example in the *Fig. 7*. Then let's not have it keep on oscillating or bouncing back and forth. Let's reduce $\alpha_j$ for that parameter a little bit.

![image](https://user-images.githubusercontent.com/73081144/191167193-3ef8b385-6b69-4e93-9c65-32bb17eb497c.png)

*Fig. 7. Adam intuition.*
