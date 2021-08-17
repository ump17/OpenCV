import cv2 as cv
import numpy as np

img = cv.imread('image/srk.jpg')
#cv.imshow('image',img)

blank = np.zeros(img.shape[ : 2], dtype= 'uint8')
#cv.imshow('blankimage',blank)

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),150,250,-1)
#150=radius,color,thickness
#cv.imshow('maskimage',mask)

masked = cv.bitwise_and(img,img,mask= mask)
cv.imshow('maskedimage',masked)


cv.waitKey(0)