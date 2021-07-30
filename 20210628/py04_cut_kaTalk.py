# -*- coding:utf-8 -*-
import pandas as pd
from sys import maxunicode
from unicodedata import category

f = open("C:\\Users\\sdedu\\Desktop\\test\\iruri/Talk1.txt", "r", encoding = 'utf-8')
first = True
wc = {}
special = []
for i in range(maxunicode):
    if category(chr(i)).startswith("P"):
        special.append(chr(i))
print(special)
print(len(special))
# special = list(set(special))
# print(special)
# print(len(special))
for line in f.readlines():
    line = line.replace("\n", "").split(" : ")
    if len(line) == 2:
        if first:
            first = False
        else:
            for s in special:
                line[1] = line[1].replace(s, " ")
            print(line[1])
            if line[1].find('이모티콘') == -1 and line[1].find('사진') == -1 and line[1].find('jpg') == -1 and line[1].find('png') == -1 and line[1].find('m4a') == -1 and line[1].find('동영상') == -1:
                for w in line[1].split(" "):
                    if w in wc:
                        wc[w] += 1
                    else:
                        wc[w] = 1
f.close()

word = []
count = []
for k,v in wc.items():
    word.append(k)
    count.append(v)
    
wcDF = pd.DataFrame()
wcDF['단어'] = word
wcDF['횟수'] = count
wcDF = wcDF.sort_values(by = '횟수', ascending=False)
print(wcDF.head(20))

# pd.DataFrame을 csv로 내보내기
wcDF.to_csv('C:\\Users\\sdedu\\Desktop\\test/kakaoResult.csv', header=False, index=False)

# 넘파이 판다스로 분석
# 멧플로립/시본으로 시각확
#
# 넘파이 판다스 분석결과 시에스브이
# 하둡결과 txt로 나온ㅡㄴ데
# R로 시각화

