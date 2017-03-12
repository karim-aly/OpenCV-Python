import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# load a color image
img = cv.imread('messi5.jpg')

####### Single Pixel Accessing #######

# You can access a pixel value by its row and column coordinates. 
# For BGR image, it returns an array of Blue, Green, Red values. 
# For grayscale image, just corresponding intensity is returned.

px = img[100,100]
print("pixel at (100, 100):", px)

# accessing only blue pixel
blue = img[100,100,0]
print("blue channel value at (100, 100):", blue)

# You can modify the pixel values the same way.
img[100,100] = [255,255,255]
print("pixel at (100, 100):", img[100,100])

# Warning
# Numpy is a optimized library for fast array calculations. 
# So simply accessing each and every pixel values and modifying it will be very slow and it is discouraged.



####### Better pixel accessing and editing method: #######

# accessing RED value
red = img.item(10,10,2)
print("red channel value at (10, 10):", red)

# modifying RED value
img.itemset((10,10,2),100)
red = img.item(10,10,2)
print("red channel value at (10, 10):", red)




####### Accessing Image Properties #######

# 1) Shape of image is accessed by img.shape :
#    It returns a tuple of number of rows, columns and channels (channels if image is colored)
print("image shape:", img.shape)

# 2) Total number of pixels is accessed by img.size :
print("image size (number of pixels * channels):", img.size)

# 3) Image datatype is obtained by img.dtype :
#    img.dtype is very important while debugging because a large number of errors in OpenCV-Python code is caused by invalid datatype.
print("image data type:", img.dtype)




####### ROI (Region of Interest) #######

# ROI is obtained using Numpy indexing. 
# Here I am selecting the ball and copying it to another region in the image:

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv.imshow("ball moved", img)
cv.waitKey(0)
cv.destroyAllWindows()




####### Splitting and Merging Image Channels #######

# split channels
b,g,r = cv.split(img)

# merge channels
img = cv.merge((b,g,r))

# Note
# cv2.split() is a costly operation (in terms of time), 
# so only use it if necessary. Numpy indexing is much more efficient and should be used if possible.

# Numpy Indexing
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]


# Suppose, you want to make all the red pixels to zero, 
# you need not split like this and put it equal to zero. 
# You can simply use Numpy indexing which is faster.
img[:,:,2] = 0



####### Making Borders for Images (Padding) #######
"""
If you want to create a border around the image, something like a photo frame, 
you can use cv2.copyMakeBorder() function. 
But it has more applications for convolution operation, zero padding etc. This function takes following arguments:

- src : input image
- top, bottom, left, right : border width in number of pixels in corresponding directions
- borderType : Flag defining what kind of border to be added. It can be following types:
    - cv2.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
    - cv2.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
    - cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
    - cv2.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
    - cv2.BORDER_WRAP - Can’t explain, it will look like this : cdefgh|abcdefgh|abcdefg
- value - Color of border if border type is cv2.BORDER_CONSTANT """

# Below is a sample code demonstrating all these border types for better understanding: 

BLUE = [255,0,0]

img1 = cv.imread('opencv_logo.png')

constant= cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=BLUE)
reflect = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
replicate = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REPLICATE)
wrap = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_WRAP)


plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(236),plt.imshow(wrap,'gray'),plt.title('WRAP')


plt.show()