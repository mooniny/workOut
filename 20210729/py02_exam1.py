# -*- coding:utf-8 -*-
import os
import cv2

def loadFile(folder):
    imgs=[]
    for f in os.listdir(folder):
        print(f)
        img = cv2.imread(folder + "/" + f, cv2.IMREAD_GRAYSCALE)
        img = img.flatten()
        imgs.append(img)
        print(img)
    return imgs

###############################################################

xData = loadFile('C:\\Users\\sdedu\\Desktop\\test\\emoji')
yData = [0,0,0,0,0, 1,1,1,1,1]
label = ['기분이 좋다.', '기분이 안좋다']

###############################################################

# x = tf.placeholder(tf.float64)
# y = tf.placeholder(tf.float64)
#
# a1 = tf.Variable(tf.random_uniform([len(xData[0]), 100], -2, 3, tf.float64))
# b1 = tf.Variable(tf.random_uniform([100], -1, 1, tf.float64))
# sik1 = tf.add(tf.matmul(x, a1), b1)
# sik1 = tf.nn.relu(sik1)
#
# a2 = tf.Variable(tf.random_uniform([100, 200], -2, 3, tf.float64))
# b2 = tf.Variable(tf.random_uniform([200], -2, 3, tf.float64))
# sik2 = tf.add(tf.matmul(sik1, a2), b2)
# sik2 = tf.nn.relu(sik2)
#
# a3 = tf.Variable(tf.random_uniform([200, len(label)], -2, 3, tf.float64))
# b3 = tf.Variable(tf.random_uniform([len(label)], -2, 3, tf.float64))
# sik3 = tf.add(tf.matmul(sik2, a3), b3)
#
# dist = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels = y, logits = sik3))
# o = tf.train.AdamOptimizer(learning_rate=0.000001)
# goal = o.minimize(dist)
#
# # ##################################################################
# s = tf.Session()
# s.run(tf.global_variables_initializer())
#
# yData = s.run(tf.one_hot(yData, len(label)))
#
# while True:
    # s.run(goal, {x:xData, y:yData})
    # d = s.run(dist, {x:xData, y:yData})
    # print(d)
    # if d < 10:
        # break
# # ##################################################################
#
# while True:
    # fName = input('경로 : ')
    # i = cv2.imread(fName, cv2.IMREAD_GRAYSCALE)
    # i = [i.flatten()]
    # result = s.run(tf.argmax(sik3, 1), {x:i})
    # print(label[result[0]])

