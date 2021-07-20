# -*- coding:utf-8 -*-
import tensorflow as tf
import pandas as pd
from flask.app import Flask
from flask.globals import request
from flask.helpers import make_response
from flask.json import jsonify

app = Flask(__name__)   # 서버화 시키기

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
print(xData)
print(yData)

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

dist = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels = y, logits = sik4))
o = tf.train.AdamOptimizer(learning_rate=0.0001)
goal = o.minimize(dist)

##################################################################
s = tf.Session()
s.run(tf.global_variables_initializer())

while True:
    s.run(goal, {x:xData, y:yData})
    d = s.run(dist, {x:xData, y:yData})
    print(d)
    
    if d < 700:
        break
##################################################################

# http://192.168.0.189:8989/aircon.control?t=30&h=50
@app.route("/aircon.control")
def controlAircon():
    xx1 = float(request.args.get("t"))
    xx2 = float(request.args.get("h"))
    xxData = [[xx1, xx2]]
    
    result = s.run(tf.argmax(sik4, 1), {x:xxData})
    
    f = open("C:\\Users\\sdedu\\Desktop\\test\\owmWeather/owmWeather.csv",'a',encoding='utf-8')
    f.write('0,0,0,0,0,ㅋ,%f,%f,%s\n' % (xx1, xx2, label[result[0]]))
    f.close()
    
    d = {"power" : label[result[0]]}
    resBody = make_response(jsonify(d))
    return resBody

if __name__ == '__main__':
    app.run("0.0.0.0", 8989, True)



