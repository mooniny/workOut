# -*- coding:utf-8 -*-
import urllib.request, re
from pip._internal import locations
import pandas as pd

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
html = urllib.request.urlopen(url)
contents = html.read().decode('utf-8')

locations = re.findall(r'<location wl_ver="3">.+?</location>', contents, re.DOTALL)
province = {}
city = {}
rain = {}
wfKor = {}
tmn = {}
tmx = {}
for loc in locations:
    province.append(re.search(r"<province>(.+)</province>", loc))
    city.append(re.search(r"<city>(.+)</city>", loc))
    
    print(province.group(1))
    print(city.group(1))
    
    data = re.findall(r'<data>.+?</data>', loc, re.DOTALL)
    
    for items in data:
        wfKor.append(re.search(r"<wf>(.+)</wf>", items))
        tmn.append(re.search(r"<tmn>(.+)</tmn>", items))
        tmx.append(re.search(r"<tmx>(.+)</tmx>", items))
        rain.append(re.search(r"<rnSt>(.+)</rnSt>", items))
        
        # print(wfKor, tmn, tmx, rain)
 
    
# weatherData = urllib.request(contents)
# weathers = weatherData.iter('body')
# province = []
# city = []
# rain = []
# wfKor = []
# tmn = []
# tmx = []
#
# for w in weathers.find("location"):
    # province.append(w.find("province").text)
    # city.append(w.find("city").text)
    #
# for d in weathers.iter("data"):
    # rain.append(d.find(float("rnSt").text))
    # wfKor.append(d.find("wf").text)
    # tmn.append(d.find(float("tmn").text))
    # tmx.append(d.find(float("tmx").text))
    #
    #
# weatherDF = pd.DataFrame()
# weatherDF['시'] = city
# weatherDF['도'] = province
# weatherDF['강수확률'] = rain
# weatherDF['날씨'] = wfKor
# weatherDF['최고기온'] = tmx
# weatherDF['최저기온'] = tmn
#
# print(weatherDF)


# bs_html = BeautifulSoup(html.content,'html.parser')
#
# location = bs_html.find_all('location')
#
#
# for l in location:
    # city = l.find('city').text
    # print(city)
    # w_list = re.findall('<data>.+?<tmef>(.+?)</tmef>.+?<wf>(.+?)</wf>.+?<tmn>(.+?)</tmn>.+?<tmx>(.+?)</tmx>\n<reliability>(.+?)</reliability>\n</data>',str(l),re.DOTALL)
    # i = 1
    # for w in w_list:
        # print(w[0],w[1],w[2],w[3],w[4])
        #
    # print('-'*30)