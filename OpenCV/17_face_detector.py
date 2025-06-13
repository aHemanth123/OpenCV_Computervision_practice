
import cv2 as cv

import matplotlib.pyplot as plt 
import numpy as np 

 
# img =  cv.imread('Images/lady_img.jpg')
img =  cv.imread('Images/group_p.jpg')

cv.imshow('lady',img) 

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
 
#pre trained models 
harcascade =cv.CascadeClassifier("17_haarcascade_frontalface.xml")

faces_rect =harcascade.detectMultiScale(gray,scaleFactor= 1.1 ,minNeighbors= 1)  # incr/ dec when u got wrong  faces 

print(f'number of  faces found = {len(faces_rect)}')


for (x,y, w,h) in  faces_rect :
    cv.rectangle(img, (x,y) ,(x+w,y+h) ,(0,255,0) ,thickness= 2)

cv.imshow('Detected faces',img)

cv.waitKey(0)
