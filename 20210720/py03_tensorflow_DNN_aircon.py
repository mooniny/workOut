# -*- coding:utf-8 -*-
import tensorflow as tf
import pandas as pd

# 에어콘
# def power():
    # if power == "강":
        # print("[1, 0, 0]")
    # elif power =="중":
        # print('[0, 1, 0]')
    # else:
        # print('[0, 0, 1]')
        #

airconDF = pd.read_csv("C:\\Users\\sdedu\\Desktop\\test\\owmWeather/owmWeather.csv", names=['Year','Month','Day','Hour','Minute','Weather','Temp','Humi','Power'])
xData = airconDF[['Temp','Humi']].to_numpy()
label = airconDF['Power'].unique().tolist()      # 중복 제거.list추가

def convert(t):
    return label.index(t)

airconDF["Power2"] = airconDF['Power'].apply(convert) # power의 강중약이 리스트 몇번에 위치하는지 보여주기

yy = airconDF['Power2'].to_numpy()
yData=[]
for v in yy:
    l = []        # 각각 하나가 리스트로 바뀌어야
    for i in range(len(label)):
        # print(i)
        if i == v:
            l.append(1)
        else:
            l.append(0)
    yData.append(l)
# print(yData)


# xData=[]
# yData=[]
# f = open("C:\\Users\\sdedu\\Desktop\\test\\owmWeather/owmWeather.csv", "r", encoding="utf-8")
# for line in f.readlines():
    # line = line.replace("\n","").split(",")
    # xData.append(line[6], line[7])
    # yData.append(line[8])
    # print(xData)
    # print(yData)
    # for temp, humi in f.readlines():
        # temp = 
# f.close()

# xData = [기온, 습도]
# yData = [1, 0, 0], [0, 1, 0],[0, 0, 1],...
# label = ['강', '중', '약']

# ##################################################################
x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

a1 = tf.Variable(tf.random_uniform([len(xData[0]), 100], -2, 3, tf.float64))
b1 = tf.Variable(tf.random_uniform([100], -2, 3, tf.float64))
sik1 = tf.add(tf.matmul(x, a1), b1)
sik1 = tf.nn.relu(sik1)

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
    # print(d)
    
    if d < 100:
        break
##################################################################
xx1 = float(input("fight_scene : "))
xx2 = float(input("bad_language : "))
xxData = [[xx1, xx2]]
result = s.run(tf.argmax(sik4, 1), {x:xxData})
print(result)
print(result[0])
print(label[result[0]])









