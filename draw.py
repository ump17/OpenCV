import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3), dtype='uint8')
cv.imshow('blankimage',blank)
#RGB
#blank[:]= 0,255,0
#cv.imshow('green_koibhinaam',blank)
#img = cv.imread('image/friends.jpg')
#cv.imshow('imagename',img)
#image name and variable

#cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=-1)
#cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
#cv.imshow('rectangle',blank)

#cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
#cv.imshow('circle',blank)

#cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
#cv.imshow('Line',blank)

cv.putText( blank,'Hello,smart ladke',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),3)
cv.imshow('Text',blank)
cv.waitKey(0)