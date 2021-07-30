# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads

# http://openapi.seoul.go.kr:8088/4f6a6547456b6368333355736a714f/json/GetParkInfo/1/1000/
con = HTTPConnection("openapi.seoul.go.kr:8088")
f = open("C:\\Users\\sdedu\\Desktop\\test/parkinglot.csv", "a", encoding = "utf-8")

for start in range(1, 14690, 1000):
    con.request("GET", "/4f6a6547456b6368333355736a714f/json/GetParkInfo/%d/%d/" % (start, start+999))
    resBody = con.getresponse().read()

    pkLotData = loads(resBody)
    for p in pkLotData["GetParkInfo"]["row"]:
        # f.write("%s," % p["PARKING_NAME"])
        # f.write("%s," % p["ADDR"])
        f.write("%s," % p["PAY_NM"])
        f.write("%.6f," % p["LAT"])
        f.write("%.6f\n" % p["LNG"])
    

# print(pkLotData)
con.close()
f.close()
# 데이터 수가 많이 않을경우엔 for문보다는 /1/1000, /1001/2000 이런식으로 두번 써서 돌린다(위아래로)