# **Autoencoders**

What are *autoencoders*?  
&nbsp;&nbsp;&nbsp;&nbsp; - neural networks capable of learning dense representations of input data without supervision (training data not labeled);  
&nbsp;&nbsp;&nbsp;&nbsp; - useful for dimensionality reduction and for visualization;  
&nbsp;&nbsp;&nbsp;&nbsp; - can be used to generate new data that resembels input data;  
&nbsp;&nbsp;&nbsp;&nbsp; - in practice they:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a. copy input to output;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b. learn efficient ways to represent data. 

&nbsp;  

## **Basic Autoencoder Architecture**
In autoencoders, the number of inputs and output neurons should match. For example, if we have x1, x2 and x3, then then we should have 3 neurons, where each produces y1, y2 and y3 respectively. However, the number of neurons in encoder and decoders cannot match! Otherwise, there will be a straith path from inputs to outputs and no pattern to represent data will be learned. This network representation is called *under complete*. Also, when training the network, you feed it the same data as x_train and y_train.  

&nbsp;

**Basic architecture:**   
&nbsp;&nbsp;&nbsp;&nbsp; - *Inputs*: X1, X2, X3;  
&nbsp;&nbsp;&nbsp;&nbsp; - Layer that takes inputs and encodes the latent representation of the input data - 2 neurons (turn 3D input data into 2D encoded data) - *Encoder*;  
&nbsp;&nbsp;&nbsp;&nbsp; - Layer that takes latent representation of input data, decodes it and turns it into an output - 3 neurons (turn 2D encoded data into 3D decoded, approximated representation of input data) - *Decoder*;  
&nbsp;&nbsp;&nbsp;&nbsp; - *Outputs*: Y1, Y2, Y3.

&nbsp;  

# **Deep autoencoders**
## **Stacked Autoencoders**
Stacked autoencoder architecture can be used to achieve encoding and decoding for more complex images. They are usually more accurate than shallow autoencoders. A bottleneck layer - the shallowest layer in the network - is used to get more features but without further reducing the dimension afterwards.  

&nbsp;  

**Stacked Autoencoder Architecture:**  
&nbsp;&nbsp;&nbsp;&nbsp; - *Inputs*: X1, X2, X3, X4, X5;  
&nbsp;&nbsp;&nbsp;&nbsp; - *Encoder:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 4 neurons;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 3 neurons.  
&nbsp;&nbsp;&nbsp;&nbsp; - *Bottleneck* - 2 neurons;  
&nbsp;&nbsp;&nbsp;&nbsp; - *Decoder:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 3 neurons;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 4 neurons.  
&nbsp;&nbsp;&nbsp;&nbsp; - *Output* - reconstructed input.

&nbsp;  

## **Convolutional Autoencoders**
It is known that convolutional neural networks are better for computer vision. Thereby, convolutional autoencoders work better than just DNN autoencoders. Notice we don't flatten the images. This is because CNNs can deal with 2D arrays. 

&nbsp;

**Convlutional Autoencoder Architecture:**  
&nbsp;&nbsp;&nbsp;&nbsp; - *Input*;  
&nbsp;&nbsp;&nbsp;&nbsp; - *Encoder:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D_2(filters=64) + POOLING_1(2x2) (28x28x64);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D_3(filters=128) + POOLING_2(2x2) (14x14x128).  
&nbsp;&nbsp;&nbsp;&nbsp; - *Bottleneck:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D_4(filters=256) (7x7x256);  
&nbsp;&nbsp;&nbsp;&nbsp; - *Decoder:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D_5(filters=128) + UPSAMPLING_1(2x2) (14x14x128);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D_6(filters=64) + UPSAMPLING_2(2x2) (28x28x64);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D_7(filters=1) (28x28x1) (1x1 convolution?).  
&nbsp;&nbsp;&nbsp;&nbsp; - *Output* - reconstructed input.