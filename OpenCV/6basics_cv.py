import cv2 as cv  
img = cv.imread('Images/elephant.jpg ')
cv.imshow('elephant',img)

# convert bgr to grayscale (white -black)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blurred image 
blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT) # odd no 3,3  -> 7,7  increasing the blur 
cv.imshow('BLur',blur)

# Edge cascade 
canny = cv.Canny(img, 125,175)
cv.imshow("Canny Edges ",canny )
# if there are so many edges  then pass blur image 


# dilating  the image  using structure img <- canny 
dilated = cv.dilate(canny , (3,3), iterations= 1)
cv.imshow('Dilated',dilated)

#Eroding
eroded = cv.erode(dilated, (3,3) ,iterations = 1)
cv.imshow("Eroded",eroded)

# resize and croping
resized  = cv.resize(img, (500,500) , interpolation=  cv.INTER_AREA) # smaller  # sclae up imag  -->INTER_LINEAR, INTER_CUbic
cv.imshow("Resize",resized)

#cropping 
croped = img [50:100, 200:400] 
cv.imshow('Cropped',croped)
cv.waitKey(0)  
