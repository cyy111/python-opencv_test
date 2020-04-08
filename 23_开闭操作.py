import cv2 as cv
import numpy as np
'''
开操作open：图像形态学的重要操作之一，基于膨胀与腐蚀操作组合形成的。主要是利用在二值图像分析中，灰度图像亦可。
开操作=腐蚀+膨胀，输入图像+结构元素---消除图像中的小干扰区域
闭操作closed:闭操作=膨胀+腐蚀，输入图像+结构元素--填充闭合区域
开闭操作作用：水平或者垂直直线提取
'''
def open_demo(image):
    print(image.shape)
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary image",binary)
    #kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
   # kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 15)) #去除横线
   # kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  #去除干扰线
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5)) #去除形状不规则点
    binary=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
    cv.imshow("open-result",binary)
def close_demo(image):
    print(image.shape)
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary image",binary)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    binary=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
    cv.imshow("close-result",binary)

print("-----------------")
src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
open_demo(src)
close_demo(src)


cv.waitKey(0)

cv.destroyAllWindows()
