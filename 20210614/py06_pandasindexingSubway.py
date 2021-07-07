# -*- coding:utf-8 -*-
import pandas as pd

# subway.csv 데이터 프레임으로
subwayDF = pd.read_csv("C:/Users/sdedu/Desktop/test/seoulSubway.csv", names=['년', '월', '일', '노선', '역', '타', '내리'])
print(subwayDF)
print("-----")
print(subwayDF.columns)             # 열 제목들
print("-----")
print(subwayDF.head(3))             # 앞 3개만
print("-----")
print(subwayDF.tail()["역"])        # 뒤 5개 역 명만
print("-----")
print(subwayDF.iloc[0])             # 첫 데이터 전체
print("-----")
print(subwayDF.iloc[1][["노선", "역"]])         #두번째 데이터 노선, 역명
print("-----")
print(subwayDF.iloc[2:6][["노선", "역"]])       # 2 ~ 5까지 노선, 역명
