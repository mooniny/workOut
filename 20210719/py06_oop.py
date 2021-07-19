# -*- coding:utf-8 -*-

# OOP : 객체라는 걸로 실생활을 표현 -> Python이 인간의 언어에 가까워지게
#       -> 유지보수에 용이 -> 쉽다
#       #객체지향 : 은닉

# OOD
#    1) 실제 상황을 떠올리기
#    2) 이 프로그램에 필요없는거 제외하고 객체로
#    3) 그 객체가 어떤 속성이고, 어떻게 행동을 하는지
class Doctor:
    def start(self):
        p = self.callPatient()      # 환자를 부른다.
        self.askHeight(p)           # 데려다 놓고 키 물어보기
        self.askWeight(p)           # 데려다 놓고 몸무게 물어보기
        self.calculate(p)           # 비만도 계산하기
        self.tellResult(p)          # 결과 말해주기
        
    
    def callPatient(self):
        return Patient()            # 환자 객체를 만든다.
    
    def askHeight(self, p):
        p.tellHeight()
    
    def askWeight(self, p):
        p.tellWeight()
    
    def calculate(self, p):
        hm = p.height / 100
        p.bmi = p.weight / (hm * hm)
        p.status = '저체중'
        if p.bmi >= 35:
            p.status = '고도비만'
        elif p.bmi >= 30:
            p.status = '중도비만'
        elif p.bmi >= 25:
            p.status = '경도비만'
        elif p.bmi >= 23:
            p.status = '과체중'
        elif p.bmi >= 18.5:
            p.status = '정상'
        
        
    def tellResult(self, p):
        print("BMI : %f" % p.bmi)
        print("판정 : %s" % p.status)
        


class Patient:
    # name = None -> 파이썬이라서 의미가 없는
    def tellHeight(self):
        self.height = float(input("키 : "))
    
    def tellWeight(self):
        self.weight = float(input("몸무게 : "))

###########################
d = Doctor()    # 출근해서
d.start()       # 업무시작    ***여기는 너무 많이쓰는거 X


