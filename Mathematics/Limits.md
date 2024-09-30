To find the limit of a function at a point, you can follow these steps:

- Substitute the value a into the function: Replace x with the value a in the function f(x).

- Calculate the result: Evaluate the expression to find the limit L.

The limit L may exist and be a real number, it may be infinity (∞), or it may not exist (undefined). Various techniques and rules, such as L'Hôpital's Rule or algebraic manipulations, can be applied to determine limits in more complex cases. The limit helps you understand the behavior of a function near a particular point.

## $\frac{d}{dx} : f \circ g, f \cdot g, \frac{f}{g}$

- Chain Rule: $f \circ g$: If you have a composite function f(g(x)), where f and g are differentiable functions, the derivative is found using the chain rule. The chain rule states that:
$$(f \circ g)'(x) = f'(g(x)) * g'(x)$$

- Product Rule: $f \cdot g$:
$$(f \cdot g)' = f'(x) \cdot g(x) + f(x) \cdot g'(x)$$

- Quotient Rule: $\frac{f(x)}{g(x)}$: 
$$(\frac{f}{g})'(x) = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{g(x)^2}$$


## L'Hopitals Rule

$$\lim _{x \rightarrow c} \frac{f(x)}{g(x)}=\lim _{x \rightarrow c} \frac{f^{\prime}(x)}{g^{\prime}(x)}$$


## Examples

Find limits for:

1. $lim_{x \rightarrow 0}\frac{sin(x)}{x} = $

Start with the function f(x) = sin(x)/x.

As x approaches 0, you'll notice that both the numerator (sin(x)) and the denominator (x) go to 0. This is an indeterminate form (0/0).

Apply L'Hôpital's Rule, which states that if you have an indeterminate form 0/0, you can find the limit by taking the derivative of the numerator and the derivative of the denominator and then evaluating the limit again.

$f'(x) = (sin(x))' = cos(x)$

$g'(x) = x' = 1$

$\lim_{x \rightarrow 0}\frac{sin(x)}{x} = \lim_{x \rightarrow 0}\frac{cos(x)}{1} = cos(0) = 1$

2. $\lim_{x \rightarrow 0} \frac{1-cos(x)}{x}$

$\frac{d}{dx}(1-cos(x)) = sin(x)$

$\lim_{x \rightarrow 0} \frac{1-cos(x)}{x} = \lim_{x \rightarrow 0} sin(x) = sin(0) = 0$

3. $\lim_{x \rightarrow 0} \frac{1-cos(x)}{x^2}$

Apply L'Hopital's Rule:

$\lim_{x \rightarrow 0} \frac{sin(x)}{2x}$

Apply L'Hopital's Rule:

$\lim_{x \rightarrow 0} \frac{cos(x)}{2} = \frac{1}{2}$

4. $\lim_{x \rightarrow 0} \frac{log(1 + x)}{sin(x)}$

$log(1+x)' = \frac{1}{1+x}$

Apply L'Hopital's Rule:

$\lim_{x \rightarrow 0} \frac{log(1 + x)}{sin(x)} = \lim_{x \rightarrow 0} \frac{\frac{1}{1+x}}{cos(x)} = 1$
