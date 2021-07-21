# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

# https://vip.mk.co.kr/newSt/price/daily.php?p_page=3&y1=2021&m1=02&d1=22&y2=2021&m2=07&d2=21&stCode=005930
cCode = '005930'

con = HTTPSConnection("vip.mk.co.kr")
for page in range(1, 3):
    con.request("GET", "/newSt/price/daily.php?p_page=%d&y1=2021&m1=02&d1=22&y2=2021&m2=07&d2=21&stCode=%s" % (page, cCode))
    rb = con.getresponse().read()
    print(rb)
    # ssMarketData = BeautifulSoup(rb, "html.parser", from_encoding = "utf-8")
    # ssMarketDatas = ssMarketData.select("table.type2 tbody tr td span")
    # for m in ssMarketDatas:
        # print(m.text.strip())


'''
 - 주식시장 일별시세 표, 파싱해서 
    => 날짜, 종가, 전일비, 시가, 고가, 저가, 거래량
    => pandas?
   
 - 기사 수와 전일 대비 등락정도 비교
 
 - 기사 수↑, 상승 => 기사 전문 텍스트 정제시켜서 워드클라우드?!
 - 기사 수↑, 하락 => 
 - 기사 수↓, 상승 => 
 - 기사 수↓, 하락 => 
   
 - 기사 수와 주가의 상관관계 도출 => AI학습으로 매도, 매수 프로그램  
    
'''
    