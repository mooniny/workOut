# -*- coding:utf-8 -*-
from cx_Oracle import connect
import pandas as pd

# sqlplus sdedu/1@121.160.41.151:1521/xe
con = connect("sdedu/1@121.160.41.151:1521/xe")
sql = "select * from BMIAM_MENU"
cur = con.cursor()
cur.execute(sql)
bmiMenuDF = pd.read_sql(sql, con)
print(bmiMenuDF)


con.close()

