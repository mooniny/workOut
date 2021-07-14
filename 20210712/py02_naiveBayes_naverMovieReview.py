# -*- coding:utf-8 -*-

# 파일 읽어서 리뷰 내용만 출력
f = open("C:\\Users\\sdedu\\Desktop\\test/naverMovie.txt", "r",encoding = "utf-8")
f2 = open("C:\\Users\\sdedu\\Desktop\\test/naverMovieLabel.txt", "a", encoding = "utf-8")  # 결과파일로 저장
for line in f.readlines():
    line = line.replace("\n","").split("|")
    print(line[4], ':', line[6])  # 영화제목, 리뷰
    what = input('정상 or 걸러 : ')     # 판단(지도학습)
    f2.write("%s\n" % what)
        
f2.close()
f.close()



