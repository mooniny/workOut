# -*- coding:utf-8 -*-
import os
import cv2
import tensorflow as tf

# 1번 : 그림 그린 파일 캡쳐


x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

a1 = tf.Variable(tf.random_uniform([len(xData[0]), 100], -2, 3, tf.float64))
b1 = tf.Variable(tf.random_uniform([100], -1, 1, tf.float64))
sik1 = tf.add(tf.matmul(x, a1), b1)
sik1 = tf.nn.relu(sik1)

a2 = tf.Variable(tf.random_uniform([100, 200], -2, 3, tf.float64))
b2 = tf.Variable(tf.random_uniform([200], -2, 3, tf.float64))
sik2 = tf.add(tf.matmul(sik1, a2), b2)
sik2 = tf.nn.relu(sik2)

a3 = tf.Variable(tf.random_uniform([200, len(label)], -2, 3, tf.float64))
b3 = tf.Variable(tf.random_uniform([len(label)], -2, 3, tf.float64))
sik3 = tf.add(tf.matmul(sik2, a3), b3)

dist = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels = y, logits = sik3))
o = tf.train.AdamOptimizer(learning_rate=0.000001)
goal = o.minimize(dist)