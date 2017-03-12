import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


######## Simple Thresholding ########

# The function used is cv.threshold. 
# First argument is the source image, which should be a grayscale image. 
# Second argument is the threshold value which is used to classify the pixel values. 
# Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value. 
# OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function. Different types are:
# 	- cv.THRESH_BINARY
# 	- cv.THRESH_BINARY_INV
# 	- cv.THRESH_TRUNC
# 	- cv.THRESH_TOZERO
# 	- cv.THRESH_TOZERO_INV

img = cv.imread('gradient.png', 0)
ret,thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()



######## Adaptive Thresholding ########

# In the previous section, we used a global value as threshold value. 
# But it may not be good in all the conditions where image has different lighting conditions in different areas. 
# In that case, we go for adaptive thresholding. In this, the algorithm calculate the threshold for a small regions of the image. 
# So we get different thresholds for different regions of the same image and it gives us better results for images with varying illumination.

# It has three ‘special’ input params and only one output argument.

# 	- Adaptive Method - It decides how thresholding value is calculated.
#		cv.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
# 		cv.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
# 	- Block Size - It decides the size of neighbourhood area.
# 	- C - It is just a constant which is subtracted from the mean or weighted mean calculated.

# Below piece of code compares global thresholding and adaptive thresholding for an image with varying illumination:


img = cv.imread('dave.jpg', 0)
img = cv.medianBlur(img, 5)

ret,th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()