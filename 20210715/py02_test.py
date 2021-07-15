# -*- coding:utf-8 -*-
from konlpy.tag._okt import Okt
import matplotlib.pyplot as plt
from wordcloud.wordcloud import WordCloud
from hanspell import spell_checker

o = Okt()
f = open("C:\\Users\\sdedu\\Desktop\\test/naverBlogSearch.txt", "r", encoding = "utf-8")
for line in f.readlines():
    line = line.replace("\n","")
    txt = None
    if txt != "" and txt != None:
        try:
            txt = o.normalize(txt)
            print(txt)
            # txt = spell_checker.check(txt).checked
            # txt = o.nouns(txt)
        except:
            print(txt + "?")
            
f.close()
# wc = WordCloud(font_path ="C:/Users/sdedu/Desktop/test/malgun.ttf", background_color='white').generate(txt)
# plt.imshow(wc)
# plt.show()