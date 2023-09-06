## Taylor Expansion (Taylor Series)

The Taylor expansion (or Taylor series) of a function at a point is a way to represent a function as an infinite sum of terms involving its derivatives. It's a useful tool in calculus for approximating functions, particularly when you want to analyze a function's behavior near a specific point. The Taylor expansion of a function f(x) at a point a is typically written as:

$$f(x) = f(a) + f'(a)(x - a) + \frac{f''(a)(x - a)^2}{2!} + \frac{f'''(a)(x - a)^3}{3!} + ...$$

$$=$$

$$f(x) = \sum^\infty_{n=0}\frac{f^{(n)}(a)}{n!}(x-a)^n$$

, where:
- $f^{(n)}(a)$ - $n_{th}$ derivative of f at point a
- a - real or complex number

This means that as x gets closer and closer to the value a, the function f(x) approaches the limit L.


## Maclaurin Series

Same as Taylor Series, but a = 0.

$$f(x) = \sum_{n=0}^\infty\frac{f^{(n)}(0)}{n!}x^n$$