'''
Created on 2020. 1. 14.
@author: GDJ19

    <Fibonacci수열>
'''

def fibo(n) :
    # global ..없으면 local variable 에러
    # global 자료형 안 쓸거면 전역변수로 선언한 num값을 지역변수로 불러와야함
#     num1 =0
#     num2 =1
#     num3 =num1+num2

    global num1, num2, num3
    fibolist.append(num1)
    fibolist.append(num2)
    fibolist.append(num3)
    for i in range(3,n) :
        num1 = num2
        num2 = num3
        num3 = num1 + num2
        fibolist.append(num3)

# 전역변수(global)
fibolist =[]
num1 =0
num2 =1
num3 =num1+num2

# main
num = int(input("피보나치 수열을 구할 개수를 입력하세요 (단, 3이상의 값 ) : "))
print("f(",num,")=",end="")
fibo(num)
print(fibolist)