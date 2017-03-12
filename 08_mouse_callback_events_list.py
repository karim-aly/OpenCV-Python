import cv2 as cv
import numpy as np


# we create a mouse callback function which is executed when a mouse event take place. Mouse event can be anything related to mouse like
# left-button down, left-button up, left-button double-click etc. It gives us the coordinates (x,y) for every mouse event. With this event and
# location, we can do whatever we like. To list all available events available, run the following code in Python terminal:

events = [i for i in dir(cv) if 'EVENT' in i]

for event in events:
	print (event)

def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK: # left click double click
        cv.circle(img, (x,y), 100, (255,0,0), -1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')

# sets the mouse callback to the image we created
cv.setMouseCallback('image', draw_circle)

while(1):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27: # press esc to exit
        break
cv.destroyAllWindows()