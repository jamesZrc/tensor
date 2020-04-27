import cv2
import numpy as ny
import matplotlib.pyplot as plt

image = cv2.imread('D:/download/fds.png')

top_size = 10
bottom_size = 10
left_size = 10
right_size = 10


def cv2_imshow(name, img):
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    top_size, bottom_size, left_size, right_size = (100, 100, 100, 100)


replicate = cv2.copyMakeBorder(image, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)  # bordertype是边界类型#复制法
reflect = cv2.copyMakeBorder(image, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT)  # 反射法
reflect101 = cv2.copyMakeBorder(image, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT101)
warp = cv2.copyMakeBorder(image, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_WRAP)  # 外包装法
constant = cv2.copyMakeBorder(image, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_CONSTANT,
                              value=(0, 255, 0))  # 常量法

cv2_imshow('replicate', replicate)
cv2_imshow('reflect', reflect)
cv2_imshow('warp', warp)
cv2_imshow('reflect101', reflect101)
cv2_imshow('constant', constant)
