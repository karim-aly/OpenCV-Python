import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

####### Image Addition #######

# You can add two images by OpenCV function, cv2.add() 
# or simply by numpy operation, res = img1 + img2. 
# Both images should be of same depth and type, or second image can just be a scalar value.

# OpenCV addition is a saturated operation while Numpy addition is a modulo operation.

x = np.uint8([250])
y = np.uint8([10])

print(cv.add(x,y)) # 250+10 = 260 => 255

print(x+y)         # 250+10 = 260 % 256 = 4



####### Image Blending #######

# This is also image addition, but different weights are given to images so that it gives a feeling of blending or transparency. 
# Images are added as per the equation below:
#     g(x) = (1 - alpha) * f0(x) + alpha * f1(x)

# cv2.addWeighted() applies following equation on the image.
#     dst = alpha * img1 + beta * img2 + gamma

img1 = cv.imread('ml.png')
img2 = cv.imread('opencv_logo.jpg')

alpha = 0.7
beta = 0.3
gamma = 0
dst = cv.addWeighted(img1, alpha, img2, beta, gamma)

cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()



####### Bitwise Operations #######

# This includes bitwise AND, OR, NOT and XOR operations. 
# They will be highly useful while extracting any part of the image (as we will see in coming chapters), 
# defining and working with non-rectangular ROI etc. 

# Below we will see an example on how to change a particular region of an image.

# I want to put OpenCV logo above an image. 
# If I add two images, it will change color. 
# If I blend it, I get an transparent effect. 
# But I want it to be opaque. If it was a rectangular region, I could use ROI as we did in last chapter. 
# But OpenCV logo is a not a rectangular shape. So you can do it with bitwise operations as below:

# Load two images
img1 = cv.imread('messi5.jpg')
img2 = cv.imread('opencv_logo.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
start_col = img1.shape[1] - cols 
roi = img1[0:rows, start_col:None]

# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

cv.imshow('img2gray', img2gray)

ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

cv.imshow('mask', mask)
cv.imshow('mask_inv', mask_inv)

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

cv.imshow('img1_bg', img1_bg)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

cv.imshow('img2_fg', img2_fg)

# Put logo in ROI
dst = cv.add(img1_bg, img2_fg)

cv.imshow('dst',dst)

# modify the main image
img1[0:rows, start_col:None] = dst

cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()