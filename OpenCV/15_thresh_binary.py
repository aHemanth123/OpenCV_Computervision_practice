
import cv2 as cv

import matplotlib.pyplot as plt 
import numpy as np 

 
img =  cv.imread('Images/roadway.jpg')
# cv.imshow('Img',img) 

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


# simple thresholding 
threshold, thresh = cv.threshold(gray,  100 , 255, cv.THRESH_BINARY ) # if  >150 - 255 or  0 thats why 
cv.imshow('SImple Threshold',thresh) 

#inv thresholding
threshold, thresh_inv = cv.threshold(gray,  100 , 255, cv.THRESH_BINARY_INV) # if  >150 - 255 or  0 thats why 
cv.imshow('  Threshold  INV ',thresh_inv) 

#adaptive thresholding 
# adapt_thresh = cv.adaptiveThreshold(gray ,255 ,cv.ADAPTIVE_THRESH_MEAN_C ,cv.THRESH_BINARY , 11 , 3)
# finds mean  by surrounding s on threshold 
#  cv.imshow()

adapt_thresh = cv.adaptiveThreshold(gray ,255 ,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY , 11 , 3)
cv.imshow('Adap thr',adapt_thresh)

cv.waitKey(0)