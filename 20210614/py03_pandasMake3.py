# -*- coding:utf-8 -*-
import pandas as pd
from cx_Oracle import connect

# 첫줄을 제목으로
a = pd.read_csv("C:\\Users\\sdedu\\Desktop\\test/titanic.csv")
print(a)
print("=====")

# 첫 줄이 제목이 아닌 경우
b = pd.read_csv("C:/Users/sdedu/Desktop/test/seoulSubway.csv", names=['년', '월', '일', '노선', '역', '타', '내리'])
print(b)
print("=====")

# 다른 파일
c = pd.read_csv("C:\\Users\\sdedu\\Desktop\\test/bhResult2.txt", sep='\t', names=['요일', '이용객수'])
print(c)
print("=====")

con = connect("moony/pink88@192.168.0.131:1521/xe")
sql = "select * from exam_student_list"
d = pd.read_sql(sql, con)
con.close()
print(d)
print("=====")