# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 크기 변경
# data = cv2.imread("C:\\Users\\llaum\\Pictures\\maLove/7-7.jpg", cv2.IMREAD_GRAYSCALE)
# data = cv2.resize(data, dsize = (500, 250))     # 절대값 조정 (원본 비율 파괴)
# data = cv2.resize(data, dsize = (0, 0), fx = 0.3, fy = 0.3)      # 비율 (x축 30퍼만큼 축소, y축 30퍼만큼 축소)
# data = cv2.resize(data, dsize = (0, 0), fx = 0.3, fy = 0.3, interpolation = cv2.INTER_LINEAR)    # 보간
# plt.imshow(data, cmap="gray")
# plt.show()

# 자르기
# data = cv2.imread("C:\\Users\\llaum\\Pictures\\maLove/7-7.jpg", cv2.IMREAD_GRAYSCALE)
# data = data[100:200, 100:500]     # list에서 픽셀 선택하기
# plt.imshow(data, cmap="gray")
# plt.show()

# 블러
# data = cv2.imread("C:\\Users\\llaum\\Pictures\\maLove/7-7.jpg", cv2.IMREAD_GRAYSCALE)
# data = cv2.blur(data, (20,50))      # 주위 20*50의 픽셀의 평균값으로 흐리게 하기
# plt.imshow(data, cmap="gray")
# plt.show()

# 쨍하게 (직접 만들기)
# data = cv2.imread("C:\\Users\\llaum\\Pictures\\maLove/7-7.jpg", cv2.IMREAD_GRAYSCALE)
# k = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])     # 커널(중앙점)     5:쨍하고 주번은 약해지게
# data = cv2.filter2D(data, -1, k)      # -1 : 원본하고 같은 포멧으로(.jpg)
# plt.imshow(data, cmap="gray")
# plt.show()

# 대비 늘리기(밝은거 더 밝게 어두운 거 더 어둡게)
# data = cv2.imread("C:\\Users\\llaum\\Pictures\\maLove/7-7.jpg", cv2.IMREAD_GRAYSCALE)
# data = cv2.equalizeHist(data)
# plt.imshow(data, cmap="gray")
# plt.show()

# 경계선 처리하기
# data = cv2.imread("C:\\Users\\llaum\\Pictures\\maLove/7-7.jpg", cv2.IMREAD_GRAYSCALE)
# data = cv2.Canny(data, 50,100)  # 50보다 작으면 무시, 100보다 크면 무조건 경계선으로, 그 사이는 알아서
# plt.imshow(data, cmap="gray")
# plt.show()

# 이진화 (값보다 크면 흰색, 작으면 검정색우로)
data = cv2.imread("C:\\Users\\llaum\\Pictures\\maLove/7-7.jpg", cv2.IMREAD_GRAYSCALE)
_, data = cv2.threshold(data,    # 앞에꺼는 상관없고 뒤에꺼는 결과
                        100,     # 기준값
                        255,     # 바꿀값
                        cv2.THRESH_BINARY)      # 100보다 크면 255로, 아니면 0
                        #cv2.THRESH_BINARY_INV)  # 반대로
plt.imshow(data, cmap="gray")
plt.show()










































