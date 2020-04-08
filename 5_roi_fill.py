import cv2 as cv
import numpy as np
#泛洪填充
def fill_color_demo(image):
    copyImg =image.copy()
    h,w =image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8) #这句必须是这样
    cv.floodFill(copyImg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FlOODFILL_FIXED_RANGE)
    cv.imshow("fill_clor_demo",copyImg)
'''
泛洪填充，如何填充一个对象内部区域，
--FlOODFILL_FIXED_RANGE  -改变对象，泛洪填充
--FLOODFILL_MASK_ONLY     -不改变对象，只填充遮罩层本身，忽略新的颜色值参数
floodFill(Mat image,Mat mask,Point seedPoint,Scalar newVal)
floodFill(image,mask,seedPoint,newVal,rect,loDiff,upDiff,flags)
src(seed x,seed y)-loDiff<=src(img)<=src(seed.x,seed.y)+upDiff
灰度低值         灰度高值
'''
#二值化填充
def fill_binary():
    image=np.zeros([400,400,3],np.uint8)
    image[100:300,100:300, : ]=255
    cv.imshow("fill_binary",image)

    mask=np.ones([402,402,1],np.uint8)
    mask[101:301,101:301] = 0 #这里mask注意，他要是唯一的
    cv.floodFill(image,mask,(200,200),(0,0,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled bimary",image)

src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

'''
#获取ROI区域，region of interest
face = src[50:250,100:300]
gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
src[50:250,100:300] = backface
cv.imshow("face",src)
'''
#fill_color_demo(src)
fill_binary()
cv.waitKey(0)

cv.destroyAllWindows()
