import cv2 as cv
import ipython

# In image processing, since you are dealing with large number of operations per second, 
# it is mandatory that your code is not only providing the correct solution, 
# but also in the fastest manner. So in this chapter, you will learn:
# 	- To measure the performance of your code.
# 	- Some tips to improve the performance of your code.
# 	- You will see these functions : cv.getTickCount, cv.getTickFrequency etc.


######## Measuring Performance with OpenCV ########

# cv.getTickCount function returns the number of clock-cycles after a reference event 
# (like the moment machine was switched ON) to the moment this function is called. 
# So if you call it before and after the function execution, you get number of clock-cycles used to execute a function.

# cv.getTickFrequency function returns the frequency of clock-cycles, or the number of clock-cycles per second. 
# So to find the time of execution in seconds, you can do following:

img = cv.imread('messi5.jpg')

e1 = cv.getTickCount()
for i in range(5,49,2):
    img = cv.medianBlur(img, i)
e2 = cv.getTickCount()
t = (e2 - e1) / cv.getTickFrequency()

print("Time taken: %f seconds" % t)

# Note
# You can do the same with time module. Instead of cv2.getTickCount, use time.time() function. Then take the difference of two times.



######### Default Optimization in OpenCV #########

# Rest of this Code Note is in this notebook:
#	-> Measuring Performance in IPython.ipynb