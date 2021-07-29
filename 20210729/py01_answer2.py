# -*- coding:utf-8 -*-
import tensorflow as tf


a = tf.Variable(tf.random_uniform([1], -1, 1, tf.float64))
b = tf.Variable(tf.random_uniform([1], -1, 1, tf.float64))
x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

sik = a * x + b

dist = tf.reduce_mean(tf.square(y - sik))
o = tf.train.AdamOptimizer(learning_rate=0.01)
goal = o.minimize(dist)
