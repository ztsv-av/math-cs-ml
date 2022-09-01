# **Gram Matrix**
 *Gram Matrix* is an inner product between vectorized feature maps i and j in layer l
 $$G_{ij}^l=\sum_kF_{ik}^l\cdot F_{jk}^l$$
 &nbsp;&nbsp;&nbsp;&nbsp; $G_{ij}^l$ - inner product between vectorized feature maps i and j in layer l,  
&nbsp;&nbsp;&nbsp;&nbsp; $F_{ik}^l$ - feature map i in layer l,  
&nbsp;&nbsp;&nbsp;&nbsp; $F_{jk}^l$ - feature map j in layer l.

```
style_layer = tf.constant([1,2,3,4,5,6,7,8], shape=(2,2,2))
# return [[[1, 2], [3, 4]],
#         [[5, 6], [7, 8]]]

A = tf.transpose(tf.reshape(style_layer, shape=(2,4)))
# return [[1, 5],
#         [2, 6],
#         [3, 7],
#         [4, 8]]

AT = tf.transpose(A)
# return [[1, 2, 3, 4],
#        [5, 6, 7, 8]]

G = tf.matmul(AT, A)
# return [[30, 70],
#         [70, 140]]

# You can use only this line of code to get the same result
G = tf.linalg.einsum('cij, dij->cd', style_layer, style_layer)
# return [[30, 70],
#         [70, 140]]
```