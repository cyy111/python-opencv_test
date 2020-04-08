import cv2 as cv
import numpy as np
'''
图像形态学是图像处理学科的一个单独分支学科，
灰度与二值图像处理中的重要手段
是由数学的集合论等相关理论发展起来的。
膨胀（Dilate）:3X3的结构元素  ---或--注意：腐蚀与膨胀都支持，任意形状的结构元素。
膨胀作用：对象大小增肌一个像素（3X3），平滑对象边缘，减少或者填充对象之间的距离
腐蚀：--与-,作用：对象大小减少1个像素（3X3）平滑对象边缘  弱化或者分割图像之间的半岛型连接
'''
#腐蚀
def erode_demo(image):
    print(image.shape)
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    #ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY| cv.THRESH_OTSU)
    kernel =cv.getStructuringElement(cv.MORPH_RECT,(3,3))#结构元素加大，腐蚀加重
    dst=cv.erode(binary,kernel)
    cv.imshow("erode_demo",dst)
    #膨胀
def dilate_demo(image):
    print(image.shape)
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    kernel =cv.getStructuringElement(cv.MORPH_RECT,(3,3))#结构元素加大，腐蚀加重
    dst=cv.dilate(binary,kernel)
    cv.imshow("dilate_demo",dst)

print("-----------------")
src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
erode_demo(src)
dilate_demo(src)


cv.waitKey(0)

cv.destroyAllWindows()
'''
src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
kernel =cv.getStructuringElement(cv.MORPH_RECT,(5,5))#结构元素加大，腐蚀加重
#dst=cv.dilate(src,kernel)
dst=cv.erode(src,kernel)
cv.imshow("dresult",dst)

cv.waitKey(0)

cv.destroyAllWindows()
'''