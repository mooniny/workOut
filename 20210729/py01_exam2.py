# -*- coding:utf-8 -*-
import tensorflow as tf
import pandas as pd
from flask.app import Flask
from flask.helpers import make_response
from flask.json import jsonify
from flask.globals import request


xData=[]
yData=[]
f = open("C:\\Users\\sdedu\\Desktop\\test/exam_mosquito.txt", "r", encoding = "utf-8")
for line in f.readlines():
    line = line.replace("\n","").split(",")
    xData.append(line[1])
    yData.append(line[2])
f.close()

a = tf.Variable(tf.random_uniform([1], -2, 3, tf.float64))
b = tf.Variable(tf.random_uniform([1], -2, 3, tf.float64))

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
    # print("y = %fx + %f" % (s.run(a),s.run(b)))
    
    d = s.run(dist, {x:xData, y:yData})
    print(d)
    print("----------")
    
    if d < 0.001:
        break
        
#############################################################

xx = float(input("집 : "))
result = s.run(sik, {x:xx})[0]
print("공원 : ",result)

#############################################################
app = Flask(__name__)

# http://192.168.0.189:6603/park.mosquito?house=35
@app.route("/park.mosquito")
def parkMosquito():
    xx = float(request.args.get("house"))    # 요청 파라메터
    result = s.run(sik, {x:xx})[0]
    resBody = make_response(jsonify({"park":result}))
    return resBody

if __name__=="__main__":
    app.run("0.0.0.0", 6603,True)

