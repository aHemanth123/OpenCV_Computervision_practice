import cv2 as cv 
import numpy as np 

img = cv.imread('Images/elephant.jpg')
cv.imshow('ELEphant',img)

# transformation
def translate(img, x, y) :   # x ,y-> how much shift along axis 

    transMat =np.float32([[1,0,x],[0,1,y]])   # translation Matrix 
    dimensions = (img.shape[1],img.shape[0])  # width , height 
    return cv.warpAffine(img, transMat, dimensions)


# -x -->  left
# -y -->  Up
# x --> Right
# y -->   DOWN

translated =translate(img, 50, 50)  # right x ,down y
# cv.imshow('TRANSLATED',  translated)

# rotation
def rotate(img ,angle ,  rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint  is None:
        rotPoint = (width//2, height//2)   # rotate around center 

    rotMat = cv.getRotationMatrix2D(rotPoint,angle , 1.0)
    dimensions = (width , height)

    return cv.warpAffine(img, rotMat,dimensions)

roatated = rotate(img, -45)
rotated1 = rotate(roatated, -45)
# cv.imshow('Rotated Img',roatated)
# cv.imshow("ROtated1 ",rotated1)


# resizing 
resized = cv.resize(img, (500,500),interpolation= cv.INTER_AREA) # for shrinking 
resized1 = cv.resize(img, (100,100),interpolation= cv.INTER_LINEAR)  # larger -> linear , cubic 
# cv.imshow("RESIZeD",resized)
# cv.imshow("Res1",resized1)

# flipping 
flip1 = cv.flip(img, 1) #0 -> flipping vertically  # 1 -> horizantally # -1 -> both horizontal and vertical
cv.imshow('Flipping',flip1)  

# cropping 
crop = img[200:300 , 400:500]
cv.imshow('Crop', crop )

cv.waitKey(0) 