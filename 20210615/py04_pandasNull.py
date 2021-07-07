# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\llaum\\Desktop\\prActice/titanic.csv")
print(df)
print("----")
print(df['Age'].isnull())           # 값이 없는지
print("----")
print(df[df['Age'].isnull()])       # 나이 값이 없는 것들
print("----")
# df = df.fillna(0)                 # 없는 거 다 채우기 
# df['Age'] = df['Age'].fillna(0)     # 나이만 0으로 채우기
# df['Age'] = df['Age'].fillna(df['Age'].mean())    # 나이만 평균 값으로
df['Age'] = df['Age'].fillna(df['Age'].mode()[0])   # 나이를 가장 많이 등장하는 나이로
print(df.iloc[5])

# pandas 단독으로 없음을 표현 불가
# 없애기
df['Survived'] = df['Survived'].replace(0, np.nan)
print(df.iloc[5])