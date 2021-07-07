# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt

data = cv2.imread("C:\\Users\\llaum\\Pictures\\maLove/7-7.jpg", cv2.IMREAD_COLOR)
avgColor = cv2.mean(data)
# print(avgColor)
b = avgColor[0]
g = avgColor[1]
r = avgColor[2]

r = int(r)  # 16진수로 바꾸기위해 소수점떼기
g = int(g)
b = int(b)

r = "%02X" % r
g = "%02X" % g
b = "%02X" % b

c = "#" + r + g + b
# print(color)
plt.bar(10, 10, color = c)
plt.show()