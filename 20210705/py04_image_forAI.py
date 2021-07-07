# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt

# 인공신경망에 넣으려면 -> 1차원으로(숫자)

data = cv2.imread("C:\\Users\\llaum\\Pictures\\maLove/7-7.jpg", cv2.IMREAD_COLOR)
data = data.flatten()
print(data)

