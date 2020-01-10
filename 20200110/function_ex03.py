'''
Created on 2020. 1. 10.
@author: GDJ19

    <전역 변수 사용하기>
'''

# 함수 선언
def func1() :
    # 지역변수
    gval =200
    print("func1()함수 호출당하고, 지역변수 gval 출력", gval)
    
    global globalVal
    globalVal =300
    a =20 # 지역변수
    b =1000
    print("func1()함수 호출당하고, 전역변수 globalVal 출력", globalVal)
    print(a, b)
    
def func2() :
    print("func2()함수에서 func1()함수를 호출함 =====>")
    func1()
    print("전역변수 gval의 값 =", gval)
    print("func1()함수에서 전역변수로 선언한 globalVal의 값 =", globalVal)
    print(a)
    
# 전연변수 선언 (모든 함수에서 사용이 가능한 변수)
gval =100 # global value
a =10

# 프로그램의 시작(main 시작)
if __name__== '__main__' :
    func2()