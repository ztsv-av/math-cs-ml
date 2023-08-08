 - What is the geometric interpretation of a vector of $R^p$ and $(n,p)$-matrix as a linear mapping from $R^p$ to $R^n$?

In linear algebra, a vector in R^p represents a point in p-dimensional Euclidean space. Geometrically, we can visualize a vector as an arrow starting at the origin (0,0,..,0) and ending at the point represented by the vector. The length of the arrow represents the magnitude of the vector, and the direction of the arrow represents the direction of the vector.

On the other hand, an (n,p)-matrix represents a linear mapping from R^p to R^n. This means that it maps each vector in R^p to a vector in R^n in a linear way. Geometrically, we can think of this mapping as a transformation of the p-dimensional Euclidean space into the n-dimensional Euclidean space. The matrix specifies how each vector in the original space is transformed into a new vector in the transformed space.

More specifically, let A be an (n,p)-matrix, and let x be a vector in R^p. Then the product Ax gives us a new vector in R^n that is the result of applying the linear mapping specified by A to the vector x. Geometrically, we can think of this as taking the arrow representing x in the p-dimensional space, transforming it according to the linear transformation specified by A, and ending up with a new arrow representing the resulting vector in the n-dimensional space.

For example, if A is a 2x2 matrix and x is a vector in R^2, then Ax gives us a new vector in R^2 that is the result of applying the linear transformation specified by A to the vector x. **Geometrically, we can think of this as transforming the arrow representing x in the plane, according to the linear transformation specified by A, and ending up with a new arrow representing the resulting vector in the plane.**

- Recall the classical operations on matrices: addition, multiplication, inverse and what their interpretations are.
  
Matrix Addition: Given two matrices A and B of the same size (i.e., they have the same number of rows and the same number of columns), their sum A + B is the matrix obtained by adding the corresponding entries of A and B. Geometrically, this operation corresponds to the vector addition of the column vectors of A and B.

Matrix Multiplication: Given two matrices A and B, the product AB is defined only if the number of columns of A is equal to the number of rows of B. The resulting matrix AB is obtained by taking linear combinations of the columns of B with the coefficients given by the entries of the corresponding row of A. Geometrically, this operation corresponds to a composition of linear transformations.

Matrix Inverse: Given a square matrix A, its inverse A^-1 is a matrix such that AA^-1 = A^-1A = I, where I is the identity matrix. In other words, the inverse of a matrix undoes the effect of the matrix on a vector, and it exists only if the matrix is invertible (i.e., its determinant is not zero). Geometrically, the inverse of a matrix corresponds to the inverse transformation that undoes the effect of the original transformation.

These operations are fundamental to matrix algebra, and they have important applications in various fields such as physics, engineering, computer science, and economics.

- Recall what the rank of a matrix is. Apply a change of basis on a matrix and explain what it means.

Rank of a Matrix:
The rank of a matrix A is the maximum number of linearly independent rows (or columns) of A. In other words, it is the dimension of the subspace spanned by the rows (or columns) of A. The rank of a matrix provides information about the dimension of the range of the linear transformation associated with A, and it also has implications for the existence and uniqueness of solutions to systems of linear equations involving A.

Change of Basis on a Matrix:
A change of basis on a matrix refers to the process of expressing the same linear transformation (specified by the matrix) in terms of different bases of the domain and range spaces. More precisely, suppose that A is an n x m matrix that represents a linear transformation T: R^m -> R^n with respect to the standard bases of R^m and R^n. Suppose also that we have a change of basis matrix P that transforms the standard basis of R^m into a new basis B for R^m, and a change of basis matrix Q that transforms the standard basis of R^n into a new basis C for R^n. Then, we can obtain the matrix representation of the same linear transformation T with respect to the bases B and C by computing the product Q^(-1)AP.

Geometrically, a change of basis on a matrix corresponds to changing the coordinate systems in the domain and range spaces, while keeping the same underlying linear transformation. It allows us to represent the same linear transformation with respect to different bases, which can be useful for various applications, such as diagonalization of matrices, optimization problems, and data analysis.


##  Recall what is an inner product in a Euclidean space

In a Euclidean space, an inner product is a bilinear operation that takes two vectors as input and produces a scalar as output. More specifically, an inner product on a real vector space V is a function ⟨·,·⟩: V × V → R that satisfies the following properties for all vectors u, v, and w in V, and all scalars c:

