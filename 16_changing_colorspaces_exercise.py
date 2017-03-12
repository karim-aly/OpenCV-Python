import cv2 as cv
import numpy as np

###### Changing Color-space ######
# There are more than 150 color-space conversion methods available in OpenCV. 
# But we will look into only two which are most widely used ones, BGR to Gray and BGR to HSV.

# For color conversion, we use the function cv.cvtColor(input_image, flag) where flag determines the type of conversion.
# For BGR to Gray conversion we use the flags cv.COLOR_BGR2GRAY. 
# Similarly for BGR to HSV, we use the flag cv.COLOR_BGR2HSV.

# To get other flags, just run following commands in your Python terminal :
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
for flag in flags:
	print(flag)
print("Number of flags:", len(flags))

# Note:
# For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]
# Different softwares use different scales. So if you are comparing OpenCV values with them, you need to normalize these ranges.

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.imshow('image', img)

def changeImageColor(x):
    # get current positions of four trackbars
    h = cv.getTrackbarPos('H','image')
    s = cv.getTrackbarPos('S','image')
    v = cv.getTrackbarPos('V','image')

    global img

    img[:] = [h,s,v]
    img = cv.cvtColor(img, cv.COLOR_HSV2BGR)

    cv.imshow('image', img)



# create trackbars for color change
cv.createTrackbar('H', 'image', 0, 179, changeImageColor)
cv.createTrackbar('S', 'image', 0, 255, changeImageColor)
cv.createTrackbar('V', 'image', 0, 255, changeImageColor)

while(1):
    k = cv.waitKey(1) & 0xFF
    if k == 27: # esc button
        break

cv.destroyAllWindows()


###### Object Tracking ######

# Now we know how to convert BGR image to HSV, we can use this to extract a colored object. 
# In HSV, it is more easier to represent a color than RGB color-space. In our application, 
# we will try to extract a blue colored object. So here is the method:

# 	- Take each frame of the video
# 	- Convert from BGR to HSV color-space
# 	- We threshold the HSV image for a range of blue color
#	- Now extract the blue object alone, we can do whatever on that image we want.

cap = cv.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask_b = cv.inRange(hsv, lower_blue, upper_blue)

    # define range of red color in HSV
    #lower_red = np.array([170,50,50])
    #upper_red = np.array([10,255,255])
    #mask_r = cv.inRange(hsv, lower_red, upper_red)

    # define range of yellow color in HSV
    lower_yellow = np.array([20,50,50])
    upper_yellow = np.array([40,255,255])
    mask_y = cv.inRange(hsv, lower_yellow, upper_yellow)

    mask = cv.bitwise_or(mask_b, mask_y)
    #mask = cv.bitwise_or(mask, mask_y)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask= mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()

# Note

# This is the simplest method in object tracking. Once you learn functions of contours, 
# you can do plenty of things like find centroid of this object and use it to track the object, 
# draw diagrams just by moving your hand in front of camera and many other funny stuffs


####### How to find HSV values to track? #######

# It is very simple and you can use the same function, cv2.cvtColor(). Instead of passing an image, 
# you just pass the BGR values you want. For example, to find the HSV value of Green

red = np.uint8([[[0,0,255]]])
hsv_red = cv.cvtColor(red, cv.COLOR_BGR2HSV)
print(hsv_red)


# Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively. 

# Apart from this method, you can use any image editing tools like GIMP or any online converters to find these values, 
# but don’t forget to adjust the HSV ranges.