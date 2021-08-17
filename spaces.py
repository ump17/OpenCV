import cv2 as cv

img = cv.imread('image/srk.jpg')
cv.imshow('image',img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsvimage',hsv)

cv.waitKey(0)