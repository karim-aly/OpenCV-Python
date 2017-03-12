import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Loads a color image. 
# Any transparency of image will be neglected. It is the default flag
# variant flags: (cv.IMREAD_GRAYSCALE, cv.IMREAD_UNCHANGED -> for alpha channel)
img_bgr = cv.imread('lena30.jpg', cv.IMREAD_COLOR) # image loaded in BGR order

# split 3 color channels
b, g, r = cv.split(img_bgr)

# merge in the right order for RGB image
img_rgb = cv.merge([r, g, b])

# two more ways to convert image from BGR to RGB
# first:
# img_rgb = img[..., ::-1] or img[:, :, ::-1]
#
# second:
# cv.cvtColor(img, cv.COLOR_BGR2RGB)

# show using matplotlib
plt.subplot(121); plt.imshow(img_bgr) # expects distorted color
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.subplot(122); plt.imshow(img_rgb) # expect true color
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

# show using opencv
cv.imshow('bgr image', img_bgr) # expects true color
cv.imshow('rgb image', img_rgb) # expects distorted color

# wait until a key is pressed and returns the pressed key
# we pass 0 to wait indefinitely and we have no interest in the key pressed
cv.waitKey(0)

# closes all opened windows
# If you want to destroy any specific window, 
# use the function cv.destroyWindow(window_name)
cv.destroyAllWindows()
