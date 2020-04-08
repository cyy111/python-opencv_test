import cv2 as cv
import numpy as np


#边缘保留滤波EPF---类似美颜磨皮效果
#高斯双边
def b1_demo(image):
    dst = cv.bilaterFilter(image,0,100,15)
    cv.imshow("bi demo",dst)

#均值迁移方式
def shift_demo(image):
    dst =cv.pyrMeanShiftFiltering(image,10,50)
    cv.imshow("shift demo",dst)

src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
#b1_demo(src)
shift_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()