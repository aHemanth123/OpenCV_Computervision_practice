import os 
import cv2 as cv
import numpy  as np 


people = [ 'Allu_Arjun','nani']


# p = []

# for  i in  os.listdir(r' '):
#     p.append(i)


# print(p)
# to get same  p  == people list 

DIR = r'C:\Users\Hemanth2512005\Desktop\OpenCV\Images\Image_face_detectin'


harcascade =cv.CascadeClassifier("17_haarcascade_frontalface.xml")

features = []  
labels = []     # whose image it is  0 -> AA  1 ->Prabhas 

def create_train():

    for person in  people : 

        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path= os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect =harcascade.detectMultiScale(gray,scaleFactor= 1.1 ,minNeighbors= 2)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi) 
                labels.append(label)


create_train()
print(f'length of the features = {len(features)}')
print(f'length of the  labels = {len( labels )}')
print('training done ----------')

features =  np.array(features ,dtype= 'object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()


# train  the recognizer  on the features list  and the  labels list 
face_recognizer.train(features,labels)


face_recognizer.save('face_trained.yml') # storing it in yaml file  for training again 

np.save('features.npy',features)
np.save('labels.npy',labels)