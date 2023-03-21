- What is the result of multiplying a matrix by a vector?

The result of multiplying a matrix by a vector is a new vector whose entries are obtained by taking linear combinations of the rows of the matrix with the corresponding entries of the vector.

More precisely, let A be an m x n matrix and let x be a column vector with n entries. Then the product Ax is a column vector with m entries, given by:

$Ax = [a11 a12 ... a1n] [x1] [a11x1 + a12x2 + ... + a1nxn]
[a21 a22 ... a2n] [x2] = [a21x1 + a22x2 + ... + a2nxn]
[... ... ... ...] [...]= [... ... ... ]
[am1 am2 ... amn] [xn] [am1x1 + am2x2 + ... + amnxn]$

In other words, the first entry of the product Ax is obtained by taking the dot product of the first row of A with the vector x, the second entry is obtained by taking the dot product of the second row of A with the vector x, and so on, until the last entry is obtained by taking the dot product of the last row of A with the vector x.

Note that the number of columns in A must match the number of entries in x in order for the multiplication to be defined.
