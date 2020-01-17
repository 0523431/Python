'''
Created on 2020. 1. 17.
@author: GDJ19

    <class : 상속 예제, 오버라이딩 >
    - 다중 상속이 가능함
    - 단, 상속받은 클래스에 동일한 변수가 있다면 어느 먼저 상속받은 클래스의 변수를 가져오기때문에 주의해야함
    - ex) 변수 room이 Car에도 있고, Container에도 있으면 상속 순서에 따라 출력되는 mcar.room의 개수가 달라짐
'''

class Car :
    speed =0
    room =100
    def upSpeed(self, value) :
        self.speed +=value
        print("현재 속도(부모클래스) : %d" % self.speed)
        
# 상속표현
class Sedan(Car) :
    pass
    # 추가 되는 멤버가 없는 경우

class Truck(Car) :
    # 인스턴스 메서드
    # 인스턴스 메서드들은 self를 자동으로 가지고 있음 (java의 this)
    def upSpeed(self, value) :
        self.speed +=value
        if self.speed >150 :
            self.speed =150
        print("현재속도(자손클래스) : %d" % self.speed)

class Container :
    room =1
    
class MovingCar(Car, Container) :
    pass

sedan1, truck1, mcar =None, None, None

sedan1 =Sedan()
truck1 =Truck()
mcar =MovingCar()

print("승용차 ->", end="")
sedan1.upSpeed(200)

print("트럭 ->", end="")
truck1.upSpeed(200)

print("이동차 방개수 ->", mcar.room, ", ", end="")
mcar.upSpeed(200)
