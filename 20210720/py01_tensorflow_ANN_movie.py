# -*- coding:utf-8 -*-
import tensorflow as tf
# (1, 3),             (2, 5), (3, 7), (5, ?) : y = 2x + 1
# ([80, 20], [1, 0]), ([95, 5], [1, 0]), ... : y = ax + b

# 다층·다차원회귀 (식을 여러개 만들어서)

# ANN (Artificial Neural Network) : 입력층 1, 출력층 1로 구성된 인공신경망 (이렇게는 정확도가 떨어짐)

# one-hot encoding : 한쪽에만 불이 들어오는 encoding
#    Action - 왼팔    =>    [1, 0]    # [왼팔, 오른팔]
#    Noir - 오른팔    =>    [0, 1]

xData = [[80,20],[95,5],[10,90],[90,10],[5,95]]
yData = [[1, 0], [1, 0], [0, 1], [0, 1], [1, 0]]
label = ['Action', 'Action', 'Noir', 'Noir', 'Action']
##################################################################
x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

# xData = 1x2    ***행렬
# yData = 1x2
# a = 2 x 2 여야
# y      =  x       *  a           +  b
# [1, 0] = [80, 20] * [-1.11 1.22  + [-1.55 1.66]
#                      -1.33 1.44
# (1 x 2) = (1 x 2) * (2 x 2)      + (1 x 2)
a = tf.Variable(tf.random_uniform([len(xData[0]), len(yData[0])], -2, 3, tf.float64))  # 최초의 값을 랜덤을 뽑아서 #len(xData[0]) : 2개
b = tf.Variable(tf.random_uniform([len(yData[0])], -2, 3, tf.float64))
sik = tf.add(tf.matmul(x, a), b)    # 행렬 곱하고 더하고

# 차원수 줄이고_평균(실제 y값과 sik을 통해서 구해진 값과의 거리)
dist = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels = y, logits = sik))

o = tf.train.AdamOptimizer(learning_rate=0.0001)
goal = o.minimize(dist)     # 최적화 객체 거리 줄이기
##################################################################
s = tf.Session()
s.run(tf.global_variables_initializer())

while True:
    s.run(goal, {x:xData, y:yData})
    # print(s.run(a))
    # print(s.run(b))
    # print("--------")
    d = s.run(dist, {x:xData, y:yData})     # 오차 값
    print(d)
    
    if d < 0.7:
        break
##################################################################
xx1 = float(input("fight_scene : "))
xx2 = float(input("bad_language : "))
xxData = [[xx1, xx2]]
# result = s.run(sik, {x:xxData})
# 가장 큰 값이 있는 있는 쪽으로 전기가 흐른셈
# tf.argmax
#        list에서 가장 큰 값이 있는 인덱스 리턴
#        0 : 행방향
#        1 : 열방향
result = s.run(tf.argmax(sik, 1), {x:xxData})
print(result) # 더 큰쪽으로 움직였다.
print(result[0]) # 숫자만 꺼내서
print(label[result[0]]) # 라벨링









