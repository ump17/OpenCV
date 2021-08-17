import cv2 as cv

#img = cv.imread('image/friends.jpg')
#cv.imshow('imagename',img)
#image name and variable
#cv.waitKey(0)
#To wair indefinite period of time

#Below code for video reading

cap=cv.VideoCapture('video/Array.ts')
while True:
    isTrue, frame = cap.read()
    #cap is variable name here
    cv.imshow('koibhinaam',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()