'''
Created on 2020. 1. 17.
@author: GDJ19
    
    <추상클래스와 메서드>
'''

class SuperClass :
    # 추상메서드
    def method(self) :
        # 반드시 오버라이딩 해야함
        raise NotImplementedError
    
class SubClass1(SuperClass) :
    def method(self) :
        print("SubClass1에서  method()를 오버라이딩 함")

class SubClass2(SuperClass) :
    # 추상메서드를 상속받았기때문에 반드시 오버라이딩 해야함
    # pass
    def method(self) :
        print("SubClass2에서  method()를 오버라이딩 함")

sub1 = SubClass1()
sub2 = SubClass2()

sub1.method()
sub2.method()