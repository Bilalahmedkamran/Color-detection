import numpy as np
import cv2
import numpy as np
def nothing():
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow('abc')
cv2.createTrackbar('lh','abc',0,255,nothing)
cv2.createTrackbar('ls','abc',0,255,nothing)
cv2.createTrackbar('lv','abc',0,255,nothing)
cv2.createTrackbar('uh','abc',255,255,nothing)
cv2.createTrackbar('us','abc',255,255,nothing)
cv2.createTrackbar('uv','abc',255,255,nothing)

while (1):
    #frame = cv2.imread('left.jpg')
    _, frame= cap.read()
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh= cv2.getTrackbarPos('lh','abc')
    ls= cv2.getTrackbarPos('ls','abc')
    lv= cv2.getTrackbarPos('lv','abc')
    uh= cv2.getTrackbarPos('uh','abc')
    us= cv2.getTrackbarPos('us','abc')
    uv= cv2.getTrackbarPos('uv','abc')
    lb = np.array([lh,ls,lv])
    ub = np.array([uh,us,uv])
    mask = cv2.inRange(hsv,lb,ub)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',result)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()    
cv2.destroyAllWindows()
