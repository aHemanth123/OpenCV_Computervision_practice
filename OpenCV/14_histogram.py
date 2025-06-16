import cv2 as cv

import matplotlib.pyplot as plt 
import numpy as np 

# Masking in OpenCV is the process of isolating or highlighting specific parts of an image by using a mask—a black-and-white image 

 
img =  cv.imread('Images/elephant.jpg')
cv.imshow('Img',img)  

blank = np.zeros(img.shape[:2],dtype = "uint8")


#  1
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# # cv.imshow('Gray',gray)

# #mask
circle =  cv.circle (blank, (img.shape[1]//2 ,img.shape[0] //2 ),100,255,-1)
# mask = cv.bitwise_and(gray, circle )
# cv.imshow('Mask',mask)


# gray scale  histogram 
# gray_hist = cv.calcHist([gray], [0] , None , [256] ,[0 ,256])
# gray_hist = cv.calcHist([gray], [0] ,  mask  , [256] ,[0 ,256])


# plt.figure('Gray hist')
# plt.xlabel('bins')
# plt.ylabel("No of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#2  masking  rgb  and plotting histogram 
mask  = cv.bitwise_and(img,img, mask = circle)
cv.imshow("mask",mask)

plt.title('Color histogram')
# color histogram 

colors = ('b','g','r')
for i,col in enumerate(colors) :
     hist = cv. calcHist([img],[i] , None ,[256] ,[0,256])
     plt.plot(hist, color = col)
     plt.xlim([0,256])

plt.show()
cv.waitKey(0)
