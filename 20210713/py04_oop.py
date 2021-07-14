# -*- coding:utf-8 -*-

# class (ex. o = Okt - java중심이라 대문자로 시작) : 객체 만들때 필요한거 -> 안만들꺼면 필요없음
#         만들껀가 / 안만들껀가
#         한 파일에 여러개 만드는게 아니라 클래스 하나당 하나씩 해야 갖다쓰기가 편함

class dog:  # Dog
    # name = None -> 별의미가 없음
    type = "포유류"
    def bark(self):     # 함수안의 메소드
        print('멍ㅋ!')
        
    def printInfo(self): # 메소드의 self -> 자기 자신을 가르키려고
        print(self.name)
        print(self.age)
        print(self.type)
        
    @staticmethod # (변수는 있는데 메소드만 있을때 빨간불끄려면)
    def test():
        print('테스트')

##########
dog.test()

d = dog()   #????
d.name = '똘이'
d.age = 3   # 클래스에 없어도 자유롭게 넣을 수 있음 -> 에러잡기가 어려워짐
# d.type = "포유류"  # 매번 반복해서 안쓸 수 있게 
d.bark()
d.printInfo()
print("====")

d2 = dog()
d2.name = '장군'
d2.age = 2
# d2.type = "포유류"  # 기본값으로 지정
d2.bark()
d2.printInfo()


# 메소드
# 

