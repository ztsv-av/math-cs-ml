## Operations

- Matrix Addition: Given two matrices A and B of the same size (i.e., they have the same number of rows and the same number of columns), their sum A + B is the matrix obtained by adding the corresponding entries of A and B. Geometrically, this operation corresponds to the vector addition of the column vectors of A and B.

- Matrix Multiplication: Given two matrices A and B, the product AB is defined only if the number of columns of A is equal to the number of rows of B. The resulting matrix AB is obtained by taking linear combinations of the columns of B with the coefficients given by the entries of the corresponding row of A. Geometrically, this operation corresponds to a composition of linear transformations.

- Matrix Inverse: Given a square matrix A, its inverse A^-1 is a matrix such that AA^-1 = A^-1A = I, where I is the identity matrix. In other words, the inverse of a matrix undoes the effect of the matrix on a vector, and it exists only if the matrix is invertible (i.e., its determinant is not zero). Geometrically, the inverse of a matrix corresponds to the inverse transformation that undoes the effect of the original transformation.


# Rank

The rank of a matrix A is the maximum number of linearly independent rows (or columns) of A. In other words, it is the dimension of the subspace spanned by the rows (or columns) of A. The rank of a matrix provides information about the dimension of the range of the linear transformation associated with A, and it also has implications for the existence and uniqueness of solutions to systems of linear equations involving A. It is useful to know the rank: we have a chance of solving a system of linear equations: when the rank equals the number of variables we may be able to find a unique solution.

Instead of "not made of" we say they are linearly independent which is an important idea.

- Linear means we can multiply by a constant, but no powers or other functions. The constant can be any real number (0, 1, any whole number, fraction, negatives, etc.).

- Dependence means they depend on each other, in other words we can add some up (after multiplying by a constant) to make another one.

**When vectors are linearly independent and span a whole space we say they are a "basis" of that space.**

*Note: space is a general term covering 1, 2, 3 or higher dimensions, but we often call 2D space a **plane**.*

- For a square matrix the determinant can help: a non-zero determinant tells us that all rows (or columns) are linearly independent, so it is "full rank" and its rank equals the number of rows.

- The rank can't be larger than the smallest dimension of the matrix.

- When the rank equals the smallest dimension it is called "full rank", a smaller rank is called "rank deficient".

- The rank is at least 1, except for a zero matrix (a matrix made of all zeros) whose rank is 0.


## Change of Basis on a Matrix

A change of basis on a matrix refers to the process of expressing the same linear transformation (specified by the matrix) in terms of different bases of the domain and range spaces. More precisely, suppose that A is an n x m matrix that represents a linear transformation T: R^m -> R^n with respect to the standard bases of R^m and R^n. Suppose also that we have a change of basis matrix P that transforms the standard basis of R^m into a new basis B for R^m, and a change of basis matrix Q that transforms the standard basis of R^n into a new basis C for R^n. Then, we can obtain the matrix representation of the same linear transformation T with respect to the bases B and C by computing the product Q^(-1)AP.

Geometrically, a change of basis on a matrix corresponds to changing the coordinate systems in the domain and range spaces, while keeping the same underlying linear transformation. It allows us to represent the same linear transformation with respect to different bases, which can be useful for various applications, such as diagonalization of matrices, optimization problems, and data analysis.
