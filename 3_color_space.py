import cv2 as cv
import numpy as np

def extract_object_demo():
    capture = cv.VideoCapture("video.mp4")
    while True:
        ret,frame= capture.read()
        if ret == False:
            break
        #提取某颜色
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv=np.array([37,43,46])
        upper_hsv=np.array([77,255,255])
        #inRange()制作掩模
        mask=cv.inRange(hsv,lower_hsv=lower_hsv,upper_hsv=upper_hsv)
        #bitewise_and提取感兴趣区域
        dst= cv.bitewise_and(frame,frame,mask=mask)

        cv.imshow("mask",mask)
        cv.imshow("video",frame)
        c = cv.waitKey(40)
        if c==27:
            break

#转换颜色空间
def color_space_demo(image):
    #将颜色空间从BGR2转换到GRAY
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    # 将颜色空间从BGR2转换到HSV
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    # 将颜色空间从BGR2转换到YUV
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    # 将颜色空间从BGR2转换到YCrCb
    YCrCb=cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow("YCrCb",YCrCb)

src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

#颜色通道分离与合并
b,g,r=cv.split(src)
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)


src= cv.merge([b,g,r])
src[:,:,2]=0
cv.imshow("changed image",src)
color_space_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
