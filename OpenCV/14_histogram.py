import cv2 as cv

import matplotlib.pyplot as plt 
import numpy as np 
# An image histogram is a graphical representation of the distribution of pixel intensities (brightness values) in an image.

# Grayscale Histogram: Shows how many pixels have each intensity (0–255).
# Color Histogram: Shows the same for blue, green, and red channel


# Why Use Histograms?
# ✅ To analyze brightness and contrast.
# ✅ For image segmentation and thresholding.
# ✅ To equalize image contrast using histogram equalization.
# ✅ For feature extraction in image processing and computer vision.

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

# To limit histogram computation to the masked region

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
