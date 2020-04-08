import cv2 as cv
import numpy as np
'''
霍夫圆变换原理：从平面坐标到极坐标转换三个参数C(x,y,r),其中x,y是圆心，
假设平面坐标的任意一个圆上的点，转换到极坐标中：C(x,y,r)处有最大值，霍夫变换正是利用这个原理实现圆的检测。
现实考量：霍夫圆检测对噪声较敏感，所以首先要对图像作中值滤波。
基于效率考虑，opencv中实现的霍夫变换圆检测是基于图像梯度的实现，分为两步：
1.检测边缘，发现可能的圆心
2.基于第一步的基础上，从候选圆心开始计算最佳半径大小
'''
def detect_circles_demo(image):
    dst=cv.pyrMeanShiftFiltering(image,10,100)  #消除噪声
    cimage=cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    #param1,param2：边缘提取低值、高值，minRadius,maxRadius默认值为0，它会自动计算出真实值
    circles=cv.HoughCircles(cimage,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    circles=np.uint16.around(circles)
    for i in circles[0,:]:
        #（，中心点位置 半径，颜色，线宽）
        cv.circle(image,(i[0],i[1],i[2]),(0,0,255),2)
        cv.circle(image,(i[0],i[1]),2,(255,0,0),2)
    cv.imshow("circles",image)

print("-----------------")
src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

detect_circles_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()