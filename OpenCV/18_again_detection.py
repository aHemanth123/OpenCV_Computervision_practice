import numpy as np
import cv2 as cv


# using the model used 18_faces_train.py 

harcascade =cv.CascadeClassifier("17_haarcascade_frontalface.xml")


people = [ 'Allu_Arjun','nani']

# features = np.load('features.npy' ,allow_pickle=)
# labels = np.load('labels.npy')


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
 
img = cv.imread(r'C:\Users\Hemanth2512005\Desktop\OpenCV\Images\Image_face_detectin\AA_test_1.jpg')  # try with AA_test
gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)
 


# detect the face  in the image
faces_rect =harcascade.detectMultiScale(gray,scaleFactor= 1.1 ,minNeighbors= 2)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    
    label,confidence =  face_recognizer.predict(faces_roi)
    print(f'label = {label} with a confidence of {confidence}')


    cv.putText(img,str(people[label]) ,(20,20),cv.FONT_HERSHEY_COMPLEX, 1.0 , (0,225,0) , thickness= 2)

    cv.rectangle(img, (x,y) ,(x+w,y+h) ,(0,255,0) , thickness= 2  )

cv.imshow('Detected Face ',img)
cv.waitKey(0)