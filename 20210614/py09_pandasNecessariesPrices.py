# -*- coding:utf-8 -*-
import pandas as pd

# 그 csv로 pd.DataFrame
df = pd.read_csv("C:\\Users\\llaum\\Desktop\\prActice/lnps.csv", names=["어디", "품명", "가격", "언제", "종류"])

# for문으로 차례대로 접근
print(df.index)     # index range: 접근할 수있게 range를 줌
for i in df.index:
    print(i)

# M_Name으로 찾을 수 있게
df = df.set_index(df["어디"]) 
print(df.index)

# 통인시장꺼 다
print(df.loc["통인시장"])

# 함수 : 기능정리
# 메소드 : 객체의 액션
print(df[df['품명'].isnull()])
# df['품명'] = df['품명'].fillna('없음')    # 이게 정상적인...
print(df['품명'].mode())
df['품명'] = df['품명'].fillna(df['품명'].mode()[0])

# 오징어 살 수 있는 곳
# print(df[df["품명"]=="오징어"]["어디"])
print(df[df["품명"],str.contains("오징어")]["어디"])  # X(메소드가 없어서) -> O (메소드를 '없음'으로 채움)

# 제일 비싼 top5
df = df.sort_values(by='가격', ascending=False)
print(df.head())

# 결측치?, 이상치?

# 사과 시리즈 품명, 가격, 언제
print(df[df["품명"] == "사과"][['품명', '가격', '언제']])
print(df[df["품명"].str.contains("사과")][["품명", "가격", "언제"]])  # X
print(df[df["품명"].str.contains("사과")][["품명", "가격", "언제"]])

# 가격 5000원 이상
print(df[df["가격"] >= 5000])

# 인덱스를 날짜
df = df.set_index(df["언제"])

# 2021-01 조회
print(df.loc["2021-01"])





