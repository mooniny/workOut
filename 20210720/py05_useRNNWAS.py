# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from bson.json_util import loads

# http://192.168.0.189:8989/aircon.control?t=30&h=50

t = input("기온 : ")
h = input("습도 : ")

con = HTTPConnection("192.168.0.189:8989")
con.request("GET", "/aircon.control?t=%s&h=%s" % (t, h))
resBody = con.getresponse().read()
con.close()

resultData = loads(resBody)
print(resultData['power'])