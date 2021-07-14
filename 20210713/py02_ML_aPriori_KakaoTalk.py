# -*- coding:utf-8 -*-
from apyori import apriori

# for p in range(1, 6):
    # f = open('C:\\Users\\sdedu\\Desktop\\test\\iruri/Talk_%d.txt' % (p), 'r', encoding='utf-8')

f = open('C:\\Users\\sdedu\\Desktop\\test\\iruri/Talk_1.txt', 'r', encoding='utf-8')
who = None
data = []
    
for i, line in enumerate(f.readlines()):
    if i > 3 :
        line = line.replace("\n", "").split(" : ")
        txt = None
        if len(line) >= 2:
            txt = line[1]
            who = line[0].split(", ")[-1]
        # elif not line[0].startswith('20'):
            # txt = line[0]
        # print(who,txt)
            
        if txt != None:
            d = []
            d.append(who)
            for t in txt.split(" "):
                d.append(t)
            data.append(d)
            # print(t)
            # print("-----")
            # print(d)
            # print("-----")
f.close()
        
whoList = []
for w in data:
    if w[0]!='주차장' and w[0]!='톡딜가' and w[0]!='출처' and w[0]!='주소' and w[0]!='상품명':
        whoList.append(w[0])
whoList = list(set(whoList))
print(whoList)

result = list(apriori(data, min_support = 0.001, min_confidence = 0.02))
# result = apriori(data, min_support = 0.01, min_confidence = 0.3)
# result = list(result)
# print(result)
for r in result:
    # print(r)
    for r2 in r.ordered_statistics:
        # print(r2)
        # print(r2.items_base, '->', r2.items_add, ' : ', r2.confidence)
        # print("-----")
        ib = list(r2.items_base)
        # print(ib)
        if len(ib) == 1 and ib[0] in whoList:
            print(ib[0],'가 ', list(r2.items_add), '을 말할 확률은', r2.confidence)


    
