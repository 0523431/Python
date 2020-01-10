'''
Created on 2020. 1. 10.
@author: GDJ19
    <function : 간단한 계산기>
'''

# 함수 선언
def calc(v1, v2, op) :
    print("res=",res) # 전연변수에서 선언한 값이 출력됨
    result =0
    if op =='+' :
        result = v1 + v2
    elif op =='-' :
        result = v1 - v2
    elif op =='*' :
        result = v1 * v2
    elif op == "/" :
        result = v1 / v2
    return result
      

# 전역 변수 선언 부분  
res =10
varl, var2, oper = 0, 0, ""

# main 시작
oper = input("계산을 입력하세요(+,=,*,/) : ") # operator값
var1 = int(input("첫번째 수 : "))
var2 = int(input("두번째 수 : "))
res = calc(var1, var2, oper)

print("계산 : %d %s %d = %d" % (var1, oper, var2, res))