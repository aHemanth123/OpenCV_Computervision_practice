import cv2 as cv
import numpy as np

#dummy imag  ------------
blank =np.zeros( (500,500 ,3) ,dtype = 'uint8')
cv.imshow('Blank',blank)

#paint img  in a certain color 

# blank[:]  = 0,255,0       # green 
# cv.imshow("Green",blank) 

# for a painting a range of portion

blank[200:300 ,300:400]  = 0,255,0       # green 
# cv.imshow("Green portion" ,blank) 

# 2draw a rectangle 

#1 cv.rectangle(blank,(0,0),(250,250) ,(0,255,255), thickness=2 )  # border
#2 cv.rectangle(blank,(0,0),(250,250) ,(0,255,255), thickness=cv.FILLED )  # filling 
#3
# cv.rectangle(blank,(0,0),(250,250) ,(0,255,255), thickness= -1 )   # also -1  or  cv.FILLED 

#4
# cv.rectangle(blank , (0,0 ),(blank.shape[1]//2 , blank.shape[0]//2), (0,255,255), thickness = -1)
#  it is                       also the position mid position w rt image 
# cv.imshow("Rectangle", blank )

# 3Draw a circle  
cv.circle( blank, (blank.shape[1]//2 , blank.shape[0]//2) ,40,(0,0,255), thickness= 3) # radius 40 pixel , thickness = -1 
# cv.imshow("circle", blank  )


#4 draw a line 
cv.line(blank ,(110,200),( 300 ,  400)  ,(255,255,255), thickness= 3)
# cv.imshow("Line",blank)

#5 how to write  text in image
cv.putText(blank,'Hello',  (0,225),cv.FONT_HERSHEY_DUPLEX ,1 ,(255,255,255) ,thickness= 2 )
cv.imshow('Text', blank )

# img = cv.imread('Images/elephant.jpg')
# cv.imshow('ELEPHANT',img)

cv.waitKey(0)