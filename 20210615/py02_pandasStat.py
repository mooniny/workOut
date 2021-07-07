# -*- coding:utf-8 -*-
import pandas as pd
from _sqlite3 import connect

df = pd.read_csv("C:\\Users\\llaum\\Desktop\\prActice/titanic.csv")
print(df)
print("----")
ageMax = df["Age"].max()
print(ageMax)
print(df["Age"].min())      # 최소값
print(df["Age"].mean())     # 평균
print(df["Age"].sum())      # 합계
print(df["Age"].count())    # 갯 수
print(df["Age"].var())      #
print(df["Age"].std())      # 표준 편차
print(df["Age"].median())   # 
print("----")               # 일반적인 통계 함수들 -끝-
print(df["Age"].mode())     # 최빈값 : 제일 많이 나오는 거
print("----")
print(df["Age"].describe()) # 정리해서 다
print("----")
print(df.mean)
print("----")
print(df.describe())
print("====")

# kwon/kwon@192.168.0.81:1521/xe
# kma_weather_kwon

# DB서버에 적재해놨던 기상청 날씨 데이터
# pd.DataFrame으로
con = connect("kwon/kwon@192.168.0.81:1521/xe")
# sql = "select max(kw_temp), min(kw_temp), avg(kw_temp) from kma_weather_kwon"
sql = "select * from kma_weather_kwon"
df = pd.read_sql(sql, con)
con.close()
print(df)
print("----")
print(df["KW_TEMP"].max())      # 6월 중 제일 높은 기온
print(df["KW_TEMP"].min())      # 6월 중 제일 낮은 기온
print(df["KW_TEMP"].mean())     # 6월 중  평균 기온
print("----")
# 6월 중 제일 높았던 기온에 해당하는 전체 정보
print(df[df["KW_TEMP"] == df["KW_TEMP"].max()])
# 6월 중 평균기온 보다 높았던 기온에 해당하는 전체 정보
print(df[df["KW_TEMP"] >= df["KW_TEMP"].mean()])
# 6월 중 제일 시원했던거는 언제
print(df[df["KW_TEMP"] == df["KW_TEMP"].min()['KW_WHEN']])
print(df.describe())




