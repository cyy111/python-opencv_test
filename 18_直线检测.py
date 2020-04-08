import cv2 as cv
import numpy as np
'''霍夫直线变换  ----用来做直线检测，前提条件---边缘检测已完成
平面空间到极坐标空间转换
'''
def line_detection(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges=cv.Canny(gray,50,150,apertureSizes=3)
    #HoughLines(image,半径步长--最长极坐标，角度，边缘阈值低值)--->cita r
    lines=cv.HoughLines(edges,1,np.pi/180,200)
    for line in lines:
        rho,theta= line[0]
        a=np.cos(theta)
        b=np.sin(theta)
        x0=a+rho
        y0=b+rho
        x1=int(x0+1000*(-b))
        y1=int(y0+1000*(a))
        x2=int(x0-1000*(-b))
        y2=int(y0-1000*(a))
        #绘出一条直线                   颜色 ，线宽
        cv.lines(image,(x1,y1),(x2,y2),(0,0,255),2)
    cv.imshow("image-lines",image)
    #可自己设定检测的线段长度
def line_detect_possible_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges=cv.Canny(gray,50,100,apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100,minLineLength=50,maxLineGap=10)
    for line in lines:
        print(type(line))
        x1,y1,x2,y2=line[0]
        cv.line(image,(x1,y1),(x2,y2),(0,0,255),2)
    cv.imshow("line_detect_possible_demo",image)

print("-----------------")
src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

#line_detection(src)
line_detect_possible_demo(src)#一些小的线段也可以检测出
cv.waitKey(0)

cv.destroyAllWindows()