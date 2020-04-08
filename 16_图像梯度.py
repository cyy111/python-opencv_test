import cv2 as cv
import numpy as np
'''图像梯度：一阶导数与Sobel算子，二阶导数与拉普拉斯算子'''
def lapalian_demo(image):
    #dst =cv.Laplacian(image,cv.CV_32F)
    #lpls =cv.convertScaleAbs(dst)
    #cv.imshow("lapalian_demo",lpls)


    #kernel =np.array([0,1,0],[1,-4,1],[0,1,0])
    kernel = np.array([1, 1, 1], [1, -8, 1], [1, 1, 1])
    dst =cv.filter2D(image,cv.CV_32F,kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian_demo",lpls)

def sobel_demo(image):
    grad_x = cv.Sobel(image,cv.CV_32F,1,0)  # grad_x = cv.Scharr(image,cv.CV_32F,1,0)增强边缘,对噪声较敏感
    grad_y =cv.Sobel(image,cv.CV_32F,0,1)
    gradx=cv.convertScaleAbs(grad_x)
    grady=cv.convertScaleAbs(grad_y)
    cv.imshow("gradient-x",gradx)
    cv.imshow("gradient-y",grady)

    gradxy =cv.addWeighted(gradx,0.5,grady,0.5,0)
    cv.imshow("gradient",gradxy)


print("-----------------")
src=cv.imread("sea.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)



cv.waitKey(0)

cv.destroyAllWindows()