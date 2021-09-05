# Neural style transfer is an algorithm that takes a pair of images - 
# style image and content image, combines them and creates a stylized image.
# There are 3 approaches to Style Transfer:
#   1. Supervised learning:
#       Pairs: original & stylized (manually created) images
#       It needs lots of pairs!
#       So, you teach a model how to stylize an image
#   2. Neural Style Transfer:
#       Uses pre-trained model
#       Inputs: a single pair of images:
#           Extract style from image 1
#           Extract content from image 2
#       Generate image to match style and content
#           In a loop: minimize loss of generated image with respect
#           to the style of image 1 and content of image 2
#           You use loss minimization to merge the style and the content into
#           the generated image
#   3. Fast Neural Style Transfer:
#       Faster version of Neural Style Transfer

# We start with the image that we want to transform and we call this the content image. 
# Then there's the image that gives us the style that we want to convert our image into - style image. 
# From these, we'll create a new image that we'll call the generated image. 
# It would be created over many iterations initially looking very much like the content image but over time it will take on the attributes of the style image. 
# Using a pre-trained CNN, for example, VGG-19, we can extract the content features from the content image. 
# We'll represent these features as the last block in the network (last COVN2D block I think - features), and the style is also extracted by using a pre-trained CNN. 
# Style information can be extracted from every layer in the network, and this is represented by the arrows coming out of each block in the network diagram. 
# We'll then initialize our generated image from the content image. 
# The model can compare the generated image with the content image by calculating what's called a content loss. 
# On every iteration, it checks how much of the original content is present in the generated image. 
# As you can imagine on the first iteration, the content loss will be close or equal to zero depending on the initialization of the pre-trained CNN. 
# Over several iterations the content loss may increase as the generated image is modified to incorporate the style information. 
# Now, this might seem counterintuitive, but increasing the content loss is actually a good thing 
# because that would indicate that there are differences between the generated image and the original content image. 
# The loss would be zero if they were identical. 
# But of course, you don't want the loss to get too high or you'd lose the features and attributes of the original image. 
# Similarly, you want to reduce the style loss because we'd like some of its attributes to be in the generated image. 
# It's ultimately a BALANCING game. 
# The algorithm also compares the generated image with the style image using a metric called the style loss. 
# The style loss is calculated by comparing each layer of the CNNs for both the generated image and the style image. 
# The style loss ends up being an average loss across the multiple layers that are being compared. 
# In early iterations, as the images are very different, the style loss will be very high, 
# but the goal is to reduce it over time as the generated image incorporates more of the style information. 
# You can imagine that you'd want a generated image to keep the overall loss low. 
# You can combine the style loss with the content loss to get a total loss. 
# Given this information, we can use an optimizer to update the generated image to get a new generated image whose total loss is lower. 
# If you recall how you can use gradients in an optimizer to update each layer of a neural network, you can apply a very similar concept here to updating the input image. 
# Which should make the generated image into something closer to a merged image between the two input images. 
# We'll repeat the process comparing the generated image against the style image to get a style loss and also comparing the generated image against the content image to get a content loss. 
# Adding the two losses into a total loss, and then optimizing to reduce the overall total loss. 
# Now notice that WE ARE NOT TRAINING this network. 
# It's being used to extract the content and style information from the images. 
# But the process is quite similar to network training in that you iteratively calculate and minimize a loss through a loss function and then apply what you've learned using an optimizer to get new data. 
# Note that while I'm showing three networks here, there's really only one network. 
# I'm just splitting into three like this to make it easier to illustrate.

# Steps to Develop Neural Style Transfer:
#   1. Preprocess content & style images
#   2. Load pre-trained model, define loss functions
#   3. Loop:
#       a. Optimize and generate new image
#       b. Visualize outputs

# LOWER LAYER FEATURES DEFINE STYLE OF THE IMAGE, HIGHER LAYER FEATURES (COMPLEX)
# DEFINE CONTENT OF THE IMAGE

# VGG-19 for Style Extraction:
#   VGG-19 has 16 CONV + MAX_POOL blocks.
#   To effectively extract style, use 1st CONV layer in each CONV block
#   (CONV1_1, CONV2_1, CONV3_1, CONV4_1, CONV5_1)
# VGG-19 for Contect Extraction:
#   VGG-19 has 16 CONV + MAX_POOL blocks.
#   To effectively extract content, use only last CONV layer - CONV5_4
#   BUT it last layer isn't always the best one to use, because filters
#   reduces image to very small images containing extracted feautures.
#   Choosing a layer positioned a little before the last layer will work well.
#   For example, choose CONV5_2 or experiment.

# Total Loss
#   Ltotal(p, a, x) = alpha * Lcontent(p, x) + beta * Lstyle(a, x), where
#      Ltotal - total loss,
#      Lcontent - content loss,
#      Lstyle - style loss,
#      alpha - content weight,
#      beta - style weight
#      p - content image (original photograph),
#      x - generated image initialized to input image,
#      a - style image.

# Content Loss
#   generated image - content image = element-wise subtraction
#   then do element-wise square
#   then do reduce sum to get a scalar value
#   then apply weight
#   Lcontent(p, x, l) = 1/2 * SUMij(Fijl - Pijl)^2, where
#       Lcontent - content loss,
#       Fijl - content representation of generated image x in layer l
#           (activation of ith feature map at position j in layer l of generated image)
#       Pijl - content representation of content image p in layer l
#           (activation of ith feature map at position j in layer l of content image)

# Style Loss
#   Concept is the same as in content loss
#   El = 1/(4 * Nl^2 * Ml^2) * SUMij(Gijl - Aijl)^2, where
#       El - loss at layer l,
#       l - layer,
#       Aijl - style representation (Gram Matrix) of style image a,
#       Gijl - style representation (Gram Matrix) of generated image x,
#       1/(4 * Nl^2 * Ml^2) - weight