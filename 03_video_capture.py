import numpy as np
import cv2 as cv

# create VideoCapture object with the built-in webcam (index: 0)
# Its argument can be either the device index or the name of a video file
cap = cv.VideoCapture(0)

# check if cap is initialized, if not initialize it
if cap.isOpened() == False:
	cap.open()

# You can also access some of the features of this video using 
# cap.get(propId) method where propId is a number from 0 to 18
# For example, I can check the frame width and height by: 
# cap.get(3) and cap.get(4). It gives me 640x480 by default

# Some of these values can be modified using cap.set(propId, value)

while(True):
    # Capture frame-by-frame
    # returns a bool (True/False). True If frame is read correctly
    ret, frame = cap.read()

    if ret == True:
        # Our operations on the frame come here -> convert to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv.imshow('frame', gray)

    # wait until q key is stroked to exit the loop and terminate
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()