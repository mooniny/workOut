# -*- coding:utf-8 -*-
import pandas as pd

a = pd.DataFrame()
a['품명'] = ['모니터', '키보드']
a['가격'] = [100000, 15000]
print(a)
print("=====")

aa = pd.Series(['마우스', 12000], index=['품명', '가격'])
# print(a[1])
a = a.append(aa, ignore_index=True) # [0], [1]체제 하지 않도록
print(a)
print("=====")

aaa = {'품명':'마이크', '가격':30000}
a = a.append(aaa, ignore_index = True)
print(a)
print("=====")

# bhResult2.txt를 DataFrame으로
# 명절 : 
# 공휴일 : 
# 입력받아서 DataFrame에 추가되게

b = pd.read_csv("C:\\Users\\sdedu\\Desktop\\test/bhResult2.txt", sep='\t', names=['요일', '이용객수'])
m = input("명절: ")
g = input("공휴일: ")
mm = {'언제': '명절', '얼마나':m}
gg = {'언제': '공휴일', '얼마나':g}
b = b.append(mm, ignore_index = True)
b = b.append(gg, ignore_index = True)
print(b)


