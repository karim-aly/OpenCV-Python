import cv2
import numpy as np
import matplotlib.pyplot as plt


#### Goals
# - Blur imagess with various low pass filters
# - Apply custom-made filters to images (2D convolution)


############################################
#### 2D Convolution ( Image Filtering ) ###
############################################

# As for one-dimensional signals, images also can be filtered with various low-pass filters (LPF), high-pass filters (HPF), etc. 
# A LPF helps in removing noise, or blurring the image. 
# A HPF filters helps in finding edges in an image.

# OpenCV provides a function, cv2.filter2D(), to convolve a kernel with an image. 
# As an example, we will try an averaging filter on an image. 
# A 5x5 averaging filter kernel can be defined as follows:
# 
#                                        | 1 1 1 1 1 |
#                                        | 1 1 1 1 1 |
#                               k = 1/25 | 1 1 1 1 1 |
#                                        | 1 1 1 1 1 |
#                                        | 1 1 1 1 1 |

# Filtering with the above kernel results in the following being performed: 
# - for each pixel, a 5x5 window is centered on this pixel, 
# - all pixels falling within this window are summed up, and the result is then divided by 25. 
# This equates to computing the average of the pixel values inside that window. 
# This operation is performed for all the pixels in the image to produce the output filtered image. 

# Try this code and check the result:

img = cv2.imread('opencv_logo.png')

kernel = np.ones((5,5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


#####################################
### Image Blurring (Image Smoothing)
####################################
