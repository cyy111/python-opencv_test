import cv2 as cv
import numpy as np

#图像属性
def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width=image.shape[1]
    channels = image.shape[2]
    print("width: %s ,height: %s ,channels: %s "%(width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c]= 255 - pv
    cv.imshow("pixel_demo",image)

#比access_pixels运行快
def inverse(image):
    dst =cv.bitwise_not(image)
    cv.imshow("inverse demo",dst)
'''
 np.ones(size) 可以创建任意维度的数组，各个元素值均为1
np.zeros(size,dtype) 同上，但各个元素值为0.默认元素类型为浮点数
'''

def create_image():
    #创建长宽为256的图片，三通道GRB，像素大小为8位无符号整数
    '''img = np.zeros([400,400,3],np.uint8)
    #创建蓝色通道，设置图片的额颜色B通道为255
    img[:,:,0] = np.ones([400,400])*255
    #创建红色通道
    img[:, :, 2] = np.ones([400, 400]) * 255
    '''
   # img=np.zeros([400,400,1],np.uint8)
    #img[:,:,0] = np.ones([400,400])*127

   # img = np.zeros([400, 400, 1], np.uint8)
    #img=img*0
    #cv.imshow("new image", img)

    #m1=np.ones([3,3],np.uint8)
    # m1.fill(12222)
    # print(m1)
#数组二维、三维转换
    # m2=m1.reshape([1,9])
    # print(m2)

    m3 =np.array([[2,3,4],[1,6,5],[7,8,9]],np.int32)
    m3.fill(9)
    print(m3)

src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
t1=cv.getTickCount()
#access_pixels(src)
#inverse(src)
create_image()
t2=cv.getTickCount()
print("time:%s ns"%((t2-t1)/cv.getTickFrequency())*1000)
cv.waitKey(0)

cv.destroyAllWindows()


