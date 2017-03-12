import numpy as np
import cv2 as cv

# create VideoCapture object with the built-in webcam (index: 0)
cap = cv.VideoCapture(0)

# Define the codec FourCC code
# FourCC is a 4-byte code used to specify the video codec. 
# The list of available codes can be found in fourcc.org. It is platform dependent.

# FourCC code for MJPG for example is passed as:
# cv2.VideoWriter_fourcc('M','J','P','G') or cv2.VideoWriter_fourcc(*'MJPG')
fourcc = cv.VideoWriter_fourcc(*'XVID')

# create VideoWriter object
# arguments (out_file_name, fourcc, fps, frame_size, isColor=True)
# 'isColor' flag: If it is True (default), encoder expect color frame, otherwise it works with grayscale frame.
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # flip the frame vertically (0 -> vertically, 1-> horizontally)
        frame = cv.flip(frame, 0)

        # write the flipped frame
        out.write(frame)

        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()