import cv2 as cv
import numpy as np
'''
def face_detect_demo():
    gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    face_detectors=cv.CascadeClassifier("D:/CHEN/biancheng/touying_img/opencv-master (1)/opencv-master/data/haarcascades/haarcascade_frontalface_alt_tree.xml")
    faces=face_detectors.detectMultiScale(gray,1.02,5)
    for x,y,w,h in faces:
        cv.rectangle(src,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow("result",src)

print("-----------------")
src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.namedWindow("result",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
face_detect_demo()

cv.waitKey(0)

cv.destroyAllWindows()
'''


#视频检测人脸
def face_detect_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detectors = cv.CascadeClassifier("D:/CHEN/biancheng/touying_img/opencv-master (1)/opencv-master/data/haarcascades/haarcascade_frontalface_alt_tree.xml")
    #faces = face_detectors.detectMultiScale(gray, 1.02, 5)
    faces = face_detectors.detectMultiScale(gray, 1.1, 2)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv.imshow("result", image)
   
#src=cv.imread("sea.jpg")
capture=cv.VideoCapture(0)
#cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.namedWindow("result",cv.WINDOW_AUTOSIZE)
while(True):
    ret,frame=capture.read()
    frame=cv.flip(frame,1)
    face_detect_demo(frame)
    c=cv.waitKey(10)
    if c==27:
        break
#cv.imshow("input image",src)
#face_detect_demo()

cv.waitKey(0)

cv.destroyAllWindows()
