import cv2 as cv
import numpy as np
def clamp(pv):
    if pv > 255:
        return 255
    if pv <0:
        return 0
    else:
        return pv

def gaussian_noise(image):
    h,w,c=image.shape     #获取图像的高度、宽度和通道
    for row in range(h):
        for col in range(w):
            '''
            #np.random.randn(size)所谓标准正态分布（μ=0,σ=1），对应于np.random.normal(loc=0, scale=1, size)。loc：float
    此概率分布的均值（对应着整个分布的中心centre）
scale：float
    此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
size：int or tuple of ints
    输出的shape，默认为None，只输出一个值
            '''
            s = np.random.normal(0,20,3)
            b=image[row,col,0] #blue
            g =image[row,col,1]  #green
            r = image[row,col,2]  #red
            image[row,col,0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("noise image",image)


src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
#blur_demo(src)
#median_blur_demo(src)
gaussian_noise(src)
dst=cv.GaussianBlur(src,(5,5),0)
cv.imshow("Gaussian Blur",dst)
cv.waitKey(0)

cv.destroyAllWindows()