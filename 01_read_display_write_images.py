import numpy as np
import cv2 as cv

# Loads a color image. 
# Any transparency of image will be neglected. It is the default flag
# variant flags: (cv.IMREAD_GRAYSCALE, cv.IMREAD_UNCHANGED -> for alpha channel)
img_orig = cv.imread('lena30.jpg', cv.IMREAD_COLOR)

# save image in png format
cv.imwrite('image.png', img_orig)

# load the saved image in grayscale
img = cv.imread('image.png', cv.IMREAD_GRAYSCALE)

# create a window with flag NORMAL to make it resizable
# variant flags: (cv.WINDOW_AUTOSIZE)
cv.namedWindow('Saved as PNG', cv.WINDOW_NORMAL)

# show the image in the window
# can be called directly and a window is created but with the default flag: flag cv.WINDOW_AUTOSIZE
cv.imshow('Saved as PNG', img)

# wait until a key is pressed and returns the pressed key
# we pass 0 to wait indefinitely and we have no interest in the key pressed
cv.waitKey(0)

# closes all opened windows
# If you want to destroy any specific window, 
# use the function cv.destroyWindow(window_name)
cv.destroyAllWindows()

