import cv2 as cv
import numpy as np
'''模糊操作基本原理：
1.基于离散卷积
2.定义好每个卷积核
3.不同卷积核得到不同的卷积效果
4.模糊是卷积的一种表象'''

#均值模糊--去噪声
def blur_demo(image):
    dst = cv.blur(image,(5,5))
    cv.imshow("blur_demo",dst)

#中值模糊---去斑点噪声
def median_blur_demo(image):
    dst = cv.medianBlur(image,5)
    cv.imshow("median_blur_demo",dst)

#自定义模糊
def custom_blur_demo(image):
   # kernel=np.ones([5,5],np.float32)/25
    kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32) #锐化：奇数 总和需要是0或1，0---边缘梯度，1---增强
    dst =cv.filter2D(image,-1,kennel=kernel)
    cv.imshow("custom_blur_demo",dst)


src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
#blur_demo(src)
#median_blur_demo(src)
custom_blur_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()