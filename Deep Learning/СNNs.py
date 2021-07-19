# The smaller the stride, the more detailed the processing
# If you have 2x2 Pooling window and 2x2 Stride window => height and width will be halved. e.x.:
#   Image (4, 2)         Pooing window 2x2
#   _______                 _______
#   |1   2|                 |1   2|        _____
#   |2   1|                 |2   1| ---->  |1.5|
#   |     |   Stride 2x2    -------        |   | (2, 1)
#   |0   1|   --------->    |0   1| ---->  |0.5| 
#   |0   1|                 |0   1|        -----
#   -------                 -------

# Upsampling is increasing height and width of the feature map
#   In TensorFlow:
#       Simple Scaling - UpSampling2D(size, data_format, interpolation):
#           Scales up the image. Two types of Scailing:
#               Nearest - copies value from nearest pixel.
#               Bilinear - linear interpolation from nearby pixels (average of nearby values).
#           size = (2, 2) - meaning 1 pixel will be turned to (2, 2) or 4 pixels;
#           data_format - 'channels_first', 'channels_last' or None;
#           interpolation - type of scailing.
#       Transposed Convolution  (Deconvolution) or Reversed Convolution - Conv2DTranspose(filters, kernel_size):
#           Results will be close to the original values, but it is not going to be exact because of data loss (from pooling, etc.). e.x.:
#               0   64  128        -1   0   -2
#               48  192 144 -----> 0.5 4.5 -1.5 -----> ...
#               142 226 168        1.5  2   -3  
#
#               32   64  64        -1   0   -2
#               48  192 128 <----- 0.5 4.5 -1.5 <----- ...
#               128 192 168        1.5  2   -3
#             