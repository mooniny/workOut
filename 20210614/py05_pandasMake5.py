# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_csv("C:\\Users\\sdedu\\Desktop\\test/titanic.csv")
print(df)
print("-----")
print(df.head)
print("-----")
print(df.tail(3))
print("-----")
print(df.shape)
print("-----")
print(df.Name)
print("=====")


print("열 기준====")
print(df["Name"])
print("-----")
print(df.Name)
print("-----")
print(df[["Name", "Fare"]])     # 이름과 요금만

print("행 기준====")
print(df.iloc[1])               # 2번째 데이터
print("-----")
print(df.iloc[1:3])             # 1 ~ (3-1)까지
print("-----")
df = df.set_index(df["Name"])   # index 지정 : 사람이름 정렬
print(df)
print(df.loc["Braund, Mr. Owen Harris"]) # 이름으로 검색
print(df.loc["Braund, Mr. Owen Harris":"Allen, Mr. William Henry"]) # 범위 접근 가능
print("=====")
print()

print("행+열 기준====")
print(df.loc["Braund, Mr. Owen Harris"]["Age"])         # 위치
print("-----")
print(df.loc["Braund, Mr. Owen Harris","Fare"])         # , 가능
print()

print("조건=====")
print(df[df["Age"] >= 30])                             # 나이가 30살 이상
print(df[ (df["Age"] >= 30) & (df["Age"] <= 50)])      # 나이가 30 ~ 50세







