import cv2 as cv
import numpy as np
'''
弧长与面积：轮廓发现，
           计算每个轮廓的弧长与面积，像素单位
多边形拟合：获取轮廓的多边形拟合结果
approxPolyDP,
-contour
-epsilon越小越折线越逼近真实形状
-close-是否为闭合区域
几何矩计算（原点矩、中心距、-》图像的重心坐标）-----如何使用几何矩计算对象中心
'''
#检测对象中心，并画出内接矩形
def measure_object(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
   # ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print("threshold value:%s"%ret)
    cv.imshow("binary image",binary)
    dst =cv.cvtColor(binary,cv.COLOR_GRAY2BGR)
    #求出每一个轮廓
    outImage,contours,hireachy =cv.findContours(binary,cv.RETA_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        area =cv.contourArea(contour)
        x,y,w,h=cv.boundingRect(contour)    #计算内接矩形
        rate=min(w,h)/max(w,h)  #求出宽高比
        print("rectangle rate:%s"%rate)
        mm=cv.moments(contour)
        print(type(mm))
        #计算图像的重心坐标
        cx=mm['m10']/mm['m00']
        cy=mm['m01']/mm['m00']
        cv.circle(dst,(np.int(cx),np.int(cy)),3,(0,255,255),-1) #画圆
       # cv.rectangle(dst,(x,y),(x+w,y+h),(0,0,255),2)  #画出矩形
        print("contour area:%s"%area)
        approxCurve =cv.approxPolyDP(contour,4,True)#4---上下间距
        print(approxCurve.shape)
        if approxCurve.shape[0]>6:
            cv.drawContours(dst,contours,i,(0,0,255),2)#红色画圆轮廓线
        if approxCurve.shape[0]==4:
            cv.drawContours(dst,contours,i,(0,255,0),2)#绿色画四边形
        if approxCurve.shape[0]==3:
            cv.drawContours(dst,contours,i,(255,0,0),2)#蓝色画三角形轮廓线
    cv.imshow("measure-contours",dst)

print("-----------------")
src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
measure_object(src)


cv.waitKey(0)

cv.destroyAllWindows()
