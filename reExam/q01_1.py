# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads

#http://openapi.seoul.go.kr:8088/4f6a6547456b6368333355736a714f/json/RealtimeCityAir/1/25/
con = HTTPConnection("openapi.seoul.go.kr:8088")
con.request("GET", "/4f6a6547456b6368333355736a714f/json/RealtimeCityAir/1/25/")
resBody = con.getresponse().read()
con.close()

airData = loads(resBody)
for a in airData["RealtimeCityAir"]["row"]:
    print(a['MSRSTE_NM'])
    print(a['MSRSTE_NM'])
    print(a['PM10'])
    print(a['PM25'])
    print("-------")