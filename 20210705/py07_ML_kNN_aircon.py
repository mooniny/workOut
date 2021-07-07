# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.neighbors._classification import KNeighborsClassifier
from http.client import HTTPSConnection
from bson.json_util import loads
from sklearn.preprocessing._data import MinMaxScaler

airconDF = pd.read_csv("C:\\Users\\llaum\\Desktop\\owmWeather/owmWeather.csv", name=['Year','Month','Day','Hour','Minute','Weather','Temp','Humi','Power'])

trainData = airconDF[['Temp','Humi']].to_numpy()
label = airconDF['Air condition']

mms = MinMaxScaler()        # 20210706; 정규화
trainData = mms.fit_transform(trainData)

knc = KNeighborsClassifier(3)
knc.fit(trainData, label)

con = HTTPSConnection("api.openweathermap.org")
con.request("GET", "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = con.getresponse().read()
con.close()

weatherData = loads(resBody)
t = weatherData['main']['temp']
h = weatherData['main']['humidity']
# t = float(input("temperature : "))
# h = float(input("Humidity : "))
what = [[t, h]]
what = mms.transform(what)

result = knc.predict(what)
print(t)
print(h)
print(result[0])

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

fontFile = "C:/Users/sdedu/Desktop/test/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=20).get_name()
plt.rc("font", family=fontName)
sns.scatterplot(x="temp", y = "humi", hue = "Air_con", data=airconDF)
plt.show()
