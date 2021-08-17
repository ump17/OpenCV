import cv2 as cv
#import numpy as np
#delab>>haarcascade

img = cv.imread('image/srk.jpg')
cv.imshow('imagename',img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayimage',gray)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=1)
#minneighbor kam = more efficiency
print(f' Number of faces found = {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y),(x+w,y+h),(0,222,0),thickness=2)

cv.imshow('detected_face',img)

cv.waitKey(0)
