import cv2 as cv
import numpy as np
'''
Canny算法  边缘检测 用于图像处理
Canny算法五部：
1.高斯模糊--GaussianBlur
2.灰度转换--cvtColor
3.计算梯度--Sobel/Scharr
4.非最大信号抑制：根据图像上某一点求出其角度，然后进行判断，如果该角度小于该种颜色取值范围，则设为0，否则就保留
5.高低阈值链接，输出二值图像
高低阈值链接：T1，T2为阈值，凡是高于T2的都保留，凡是小于T1的都丢弃，从高于T2的像素出发，凡是大于T1而且相互连接的都保留，最终得到一个输出二值图像。
推荐的高低阈值比值为T2:T1=3:1/2:1,其中T2为高阈值，T1为低阈值
'''
def edge_demo(image):
    blurred=cv.GaussianBlur(image,(3,3,),0)#高斯模糊--降低噪声
    gray =cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)

    '''
     #x Gradient
    xgrad=cv.Sobel(gray,cv.CV_16SCl,1,0)
    #y Gradient
    ygrad=cv.Sobel(gray,cv.CV_16SCl,0,1)
    #edge,50,150分别为高低阈值
    edge_output=cv.Canny(xgrad,ygrad,50,150)
    以上这部分可用下面这一行代替
    '''
    edge_output=cv.Canny(gray,50,150)
    cv.imshow("Canny Edge",edge_output)

    dst =cv.bitewise_and(image,image,mask=edge_output)
    cv.imshow("Color Edge",dst)

print("-----------------")
src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)



cv.waitKey(0)

cv.destroyAllWindows()