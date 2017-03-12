
import numpy as np
import cv2 as cv

'''
learn these functions : cv2.line(), cv2.circle() , cv2.rectangle(), cv2.ellipse(), cv2.putText() etc.

In all the above functions, you will see some common arguments as given below:

img : The image where you want to draw the shapes

color : Color of the shape. for BGR, pass it as a tuple, 
        eg: (255,0,0) for blue. For grayscale, just pass the scalar value.

thickness : Thickness of the line or circle etc. 
            If -1 is passed for closed figures like circles, it will fill the shape. 
            by default, thickness = 1

lineType : Type of line, whether 8-connected, anti-aliased line etc.
            cv2.LINE_AA gives anti-aliased line which looks great for curves.
            By default, it is 8-connected. 
'''

# Create a black image
img = np.zeros((512,512,3), np.uint8)

#########################
# Drawing Ellipse
# To draw the ellipse, we need to pass several arguments. 
# One argument is the center location (x,y). 
# Next argument is axes lengths (major axis length, minor axis length). 
# angle is the angle of rotation of ellipse in anti-clockwise direction. 
# startAngle and endAngle denotes the starting and ending of ellipse arc measured in clockwise direction from major axis. 
# i.e. giving values 0 and 360 gives the full ellipse. 

thickness = 40
radius = 64
axis = (radius, radius)

center_y = 256 + radius // 2

# draw first red open circle
img = cv.ellipse(img, (256,128), axis, 90, 45, 315, (0, 0, 255), thickness, cv.LINE_AA)

# draw second green open circle
img = cv.ellipse(img, (150,center_y), axis, -45, 45, 315, (0, 255, 0), thickness, cv.LINE_AA)

# draw last blue open circle
img = cv.ellipse(img, (512-150,center_y), axis, -90, 45, 315, (255, 0, 0), thickness, cv.LINE_AA)


#########################
# Adding Text to Images:
# To put texts in images, you need specify following things:
#   - Text data that you want to write
#   - Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
#   - Font type (Check cv2.putText() docs for supported fonts)
#   - Font Scale (specifies the size of font)
#   - regular things like color, thickness, lineType etc. For better look, lineType = cv2.LINE_AA is recommended.

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (70,464), font, 3, (255,255,255), 4, cv.LINE_AA)

cv.imshow('OpenCV Logo', img)

cv.waitKey(0)
cv.destroyAllWindows()