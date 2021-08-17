import cv2 as cv

img = cv.imread('image/srk.jpg')
cv.imshow('imagename',img)

#Colot to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayimage',gray)

#simple thresholding
#threshold kam, darkness kam,150-thresh value here
threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('simple threhhold image', thresh)

threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('simple threhholdinverse', thresh_inv)

#adaptive thresholding
adaptive_thresh= cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive thresholding', adaptive_thresh)

cv.waitKey(0)