'''
Created on 2020. 1. 20.
@author: GDJ19

    <yield : 함수의 종료없이, yield 예약어로 값 리턴>
    - 함수의 종료 : 문장의 끝 / return을 만남
    - yield : 함수가 끝나지 않더라도 값을 호출한 함수에게 전달해줌
'''

def genFun(num) :
    for i in range(10, num +10) :
        yield(i)
        print(i, "값 반환")

print(type(genFun(5))) # 10부터 14까지의 값이 출력됨? ㄴㄴ //  # type : generator

# 그 값을 list로 형변환해서 출력할 수 있음
print(list(genFun(5)))

for i in list(genFun(5)) :
    print("yield : ",i)