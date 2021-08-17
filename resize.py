import cv2 as cv

img = cv.imread('image/friends.jpg')
#cv.imshow('imagename',img)
cv.waitKey(0)


def functionname(frame, scale =0.5):
    width = int(frame.shape[1]* scale)
    height = int( frame.shape[1]* scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_image = functionname(img)
cv.imshow('iamgename',resized_image)

cap=cv.VideoCapture('video/Array.ts')
while True:
    isTrue, frame = cap.read()
    frame_resized = functionname(frame)
    #cap is variable name here
    #cv.imshow('koibhinaam',frame)
    cv.imshow('newframename',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()