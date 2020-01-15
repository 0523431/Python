'''
Created on 2020. 1. 15.
@author: GDJ19

    <클래스 변수 선언하기>
    - 전역변수 (java에서는 static을 붙여줌)
'''

class Car :
    color =""
    speed =0
    count =0
    num =0
    
    # 생성자 : 객체화할때 호출되는 메서드
    def __init__(self) :
        # 인스턴스 변수
        self.speed =0
        # 클래스 변수
        # 객체생성을 할 때마다 증가
        Car.count +=1
        
        self.num = Car.count
        
        
    def printMessage(self) :
        print("printMessage 메서드 호출")

# null 객체에 아무것도 없는 상태
mycar1, mycar2 = None, None

# 객체화 : 생성자 메서드 호출
mycar1 = Car()
mycar1.speed =30
print("자동차1 : 속도  =%d, 번호 =%d, 생산번호 : %d" % (mycar1.speed, mycar1.num, mycar1.count))

mycar2 = Car()
mycar2.speed =50
print("자동차1 : 속도  =%d, 번호 =%d, 생산된 자동차 총 수량 : %d" % (mycar1.speed, mycar1.num, mycar1.count))
print("자동차2 : 속도  =%d, 번호 =%d, 생산된 자동차 총 수량 : %d" % (mycar2.speed, mycar2.num, mycar2.count))

