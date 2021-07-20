# -*- coding:utf-8 -*-
import tensorflow as tf
# 인공신경망 종류
#     ANN (Artificial Neural Network) : 입력층 1, 출력층 1로 구성된 인공신경망 - 정확도가 떨어짐
#                                       층을 늘려서 정확도를 올리고 싶었으나, H/W가 받챠주질 않음
#     DNN (Deep NN) : 입력층 1, 은닉층 n, 출력층 1로 구성 - 정확도가 상승
#     CNN (Convolution NN) : DNN인데 이미지 분석할 때 (여러개의 픽셀 중에 몇개의 픽셀씩 묶어서 처리)
#                            속도는 상승, 정확도가 떨어짐
#     RNN (Recurrent NN) : DNN결과를 다음 DNN에 활용
xData = [[80,20],[95,5],[10,90],[90,10],[5,95]]
yData = [[1, 0], [1, 0], [0, 1], [0, 1], [1, 0]]
label = ['Action', 'Action', 'Noir', 'Noir', 'Action']
##################################################################
x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

# [80 20] * [1 2 3 4 5 6 7 ...    = [123 354 985 18 9 5 3 ...] 
#            1 231 462 135 ...]
a1 = tf.Variable(tf.random_uniform([len(xData[0]), 100], -2, 3, tf.float64))
b1 = tf.Variable(tf.random_uniform([100], -2, 3, tf.float64))
sik1 = tf.add(tf.matmul(x, a1), b1)
sik1 = tf.nn.relu(sik1)     # 음수 값은 0으로 바꾸기

# 활성화 함수 : 값이 너무 작은 것은 0으로 바꿔서 다음층 계산할때 제외되게
# 전기가 흐르는 걸 묘사하는 중
# 값이 너무 작음 => 그 쪽으로는 전기가 흐르지 않았다고 보는게 효율적! 


# [123 354 985 18 9 5 3 ...]
a2 = tf.Variable(tf.random_uniform([100, 500], -2, 3, tf.float64))
b2 = tf.Variable(tf.random_uniform([500], -2, 3, tf.float64))
sik2 = tf.add(tf.matmul(sik1, a2), b2)
sik2 = tf.nn.relu(sik2)

a3 = tf.Variable(tf.random_uniform([500, 100], -2, 3, tf.float64))
b3 = tf.Variable(tf.random_uniform([100], -2, 3, tf.float64))
sik3 = tf.add(tf.matmul(sik2, a3), b3)
sik3 = tf.nn.relu(sik3)

a4 = tf.Variable(tf.random_uniform([100, len(yData[0])], -2, 3, tf.float64))
b4 = tf.Variable(tf.random_uniform([len(yData[0])], -2, 3, tf.float64))
sik4 = tf.add(tf.matmul(sik3, a4), b4)
# sik4 = tf.nn.relu(sik4)    다음 층 계산이 없으니까 제외


dist = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels = y, logits = sik4))

o = tf.train.AdamOptimizer(learning_rate=0.000001)

goal = o.minimize(dist)
##################################################################
s = tf.Session()
s.run(tf.global_variables_initializer())

while True:
    s.run(goal, {x:xData, y:yData})
    # print(s.run(a))
    # print(s.run(b))
    # print("--------")
    d = s.run(dist, {x:xData, y:yData})
    print(d)
    
    if d < 0.7:
        break
##################################################################
xx1 = float(input("fight_scene : "))
xx2 = float(input("bad_language : "))
xxData = [[xx1, xx2]]
result = s.run(tf.argmax(sik4, 1), {x:xxData})
print(result)
print(result[0])
print(label[result[0]])









