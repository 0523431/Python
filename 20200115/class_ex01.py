'''
Created on 2020. 1. 15.
@author: GDJ19

    <클래스 예제>
'''

print("기본 생성자 : __init__(self)")
print("구현된 생성자가 없는 경우, 시스템이 제공하는 생성자")
class Car :
    # 변수
    color =""
    speed =0
    
    # 생성자 : 객체생성에 관여하는 메서드
    # self ==> 자기 참조 변수 this와 같은 역할
    def __init__(self, v1="", v2=0) :
        self.color = v1
        self.speed = v2
    # method
    def upSpeed(self, value) :
        self.speed +=value
    def downSpeed(self, value) : # method
        self.speed -=value

# 객체화 (기본)
# 그냥 이렇게 쓰면, 생성자 조건에 맞지않아서 오류
# 생성자에 default값을 넣어주면 해결 ! 
myCar1 = Car()
myCar1.color ="빨강"
myCar1.speed =0
myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다" % (myCar1.color, myCar1.speed))

# 객체화 (생성자 조건에 맞게)
myCar2 = Car("Black", 50)
myCar2.downSpeed(20)
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다" % (myCar2.color, myCar2.speed))
