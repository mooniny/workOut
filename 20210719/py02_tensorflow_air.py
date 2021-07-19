# -*- coding:utf-8 -*-
import tensorflow as tf
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# http://openapi.seoul.go.kr:8088/4f6a6547456b6368333355736a714f/xml/RealtimeCityAir/1/25/

con = HTTPConnection("openapi.seoul.go.kr:8088")
con.request("GET", "/4f6a6547456b6368333355736a714f/xml/RealtimeCityAir/1/25/")
resBody = con.getresponse().read()
con.close()

airData = fromstring(resBody)
xData = []
yData = []
for i in airData.iter("row"):
    # print(i.find("PM10").text))
    # print(i.find("PM25").text))
    xData.append(float(i.find("PM10").text))
    yData.append(float(i.find("PM25").text))
    
#############################################################

a = tf.Variable(tf.random_uniform([1], -2, 3, tf.float64))
b = tf.Variable(tf.random_uniform([1], -2, 3, tf.float64))
x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

sik = a * x + b

dist = tf.reduce_mean(tf.square(y - sik))
o = tf.train.AdamOptimizer(learning_rate=0.1)
goal = o.minimize(dist)

#############################################################

s = tf.Session()
s.run(tf.global_variables_initializer())

while True:
    s.run(goal, {x:xData, y:yData})
    
    print("y = %fx + %f" % (s.run(a),s.run(b)))
    
    d = s.run(dist, {x:xData, y:yData})
    print(d)
    print("----------")
    
    if d < 3.2:
        break
        
#############################################################

xx = float(input("x : "))
result = s.run(sik, {x:xx})[0]
print(result)


