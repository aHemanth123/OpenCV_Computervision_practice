
import cv2 as cv 
import matplotlib.pyplot as plt 

img =  cv.imread('Images/roadway.jpg')
cv.imshow('Img',img) 

#matplotlib shows as rgb image  ---- not bgr 
# plt.imshow(img)
# plt.show()

#bgr to rgb 
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow('rgb',rgb)

#BGR  to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

#bgr to hsv 
hsv = cv.cvtColor( img,cv.COLOR_BGR2HSV)
# cv.imshow("HSV",hsv)

#bgr to l a b
lab  = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

#-----Note: -------- you can not  covert  gray to hsv  directly ------------> gray - bgr - hsv   <-------------------

#hsv to bgr 
hsv_bgr  = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
# cv.imshow('hsv --> bgr',hsv_bgr)

#lab to bgr 
lab_bgr= cv.cvtColor(lab,cv.COLOR_Lab2BGR)
cv.imshow('Lab--> bgr',lab_bgr)
cv.waitKey(0)