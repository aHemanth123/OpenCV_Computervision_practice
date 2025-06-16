import cv2 as cv

import matplotlib.pyplot as plt 
import numpy as np 

 
img =  cv.imread('Images/roadway.jpg')
cv.imshow('Img',img) 

# Kernel size -> no of rows and no of col  
# blur is applied to middle   as a result of surrounding pixels 

#averaging at middle  by surrounding pixels --> pixel intensity 
# Applies a normalized box filter (i.e., takes the average of all pixels in the kernel).
# Blurs the image uniformly.

average = cv.blur(img, (3,3))
cv.imshow('avgblur',average)

# gauassian blur --> each surrounding pixel is given particular pixel value 
# u will get less blur 
# Applies a weighted average where centre pixels have higher influence.
# Preserves edges better than plain average blur.

gauss = cv.GaussianBlur(img, (3,3) ,0)
cv.imshow("guass blur",gauss)

# median blur  <--> same as avg  but median
median = cv.medianBlur(img, 3) #integer - if 3  kernel size 3,3 only
cv.imshow('Median blur',median)

#bilateral blur  --> applies bluring but retains the edges  in img 

bilateral = cv.bilateralFilter(img, 10, 35 , 25 )  # explore the arg
cv.imshow('BILateral',bilateral)
#sigma space -> is nothing but how far distance it  will affect the img

cv.waitKey(0)
