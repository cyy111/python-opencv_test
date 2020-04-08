import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract as tess
'''数字验证码识别：
opencv+Tesserct-OCR，opencv预处理，Tesserct-OCR验证码识别
预处理：去除干扰线与点，不同的结构元素中选择，Image与numpy array相互转化，识别与输出
'''
def recognize_text():
    gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    #形态学-去干扰
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(2,1))
    bin1=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel=kernel)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,kernel)
    open_out=cv.morphologyEx(bin1,cv.MORPH_OPEN,kernel)
    cv.imshow("binary-image",open_out)

    cv.bitwise_not(open_out,open_out)
    textImage=Image.fromarray(open_out)
    text=tess.image_to_string(textImage)
    print('识别结果：%s'%text)

#png图片
def recognize_text2():
    gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    #形态学-去干扰
    ret,open_out=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    cv.imshow("binary-image",open_out)

    cv.bitwise_not(open_out,open_out)
    textImage=Image.fromarray(open_out)
    text=tess.image_to_string(textImage)
    print('识别结果：%s'%text)

print("-----------------")
src=cv.imread("./opencv_exercises-master/images/yzm.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
recognize_text()


cv.waitKey(0)

cv.destroyAllWindows()