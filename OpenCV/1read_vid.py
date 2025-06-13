import cv2 as cv 

# capture = cv.VideoCapture(0) # 0 ,1,2,  0 -> web cams   1,2 -> other cams 
capture = cv.VideoCapture('videos/Waterfall.mp4')

while True:
    isTrue, frame = capture.read()  # bool at left --> is frame read or not 

    cv.imshow('Video' , frame) # indv frame

    if cv.waitKey(20) & 0xFF == ord('d'):  # stop video  , if letter is d  is pressed -> stop 
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)