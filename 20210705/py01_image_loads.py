# -*- coding:utf-8 -*-
# 그림, 음성, 영상, ... -인코딩 -> 숫자

# pip install opencv-python
import cv2
import matplotlib.pyplot as plt

# grayscale
# data = cv2.imread("C:\\Users\\llaum\\Pictures\\maLove/7-7.jpg", cv2.IMREAD_GRAYSCALE)   # 숫자화
# print(data)
#
# plt.imshow(data, cmap="gray")
# plt.show()

# color
data = cv2.imread("C:\\Users\\llaum\\Pictures\\maLove/7-7.jpg", cv2.IMREAD_COLOR)   # BGR
print(data)
data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)    # BGR -> RGB
plt.imshow(data)
plt.show()







