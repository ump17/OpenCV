import cv2 as cv
import numpy as np

img = cv.imread('image/srk.jpg')
cv.imshow('imagename',img)

#Colot to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayimage',gray)

#laplacian
lap= cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('laplacian',lap)

cv.waitKey(0)