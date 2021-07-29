# -*- coding:utf-8 -*-
import tensorflow as tf


f = open("C:\\Users\\sdedu\\Desktop\\test/exam_mosquito2.csv", "r", encoding = "utf-8")
xData=[]
yData=[]
for line in f.readlines():
    line = line.replace("\n","").split(",")
    xData.append(line[1])
    yData.append(line[2])
f.close()

#############################################################

a = tf.Variable(tf.random_uniform([1], -1, 1, tf.float64))
b = tf.Variable(tf.random_uniform([1], -1, 1, tf.float64))
x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

sik = a * x + b

dist = tf.reduce_mean(tf.square(y - sik))
o = tf.train.AdamOptimizer(learning_rate=0.01)
goal = o.minimize(dist)

#############################################################

s = tf.Session()
s.run(tf.global_variables_initializer())

for _ in range(100000):
    s.run(goal, {x:xData, y:yData})
    d = s.run(dist, {x:xData, y:yData})
    print(d)

print("y = %fx + %f" % (s.run(a),s.run(b)))
