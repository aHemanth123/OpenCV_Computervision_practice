
import cv2 as cv

import matplotlib.pyplot as plt 
import numpy as np 

 
img =  cv.imread('Images/roadway.jpg')
# cv.imshow('Img',img) 

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#edge detection
#laplacian - edge

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian',lap )

# sobel --> gradients  ---> in direction  in x and y 
sobelx = cv.Sobel(gray,cv.CV_32F,1,0)
sobely = cv.Sobel(gray,cv.CV_32F,1,0)
combined_sobel =  cv.bitwise_or(sobelx,sobely)

cv.imshow('sobex',sobelx)
cv.imshow('sobely',sobely)
cv.imshow('comb     sobel',combined_sobel)

#canny  edges -> adv algorithm 
canny = cv.Canny(gray ,150 ,175)
cv.imshow('Canny',canny)

cv.waitKey(0)