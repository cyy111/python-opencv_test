import cv2 as cv
import numpy as np
'''
顶帽tophat：原图像与开操作之间的差值图像
黑帽blackhat：闭操作与原图像的差值图像
形态学梯度-Gradient:
基本梯度--是用膨胀后的图像减去腐蚀后的图像得到差值图像，称为梯度图像也是opencv中支持的计算形态学梯度的方法，而此方法得到梯度有被称为基本梯度
内部梯度--是用图像减去腐蚀之后的图像得到差值图像，称为图像的内部梯度
外部梯度--图像膨胀之后再减去原来的图像得到的差值图像，称为图像的外部梯度
'''
def top_hat_demo(image):
    gray =cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel =cv.getStructuringElement(cv.MORPH_RECT,(15,15))
    #dst=cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)#顶帽
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)
    #增加点亮度
    cimage=np.array(gray.shape,np.uint8)
    cimage=120
    dst=cv.add(dst,cimage)
    cv.imshow("top_hat_demo",dst)
def hat_binary_demo(image):
    gray =cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    kernel =cv.getStructuringElement(cv.MORPH_RECT,(15,15))
    #dst=cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)#顶帽
    #dst = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)
    dst = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)
    cv.imshow("hat_binary_demo",dst)
def gradient2_demo(image):
    kernel =cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    dm=cv.dilate(image,kernel)
    em=cv.erode(image,kernel)
    dst1 = cv.subtract(image,em)#internel gradient
    dst2=cv.subtract(dm,image)#external gradient
    cv.imshow("internal",dst1)
    cv.imshow("external",dst2)

print("-----------------")
src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
#top_hat_demo(src)
#hat_binary_demo(src)
gradient2_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()

