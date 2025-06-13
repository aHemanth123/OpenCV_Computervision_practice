import cv2 as cv

import matplotlib.pyplot as plt 
import numpy as np 

 
img =  cv.imread('Images/roadway.jpg')
cv.imshow('Img',img) 

blank = np.zeros(img.shape[:2],dtype= 'uint8')


b,g ,r = cv.split(img)

blue = cv.merge([b,blank,blank])  # displaying only blue channel  
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow('Red',r)


# cv.imshow("blue",blue)
# cv.imshow("green",green)
# cv.imshow('Red',red)

print(img.shape)

# print(b.shape) # gray images  of shape 1 
# print(g.shape)
# print(r.shape)

merge1 = cv.merge([blue,green,red])
cv.imshow('Merged1',merge1)


merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged )



cv.waitKey(0)