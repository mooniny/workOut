# -*- coding:utf-8 -*-
from cx_Oracle import connect
from apyori import apriori
from http.client import HTTPSConnection
from json import loads

# sqlplus sdedu/1@121.160.41.151:1521/xe
#  현재 학원위치의 날씨를 구해서, 오늘 회식 메뉴를 추천해주는 OracleDB+Python AI 플랫폼을 최종 완성/테스트를 진행하고, 소스와 결과를 캡쳐하시오.

data = []
def conDB():
    con = connect("sdedu/1@121.160.41.151:1521/xe")
    sql = "insert into BMIAM_MENU "
    
    sql = "select BM_WEATHER, BM_MENU"
    sql +=" from BMIAM_MENU"
    sql +=" order by BM_NO"
    cur = con.cursor()
    cur.execute(sql)
    
    for d in cur:
        data.append(d)
    # print(data)
    con.close()


# https://api.openweathermap.org/data/2.5/weather?lat=37.50252869790909&lon=127.0237229133084&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr
con = HTTPSConnection("api.openweathermap.org")
con.request("GET", "/data/2.5/weather?lat=37.50252869790909&lon=127.0237229133084&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = con.getresponse().read()
con.close()
    
weatherData = loads(resBody)
    # for bb in weatherData["weather"][0]["description"]:
        # print(bb)
        # ee.append(bb)
        # print(ee)
aa = weatherData["weather"][0]["description"]
print(aa)

def aPriori():
    result = list(apriori(data, min_support = 0.01, min_confidence = 0.5))
    for r in result:
        for r2 in r.ordered_statistics:
            ib = list(aa)
            if ib in data:
                print(ib,'->', list(r2.items_add), ' : ', '%d%%' %(r2.lift))
            # print('------')
            # print(list(r2.items_base), '->',list(r2.items_add),' : ', '%d%%' % (r2.lift))
        
        
#################################
# conDB()
# conAPI()
aPriori()
       