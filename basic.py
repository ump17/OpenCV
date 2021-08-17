import cv2 as cv

img = cv.imread('image/srk.jpg')
cv.imshow('imagename',img)

#Colot to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayimage',gray)

#more blur than gausian blur
average = cv.blur(img, (7,7,))
cv.imshow('avergaeblurr',average)

#blur image
blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
#3,3- to blur more-kernal value
cv.imshow('blurimage',blur)


#edge cascade
canny = cv.Canny(img ,100,175)
cv.imshow('canny image',canny)

#dialating image- invcraeses thickness/brightness
#useful for final year project
dilated = cv.dilate(canny,(7,7),iterations =3)
cv.imshow('dilated image',dilated)

#eroding
eroded= cv.erode(dilated, (3,3) ,iterations=1)
cv.imshow('eroded image',eroded)

#resize
#INTER_AREA- if shrinking the image ,INTER_CUBIC- if increasing size
resized = cv.resize(img,(500,500), interpolation= cv.INTER_AREA)
cv.imshow('resized image',resized)

#crop
croped = img[50:200,200:400]
cv.imshow('cropped image',croped)


cv.waitKey(0)