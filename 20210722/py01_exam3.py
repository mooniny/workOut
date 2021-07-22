# -*- coding:utf-8 -*-
from cx_Oracle import connect

# sqlplus sdedu/1@121.160.41.151:1521/xe
# 회식메뉴 테이블에, 날씨와 메뉴를 입력받아서 insert하는 Python프로그램을 제작
w = input("날씨 : ")
m = input("회식 메뉴 : ")

con = connect("sdedu/1@121.160.41.151:1521/xe")

sql = "insert into BMIAM_MENU values(BMIAM_MENU_SEQ.nextval, '%s', '%s')" % (w, m)

cur = con.cursor()
cur.execute(sql)

if cur.rowcount == 1:
    print("추가 성공")

con.commit()
con.close()

