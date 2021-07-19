# -*- coding:utf-8 -*-
'''
    >>가제 : 나의 작고 소듕한 친구는 언제 떡상을 할까?
    
    MZ세대의 유입으로 SNS와 다양한 미디어 매체의 언론보도가 폭포처럼 쏟아진다.
    뉴스가 주가에 미치는 영향은?
    주식공부! 뉴스를 많이보는게 도움은 되지만 나 너무 흔들리는거 아닐까?
    주가 데이터와 뉴스데이터의 비교분석!
    
    >> 시장의 핫이슈 빅4 : 삼성전자, 엘지전자, 카카오, 네이버 로 비교 분석 해보자
    
    
'''
from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring

# 네이버 뉴스 크롤링
    
def cut(s):
    s = s.replace("<b>", "").replace("</b>", "").replace("&quot;", "")
    return s
   
search = quote('삼성전자')        

h = {"X-Naver-Client-Id" : "gHKtdtM_pLs3ZHJb2YCo",
     "X-Naver-Client-Secret" : "qL_1zOFWVU"}

# f = open("C:\\Users\\sdedu\\Desktop\\test/naverNews.txt", "a", encoding = "utf-8")

con = HTTPSConnection("openapi.naver.com")
for p in range(1,1001,100):
    con.request("GET","/v1/search/news.xml?query=" + search + "&display=100&start=%d" % (p), headers=h)
    resBody = con.getresponse().read()
    print(resBody.decode())
    con.close()

    ssNewsData = fromstring(resBody)
    news = ssNewsData.getiterator("item")
    print(news)
    for i in news:
        print(cut(i.find("title").text))
        # print(cut(i.find("description").text))
        print('---')
        # f.write(""(cut(i.find("title").text)))

# f.close()


