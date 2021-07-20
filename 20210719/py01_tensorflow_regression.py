# -*- coding:utf-8 -*-

# 회귀분석 > 인공신경망
#
#
#
#

# regression (회귀) : 학습데이터를 최대한 만족시킬만한 (오차적은) 회귀방정식을 찾아서
#                     (최적의 a, b를 찾아서)
#                     완성된 그 식으로 예측을 진행...

# 인공신경망 : 회귀를 구간별로 심각하게 다루면
import tensorflow as tf

# (1, 11), (2, 21), (3, 31), (5, ?) : y = ax + b 

xData = [1, 2, 3]
yData = [11, 21, 31]

# 1) 인공신경망 구성
#    변수
#        tf.Variable(초기값표현) : AI가 찾아내야 할 값 (a, b)
a = tf.Variable(tf.random_uniform([1], -2, 3, tf.float64))     # [차원수];a의 첫 값 지정 : 랜덤 (1차원, -2에서 3사이, 64bit실수형)
b = tf.Variable(tf.random_uniform([1], -2, 3, tf.float64))

#        tf.placeholder() : 데이터가 들어갈 자리 (x, y)
x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

sik = a * x + b

# sik = -1.123x + 2.213 이런식
# (x = 1, y = 11, sik = 3.336 -> 오차가 크다)

# 기존 y값, sik을 통해 찾은 값의 오차가 적으면 a, b를 잘 찾은거

# 기존 y값, sik을 통해 찾은 값의 거리, 1차원으로 줄이고, 평균
dist = tf.reduce_mean(tf.square(y - sik))  # dist값을 줄여나가기 피타고라스 쓰려고 루트씌움

# 최적의 a,b를 찾아줄 객체
# learning_rate가 크면 a, b값을 크게 바꿔서 재시도 (1.123 -> 5.123 -> 9.123 -> 13.123 -> 9.5 -> 12.12)
#     빨리 찾음 , 답을 지나쳐 버릴수도 -> 최적의 값을 못 찾을수도
# learning_rate가 작으면 a, b값을 작게 바꿔서 재시도 (1.123 -> 1.223 -> 1.323)
#     느리게 찾음, 정확하게 찾기 가능

o = tf.train.AdamOptimizer(learning_rate=0.01)     # learning_rate 값을 수정해서 값을 찾아준다. (인공신경망은 데이터와 learning_rate만 수정해서 쓴다 대체적으로)

goal = o.minimize(dist)

#############################################################

# 2) 데이터를 넣어서 학습
s = tf.Session()     # 실행 섹션
s.run(tf.global_variables_initializer())    # tf.Variable()(a, b)들 초기화

# while True:     # 나올때까지 반복
for _ in range(15000):
    s.run(goal, {x:xData, y:yData})     # placeholder를 {}로
    # print("y = %fx + %f" % (s.run(a),s.run(b)))    # 잘돌아가는지 확인하기위해 식형태로
    
    d = s.run(dist, {x:xData, y:yData})     # 줄어들고 있으면 정상적으로 돌아가고 있다는 것
    print(d)
    print("----------")
    
    # if d < 0.001:  # == 0은 욕심 ; 거의 불가능
        # break

#############################################################

# 3) 예측

xx = float(input("x : "))
result = s.run(sik, {x:xx})[0]
print(result)


