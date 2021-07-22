# -*- coding:utf-8 -*-
from cx_Oracle import connect
from apyori import apriori
from http.client import HTTPSConnection
from json import loads

con = HTTPSConnection("api.openweathermap.org")
con.request("GET", "/data/2.5/weather?lat=37.50252869790909&lon=127.0237229133084&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = con.getresponse().read()
con.close()
weatherData = loads(resBody)
weather = weatherData["weather"][0]["description"]
print('today :', weather)

con = connect("sdedu/1@121.160.41.151:1521/xe")
sql = "select * from BMIAM_MENU"
cur = con.cursor()
cur.execute(sql)
data = []
for _, w, m in cur:
    # print(w, m)
    data.append([w,m])
con.close()

result = list(apriori(data, min_support = 0.01, min_confidence = 0.5))
for r in result:
    for r2 in r.ordered_statistics:
        ib = list(r2.items_base)
        ia = list(r2.items_add)
        if weather in ib or weather in ia:
            print(ib, '->', ia, ': %.1f%%' % (r2.confidence * 100))
        
    