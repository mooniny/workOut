# -*- coding:utf-8 -*-
import os
import cv2


# 폴더 내의 파일명들을 list로
filenames = os.listdir('C:\\Users\\sdedu\\Desktop\\test\\bunsikMenu')
for fn in filenames:
    print(fn)

# 회귀   : 1        -> 11
# 에어컨 : [30, 50] -> 강([1, 0])
# 손글씨 : i01.png[255,255,255,210,...]  -> 떡볶이([1,0,0,0,0])

# i = cv2.imread('C:\\Users\\sdedu\\Desktop\\test\\bunsikMenu/i01.png', cv2.IMREAD_COLOR) 오래걸림
i = cv2.imread('C:\\Users\\sdedu\\Desktop\\test\\bunsikMenu/i01.png', cv2.IMREAD_GRAYSCALE)


