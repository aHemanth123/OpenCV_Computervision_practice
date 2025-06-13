import cv2 as cv 
import numpy as np 

img = cv.imread('Images/roadway.jpg')
cv.imshow('ELp',img)

blank = np.zeros(img.shape ,dtype= 'uint8')
cv.imshow('Blank',blank)

gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey',gray)

#1 method  --- 
# #blur   # remove blur function 
# blur = cv.GaussianBlur(gray,(5,5) ,cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)

# #edge detector 
# canny =  cv.Canny( blur,125,175)
# cv.imshow('Canny Edges' ,canny )

#2 method  -----
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # threshold values 
cv.imshow('THRESH',thresh)

#----------- CONTOURS 

#contours 
contours, hierarchies =  cv.findContours( thresh ,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)  #  RETR_list ,RETR_tree ,external -> Explore  
# cv.CHAIN_APPROX_NONE ---> contours approximation  ,  cv.CHAIN_APPROX_SIMPLE  --> compressed approximation
print(f'{len(contours)} contours  found !')


# 
cv.drawContours(blank , contours , -1 ,(0,0,255),thickness= 1) # -1 -> all contours
cv.imshow('DRAw CONTOURs' , blank)

cv.waitKey(0)