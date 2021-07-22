# -*- coding:utf-8 -*-
from cx_Oracle import connect
from apyori import apriori

# sqlplus sdedu/1@121.160.41.151:1521/xe
# OracleDB에 저장된 회식메뉴에, a priori 머신러닝 알고리즘을 활용(최소 지지도 0.01, 최소 신뢰도 0.5로 설정)하여 연관관계 분석을 진행.

con = connect("sdedu/1@121.160.41.151:1521/xe")
sql = "insert into BMIAM_MENU "

sql = "select BM_WEATHER, BM_MENU"
sql +=" from BMIAM_MENU"
sql +=" order by BM_NO"
cur = con.cursor()
cur.execute(sql)

data = []
for d in cur:
    data.append(d)

con.close()

result = list(apriori(data, min_support = 0.01, min_confidence = 0.5))
# print(result)
for r in result:
    # print(r)
    for r2 in r.ordered_statistics:
        # ib = list(r2.items_base)
        # print(ib)
        # if len(ib) == 1 and ib[0]:
            # print(ib[0],'->', list(r2.items_add), ' : ', '%d%%' %(r2.lift))
        # print('------')
        print(list(r2.items_base), '->',list(r2.items_add),' : ', '%d%%' % (r2.lift))
        
        