# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from bson.json_util import loads

f = open("C:\\Users\\sdedu\\Desktop\\test/exam_mosquito2.csv", "a", encoding = "utf-8")
con = HTTPConnection("openapi.seoul.go.kr:8088")

for y in range(2020,2022):
    for m in range(5,13):       # 사이트에 5월부터 있다고 되어있음
        for d in range(1,32):
            when = "%d-%02d-%02d" % (y, m, d)
            con.request("GET", "/4f6a6547456b6368333355736a714f/json/MosquitoStatus/1/5/" + when)
            resBody = con.getresponse().read()
            mqData = loads(resBody)
            mqData = mqData.find("row")
            for i in mqData:
                f.write("%s," % when)
                f.write("%s," % mqData["MosquitoStatus"]["row"][0]["MOSQUITO_VALUE_HOUSE"])
                f.write("%s," % mqData["MosquitoStatus"]["row"][0]["MOSQUITO_VALUE_PARK"])
        if y == 2021 and m == 6:
            break        
            
con.close()
f.close()

# 2년치 데이터니까 반복문은좀 과하지 않나..