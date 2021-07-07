# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
# numpy(np.array) : 1 ~ 2차원 정도의 좋은 list
#                    데이터의 의미를 알기 힘든
#                    matplotlib, pandas등이 써서

a = pd.Series([123, 213, 4])
print(a)
print("-----")
print(a[1])
print("======")
print()

# pandas(pd.DataFrame) : 엑셀의 표 같은 (표 처럼 정렬 출력)
#                        데이터 의미 알기 용이, 다양한 인덱싱
b = pd.DataFrame()
b["이름"] = ["아메리카노", "라떼"]
b["가격"] = [3000, 3500]
print(b)
print("-----")
print(b.iloc[1])    # 특정 데이터에 접근
print("-----")
print(b["이름"])
print("======")
print()

c = pd.DataFrame()
c["이름"] = np.array(["아메리카노", "라떼"])
c["가격"] = np.array([3000, 3500])
c = c.set_index(c["이름"])        # 이름기준으로 데이터 접근 (numpy아니여도 사용가능)
print(c)
print("-----")
print(c.iloc[1])
print("-----")
print(c.loc["아메리카노"])
print("======")
print()

dd = [["아메리카노", 3000], ["라떼", 3500]]
d = pd.DataFrame(dd, columns=['품명', '가격'])
print(d)
print("======")
print()

ee = np.array([["아메리카노", 3000], ["라떼", 3500]])
e = pd.DataFrame(ee, columns=['품명', '가격'])
print(e)
print("======")
print()

ff = {'품명':["아메리카노", "라떼"],
      '가격':[3000, 3500]}
f = pd.DataFrame(ff)
print(f)
print("======")
print()

gg = [{'품명':'아메리카노', '가격':3000},
      {'품명':'라떼', '가격':3500}]
g = pd.DataFrame(gg)
print(g)
print("======")
print()










