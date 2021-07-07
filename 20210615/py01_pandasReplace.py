# -*- coding:utf-8 -*-
import pandas as pd

# PANDAS
#     데이터를 바꾸는 X
#     데이터를 추출해서 가공 O

df = pd.read_csv("C:\\Users\\llaum\\Desktop\\prActice/titanic.csv")
print(df)
print("----")
# Pclass 1인거 1등석으로  바꿔서 그것만 추출
df2 = df["Pclass"].replace(1, "1등석")
print(df)
print("----")

# Pclass 1인거를 1등석으로 바꿔서 df의 Pclass에 세팅
df["Pclass"] = df["Pclass"].replace(1, "1등석")
print(df)
print("----")


# 2 -> 2등석, 3 -> 3등석 한꺼번에
df["Pclass"] = df["Pclass"].replace([2,3], ["2등석", "3등석"])
print(df)
print("----")

# 1등석 -> 1st, 2등석 -> 2nd 한꺼번에 2
df["Pclass"] = df["Pclass"].replace({"1등석":"1st", "2등석":"2nd"})
print(df)
print("----")

# 1st, 2nd, 3등석 한꺼번에 '자리'로
df["Pclass"] = df["Pclass"].replace(["1st", "2nd", "3등석"], "자리")
print(df)
print("----")

# 전체에서 1 -> 일
df = df.replace(1, "일")
print(df)
print("----")
# 데이터 바꾸기 끝

# 열 제목
df = df.rename(columns = {"Survived":"생존여부", "Fare":"요금"})
print(df)
print("=====")

# 지하철 csv
subwayDF = pd.read_csv("C:\\Users\\sdedu\\Desktop\\test/seoulSubway.csv", names = ["년", "월", "일", "노선", "타", "내리"])

# 9호선, 2호선 -> 학원올때 타는 노선
subwayDF["노선"] = subwayDF["노선"].replace(["9호선", "2호선"], "학원올때")
# print(subwayDF[subwayDF["노선"] == '학원 올 때'])

# 집 근처역 -> 집
subwayDF["역"] = subwayDF["역"].relplace("상월곡", "집")
# print(subwayDF[subwayDF["역"] == "집"])







# df2 = df.set_index(df["Name"])
# print(df)