# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads

con = HTTPConnection("openapi.seoul.go.kr:8088")
con.request("GET", "/4f6a6547456b6368333355736a714f/json/RealtimeCityAir/1/25/")
resBody = con.getresponse().read()
con.close()

airData = loads(resBody)
whereSum = {}
whereCount = {}
guName, sum = None, None

for a in airData["RealtimeCityAir"]["row"]:
    guName = a['MSRRGN_NM']
    sum = float(a['PM10']) + float(a['PM25'])
    if guName in whereSum:
        whereSum[guName] += sum
        whereCount[guName] += 1
        
    else:
        whereSum[guName] = sum
        whereCount[guName] = 1
        
where = {}
for k,v in whereSum.items():
    where[k] = v / whereCount[k]
    
print(where)