# -*- coding:utf-8 -*-

# AI
#     머신러닝 : 그 문제를 해결하는데 필요한 알고리즘은 사람이 지정
#                영화 장르 예측 - kNN
#                스팸 메일 필터링 - naiveBayes


#      딥러닝 :  그 문제를 해결하는데 필요한 알고리즘을 직접 찾아내게
#                인공신경망 구성 -> 데이터 학습 -> 예측
#                딥러닝 라이브러리 : tensorflow

# 빅데이터 분석 취업 -> python, numpy, pandas 주력으로 쓰는 회사 가려고
# python, numpy, pandas

# 최신 tensorflow 2.x : 안되는 컴퓨터가 많은(cpu)
# CUDA : nvidia 그래픽카드까지 활용

# pip install tensorflow==1.5
###################

import tensorflow as tf     # 인공신경망 구성 -> 데이터 학습 -> 예측을 편하게 하려고 라이브러리를 쉽게 쓰기 위해     # 그 대표적인 프로그램

# 1) 인공 신경망 구성 - 실제 값은 들어가지 않음
a  = tf.constant(232)   # 상수(못바꿈)
print(a)
b = tf.constant(12)
c = tf.add(a, b)        # a와 b 더하기
d = tf.constant('zzz')

# 2) 데이터 학습 - 실제 값을 넣고, 학습시키고, ... (생김새를 보는 정도)
s = tf.Session()      # 실행 세션
# aResult = s.run(a)  # 돌려보고
# print(aResult)
cResult = s.run(c)    # 연관된거 다 실행 (c가 a,b를 사용; c만하면 c와 엮여있는게 다 되는)
print(cResult)
dResult = s.run(d)
print(dResult.decode())

# 3) 예측



