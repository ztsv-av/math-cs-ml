# Karatsuba Algoritm

Karatsuba algorithm is used to multiply two large numbers with each other using divide-and-conquer technique. 

To understand the concept behind it, see example below:

x = 146123
y = 352120
a = 146000, b = 123 (taken from x)
c = 352000, d = 120

We can rewrite a and c as:  
a = $146 \cdot 10^3$, c = $352 \cdot 10^3$
So, x and y will look like this:

$x = 146 \cdot 10^3 + 123$  
$y = 352 \cdot 10^3 + 120$

We see that $10^3$ is equal to $10^{n/2}$, where n - number of digits in the original number. This means that we can rewrite the equation as follows:

$x = a \cdot 10^{n/2} + b$  
$y = c \cdot 10^{n/2} + d$  

$x \cdot y = (a \cdot 10^{n/2} + b)(c \cdot 10^{n/2})$
$x \cdot y = ac \cdot 10^{2(n/2} + (ad + bc) \cdot 10^{n/2} + bd$

Then we recursively call Karatsuba algorithm on these three numbers, until they are less than 10:

ac = karatsuba(a, c)  
bd = karatsuba(b, d)  
ad_plus_bc = karatsuba(a+b, c+d) - ac - bd

After that, we put those numbers in the equation and return the value.

Recursive calls example:
```
k(146123, 352120)

k(146, 352) = 51392                                         k(123, 120)         k(269, 472)

k(14, 35) = 490     k(6, 2) = 12        k(20, 37) = 740     .                   .
                                                            
k(1, 3) = 3                             k(2, 3) = 6         .                   .
k(4, 5) = 20                            k(0, 7) = 0         .                   .
k(5, 8) = 40                            k(2, 10) = 20       .                   .
```

```
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        half = n // 2
        a = x // (10 ** (half))  # left part of x
        b = x % (10 ** (half))  # right part of x
        c = y // (10 ** (half))  # left part of y
        d = y % (10 ** (half))  # right part of y
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a+b, c+d)-ac-bd
        return ac * (10 ** (2 * half)) + (ad_plus_bc * (10 ** half)) + bd
```