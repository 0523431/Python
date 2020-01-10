'''
Created on 2020. 1. 10.
@author: GDJ19

    1. 리턴값을 두개 반환하기 : 리스트로 반환
    2. 가변 매개변수 함수 정의
'''
# 1. 리턴값 두개 반환
def multi(num1, num2) :
    listB = []
    listB.append(num1 + num2)
    listB.append(num1 - num2)
    return listB

# 2. 가변 매개변수
#    0개 이상의 매개변수를 설정할 수 있음
def paramFunc(* p) :
    result =0
    for i in p :
        result +=i
    return result

# 1. 리턴값 두개 반환
listA =[]
hap,sub =0,0
listA = multi(100,200) # return listB
hap = listA[0]
sub = listA[1]
print("multi함수의 리턴값 : %d, %d" % (hap, sub))

# 2. 가변 매개변수
print("paramFunc(10,20) =", paramFunc(10,20))
print("paramFunc(10,20,30) =", paramFunc(10,20,30))