Symmetry: ⟨u, v⟩ = ⟨v, u⟩

Linearity in the first argument: ⟨cu + v, w⟩ = c⟨u, w⟩ + ⟨v, w⟩

Positive definiteness: ⟨u, u⟩ ≥ 0, with equality if and only if u = 0.

Geometrically, the inner product of two vectors u and v represents the cosine of the angle between them, scaled by their magnitudes. It is a measure of how much the vectors are aligned or orthogonal to each other. The properties of the inner product also allow us to define concepts such as norm, distance, orthogonality, and angle in a Euclidean space.

Examples of inner products in Euclidean spaces include the dot product on R^n and the standard inner product on the space of continuous functions with square-integrable norm.

Inner products have many applications in mathematics and its applications, including geometry, physics, optimization, signal processing, and machine learning.


## Recall what is the orthogonal projection onto a linear subspace
 
In linear algebra, the orthogonal projection onto a linear subspace W of a vector space V is a linear transformation P: V → W that maps every vector in V onto its nearest point in W, measured with respect to the Euclidean norm induced by an inner product on V.

More formally, the orthogonal projection P is defined as follows:

For any vector v in V, we decompose it into a sum of two vectors, one in W and the other in W's orthogonal complement W⊥, i.e., v = w + w', where w is in W and w' is in W⊥.
Then, the orthogonal projection of v onto W is defined as the vector Pv that lies entirely in W and is closest to v in the sense of Euclidean distance, i.e., ||v - Pv|| ≤ ||v - w'|| for any w' in W.
The orthogonal projection onto a linear subspace has many important properties and applications in mathematics and its applications. For example:

The projection operator P is idempotent, i.e., P^2 = P, meaning that applying the projection twice gives the same result as applying it once.
The projection operator P is self-adjoint, i.e., ⟨Pv, w⟩ = ⟨v, Pw⟩ for all v, w in V, where ⟨·, ·⟩ denotes the inner product on V.
The projection operator P is the identity on W, meaning that Pv = v for all v in W.
The projection operator P is uniquely determined by its range, which is the subspace W.
The orthogonal projection is used in various areas such as image processing, machine learning, physics, and engineering to extract important features and reduce noise.


##  Give the expression of the projection matrix onto the linear span of linearly independent vectors $v_1, v_2, ..., v_d$ (that are not necessarily orthonormal)

Let V be a linear subspace of a Euclidean space and let $v_1, v_2, ..., v_d$ be a set of linearly independent vectors in V. The orthogonal projection matrix $P$ onto the subspace spanned by $v_1, v_2, ..., v_d$ is given by:

$P = A(A^TA)^{-1}A^T$

where A is the matrix whose columns are the vectors $v_1, v_2, ..., v_d$. In other words,

$P = [v_1 v_2 ... v_d][v_1 v_2 ... v_d]^{-1}$

where $[v_1 v_2 ... v_d]$ is a $d x d$ matrix whose columns are the vectors $v_1, v_2, ..., v_d$, and $[v_1 v_2 ... v_d]^{-1}$ is the inverse of this matrix, which exists since the vectors are linearly independent.

To use this projection matrix to project a vector $x$ onto the subspace $V$, we simply compute the product $Px$, which gives us the orthogonal projection of $x$ onto $V$.


## Do you know that symmetric matrices can be diagonalized? Would you be able to compute their eigenvalues and their eigenvectors?

Symmetric matrix is symmetric along its diagonal, meaning $A^T = A$. Properties:
- real eigenvalues;
- eigenvectors corresponding to the eigenvalues  that are orthogonal;
- must be diagonazible.

A matrix that is diagonalizable means there exists a diagonal matrix $D$ whose diagonal entries are the eigenvalues of A (all the entries outside of the diagonal are zeros), such that $P^{-1}AP = D$, where $P$ is an invertible real orthogonal matrix. We can also say that a matrix is diagonalizable if the matrix can be written in the form $A = PDP^{-1}$.


## Eigenvalues and eigenvectors

The eigenvectors of matrix A are the vectors whose directions don’t change after A is applied to it. The direction is not changed, but the vectors can be scaled. This shows the non-triviality of this property. Real eigenvalues indicate stretching or scaling in the linear transformation, unlike complex eigenvalues, which don’t have a “size.”
The set of all the eigenvalues of a matrix is called a spectrum.
