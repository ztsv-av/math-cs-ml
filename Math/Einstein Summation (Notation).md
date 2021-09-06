# **Einstein Notation *(or Einstein Summation)***
*Einstein summation* is a notational convention for simplifying expressions including summations of vectors, matrices, and general tensors.
```
x = tf.constant([1, 2, 3, 4], shape=(2, 2))
# return [[1, 2],
#         [3, 4]]

xT = tf.transpose(x)
# return [[1, 3],
#         [2, 4]]

tf.linalg.einsum('ij, ij->ij', x, x)
# return [[1, 4],
#         [9, 16]]
# it takes first input of x and multiplying it by the element in the same position in the second instance of x
# it is the same as squaring it

tf.linalg.einsum('ij, jk->ik', xT, x)
# return [[10, 14],
#         [14, 20]]
# it is the matrix multiplication of xT and x
# first matrix i rows j columns, second matrix j rows k columns
# output should have i rows and k columns ('...->ik' shows that)

tf.linalg.einsum('ij, jk->', xT, x)
# returns [58]
# same as reduce sum


```