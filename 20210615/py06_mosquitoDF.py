# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
# mean() : 값이 없으면 넘어감

df = pd.read_csv("C:\\Users\\llaum\\Desktop\\prActice/mosquito.csv", names = ['언제', '물가', '집', '공원'])   # 제목
print(df)
# 값이 없지 않은, None이라는 글자가 들어 있는 상태
# print(df[df['물가'].isnull()])
print(df[df['물가'] == 'None'])       # 데이터가 없는게 아니고 None이라고 되어 있음

# 'None' -> 없애고
df['물가'] = df['물가'].replace("None", np.nan)     # None이라는 데이터를 비워냄
df['집'] = df['집'].replace("None", np.nan)
df['공원'] = df['공원'].replace("None", np.nan)
print(df[df['물가'].isnull()])

# 애초에 글자/숫자 섞여있던 상태 -> 둘 다 소화가능한 object타입
print(df['물가'].dtype)       # 데이터 타입 : object객체 -> python 입장에선 둘(자료와 숫자)을 다 담을 방법이 필요했음

# 숫자로 바꿔서
df['물가'] = pd.to_numeric(df['물가'])
df['집'] = pd.to_numeric(df['집'])
df['공원'] = pd.to_numeric(df['공원'])
print(df['물가'].dtype())

# 평균 구하기
print(df['물가'].mean())
print(df['집'].mean())
print(df['공원'].mean())

# 없는 값을 평균 값으로 채우기
df['물가'] = df['물가'].fillna(df['물가'].mean())
df['집'] = df['집'].fillna(df['집'].mean())
df['공원'] = df['공원'].fillna(df['공원'].mean())
print(df.iloc[183])

# 평균값 컬럼 추가
df['평균'] = (df['물가'] + df ['집'] + df['공원']) / 3
print(df)

df = df[df['평균'] > 0]       # 데이터 값 중에 0인것 제외하려고

# 모기가 제일 심했던 날 전체
print(df[df['평균'] == df['평균'].max()])
print("----")
# 모기가 제일 잠잠했던 날 전체
print(df[df['평균'] == df['평균'].min()])
print("----")
# 평균
print(df[df['평균'].mean()])
print("----")
# 평균보다 모기가 심한 날은 언제
print(df[df['평균'] > df['평균'].mean()]['언제'])
print("----")
# 모기가 심한 날 top10 정보
df = df.sort_values(by = '평균')
print(df.head(10))
print("----")


