# -*- coding:utf-8 -*-
from cx_Oracle import connect

con = None
try:
    con = connect("sdedu/1@121.160.41.151:1521/xe")
    print("연결 성공")
except:
    print("연결 실패")

con.close()