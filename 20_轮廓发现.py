import cv2 as cv
import numpy as np
'''
轮廓发现：基于图像边缘提取的基础寻找对象轮廓的方法，
所以边缘提取的阈值选择决定会影响最终轮廓发现结果
api:--findContours() --发现轮廓，--drawContours()绘制轮廓
'''
def contours_demo(image):
    dst =cv.GaussianBlur(image,(3,3),0)
    gray=cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary image",binary)

    #cloneImage,contours,heriachy=cv.findContours(binary,cv.RETR_TREE,cv.CHATA_APPROX_SIMPLE)
    cloneImage, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHATA_APPROX_SIMPLE)  #可去除轮廓里噪音
    for i,contour in enumerate(contours):
        cv.drawContours(image,contours,i,(0,0,255),2)
        #cv.drawContours(image,contours,i,(0,0,255),-1)  填充轮廓
        print(i)
    cv.imshow("detect contours",image)

#以下是法二
def edge_demo(image):
    blurred=cv.GaussianBlur(image,(3,3,),0)#高斯模糊--降低噪声
    gray =cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
     #x Gradient
    xgrad=cv.Sobel(gray,cv.CV_16SCl,1,0)
    #y Gradient
    ygrad=cv.Sobel(gray,cv.CV_16SCl,0,1)
    #edge,50,150分别为高低阈值
    #edge_output=cv.Canny(xgrad,ygrad,50,150)

    edge_output=cv.Canny(gray,50,150)
    #edge_output=cv.Canny(gray,30,100)
    cv.imshow("Canny Edge",edge_output)
    return edge_output
def contours_demo2(image):
    binary =edge_demo(image)
    #cloneImage,contours,heriachy=cv.findContours(binary,cv.RETR_TREE,cv.CHATA_APPROX_SIMPLE)
    cloneImage, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHATA_APPROX_SIMPLE)  #可去除轮廓里噪音
    for i,contour in enumerate(contours):
        cv.drawContours(image,contours,i,(0,0,255),2)
        #cv.drawContours(image,contours,i,(0,0,255),-1)  填充轮廓
        print(i)
    cv.imshow("detect contours",image)
print("-----------------")
src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

#contours_demo(src)
contours_demo2(src)

cv.waitKey(0)

cv.destroyAllWindows()