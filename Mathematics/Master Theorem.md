# Master Theorem

The *master theorem* for divide-and-conquer recurrences provides an asymptotic analysis (using Big O notation) for recurrence relations of types that occur in the analysis of many divide and conquer algorithms. The master method works only for following type of recurrences or for recurrences that can be transformed to following type. 

$T(n) = aT(n/b) + f(n)$, where $a >= 1$ and $b > 1$

There are following three cases: 
1. If $f(n) = O(n \cdot c)$ where $c < log_ba$ then $T(n) = \theta(n \cdot log_ba)$

2. If $f(n) = \theta(n \cdot c)$ where $c = log_ba$ then $T(n) = \theta(n \cdot c \cdot log_2n)$ 

3. If $f(n) = Ω(n^c)$ where $c > log_ba$ then $T(n) = \theta(f(n))$