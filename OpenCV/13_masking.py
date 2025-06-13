# masking --> focusing on certain parts of an image 

import cv2 as cv

import matplotlib.pyplot as plt 
import numpy as np 

 
img =  cv.imread('Images/roadway.jpg')
cv.imshow('Img',img)  


blank = np.zeros(img.shape[:2],dtype= 'uint8')   
# cv.imshow('blank img',blank)

#with circle  -- 1
# mask = cv.circle(blank , (img.shape[1]//2 ,img.shape[0]//2 +45), 100 , 255 , thickness= -1)

# with rectangle  -- 2
mask = cv. rectangle(blank , (img.shape[1]//2 ,img.shape[0]//2 ),(img.shape[1]//2 -90 ,img.shape[0]//2 +90) , 255 , thickness= -1)
# cv.imshow('Masking',mask )


# custom shape 
circ = cv.circle(blank.copy(),  (img.shape[1]//2 ,img.shape[0]//2 ) , 100 ,255 , -1 )
rect = cv.rectangle( blank.copy(),(30,30), (300,300), 255 , -1)
weird   = cv.bitwise_and(circ,rect)


# #masked            --img = mask ---
# masked = cv.bitwise_and(img, img, mask = mask)
# cv.imshow('Masked image ',masked)

#masking weird         shape  = wierd   -----
masked = cv.bitwise_and(img, img, mask =  weird)
cv.imshow('Weird Masked image  ',masked)

cv.waitKey(0)