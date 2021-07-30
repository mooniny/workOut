# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# http://openapi.seoul.go.kr:8088/4f6a6547456b6368333355736a714f/xml/GetParkInfo/14600/14687
f = open("C:\\Users\\sdedu\\Desktop\\test/getParkInfo.csv", "a", encoding="utf-8")
con = HTTPConnection("openapi.seoul.go.kr:8088")
test = {}
for start in range(1,14002,1000):
    con.request("GET","/4f6a6547456b6368333355736a714f/xml/GetParkInfo/%d/%d" % (start, start + 999))
    rb = con.getresponse().read()
    for p in fromstring(rb).iter("row"):
        addr = p.find("ADDR").text
        if addr in test:
            print(addr + "은 중복")
        else:
            test[addr] = "ㅋ"
            pnm = p.find("PAY_NM").text
            lat = p.find("LAT").text
            lng = p.find("LNG").text
            if pnm != None and lat != None and lng != None:
                f.write(pnm + ',' + lat + ',' + lng + '\n')

print("END")
con.close()
f.close()