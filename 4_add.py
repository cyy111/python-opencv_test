import cv2 as cv
import numpy as np

def add_demo(m1,m2):
    dst = cv.add(m1,m2)
    cv.imshow("add_demo",dst)
def subtract_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow("subtract_demo",dst)
def divide_demo(m1,m2):
    dst = cv.divide(m1,m2)
    cv.imshow("divide_demo",dst)
def multiply_demo(m1,m2):
    dst = cv.multiply(m1,m2)
    cv.imshow("multiply_demo",dst)
    #均方差
def others(m1,m2):
    M1,dev1=cv.meanStdDev(m1)
    M2,dev2=cv.meanStdDev(m2)
    h,w=m1.shape[:2]
    print(M1)
    print(M2)
    print(dev1)
    print(dev2)

    img=np.zeros([h,w],np.uint8)
    m,dev = cv.meanStdDev(img)
    print(m)
    print(dev)
#逻辑运算
def logic_demo(m1,m2):
    dst=cv.bitewise_and(m1,m2)
    dst2=cv.bitewise_or(m1,m2)
    dst3=cv.bitewise_not('sea.jpg')
    cv.imshow("logic_window3",dst3)
    cv.imshow("logic_window1",dst)
    cv.imshow("logic_window2",dst2)
#提取亮度和对比度
def contract_bright_demo(image,c,b):
    h,w,ch=image.shape
    blank = np.zeros([h,w,ch],image,dtype)
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("contract_bright_demo",dst)

src1=cv.imread("1.jpg")
src2=cv.imread("2.jpg")
print(src1.shape)
print(src2.shape)
cv.namedWindow("image1",cv.WINDOW_AUTOSIZE)
#cv.imshow("image1",src1)
#cv.imshow("image2",src2)

src=cv.imread("sea.jpg")
cv.imshow("src",src)
contract_bright_demo(src,1.2,10)

add_demo(src1,src2)
subtract_demo(src1,src2)

add_demo("image1",src1)
cv.waitKey(0)

cv.destroyAllWindows()