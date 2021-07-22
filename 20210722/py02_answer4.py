# -*- coding:utf-8 -*-
from cx_Oracle import connect
from apyori import apriori

con = connect("sdedu/1@121.160.41.151:1521/xe")
sql = "select * from BMIAM_MENU"
cur = con.cursor()
cur.execute(sql)
data = []
for _, w, m in cur:
    # print(w, m)
    data.append([w,m])
con.close()

result = list(apriori(data, min_support = 0.01, min_confidence = 0.5))
for r in result:
    for r2 in r.ordered_statistics:
        ib = list(r2.items_base)
        ia = list(r2.items_add)
        print(ib, '->', ia, ': %.1f%%' % (r2.confidence*100))
        
    