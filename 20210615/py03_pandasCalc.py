# -*- coding:utf-8 -*-
import pandas as pd

df = pd.DataFrame()
df["이름"] = ['홍길동', '김기동', '최길동']
df['국어'] = ['100', '80', '90']

# 문자열 -> 숫자
df['국어'] = pd.to_numeric(df['국어'])

# 숫자 -> 문자열
# df['국어'] = df['국어'].astype(str)

df['영어'] = [90, 10, 20]
df['수학'] = [10, 54, 12]

# 학생이름으로 데이터 찾기
# df = df.set_index(df['이름'])
# print(df)

print(df["영어"].count())# 영어 점수의 갯수
print(df["영어"].std())# 영어점수 표준편차

# 중앙값과 2사분위 수는 서로 같은 값을 의미한다.
# 영어 점수의 중앙값과 4사분위수를 구하고 결과화면을 캡쳐하시오.
print(df["영어"].median())    # 중앙값
print(df["영어"].describe())  # 4사분위수 (75%)

# 학생별 평균 계산해서, 평균 컬럼 추가
# print(df["영어"].mean())
df['평균'] = (df['국어'] + df['영어'] + df['수학'] / 3)
print(df)

# 첫번째 학생 평균 점수 (이름빼고)
# print(df.iloc[0].mean())

