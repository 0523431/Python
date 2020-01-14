'''
Created on 2020. 1. 14.
@author: GDJ19

    <Lambda 람다식으로 함수 구현하기>
    - 함수객체
    - 동적으로 함수의 기능을 설정할 수 있음
'''

# 함수의 정의
# 정적이야 = 무조건 합만 구할 수 있는 함수
def hap(num1, num2) :
    res =num1 + num2
    return res

# main
print(hap(10,20))

# 람다 함수
# 동적이야 wow
hap2 = lambda num1,num2 : num1+num2
print("람다 함수 :",hap2(10,20))

hap2 = lambda num1,num2 : num1*num2
print("람다 함수 :",hap2(10,20))

print("위쪽은 java와 같음")
print("매개변수에 기본값 설정하기")
hap3 = lambda num1=111,num2=222 : num1+num2
print("매개변수가 없으면 default,", hap3())
print("두번째 매개변수가 없으면,", hap3(100))
print(hap3(100,200))