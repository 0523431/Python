'''
Created on 2020. 1. 15.
@author: GDJ19

    <컴프리헨션 : 자바에는 없는 표현방법>
'''

print("기존 우리가 알고 있는 표현식")
numbers =[]
for n in range(1, 11) :
    numbers.append(n)
print(numbers)

print()

print("comprehension 방식")
print([x for x in range(1, 11)])

print("comprehension 방식 자체가 list형태", end=", ")
print("numlist =[x for x in range(1, 11)]")
numlist =[x for x in range(1, 11)]
print(numlist)

print()

print("1-10까지 짝수 리스트 생성 : 우리가 알고 있는 표현식")
evenlist =[]
for n in range(1, 11) :
    if n %2 ==0 :
        evenlist.append(n)
print(evenlist)

print("1-10까지 짝수 리스트 생성 : comprehension")
print([x for x in range(1, 11) if x %2 ==0])

print("1-10까지 2의 배수이면서 3의 배수인 수")
print([x for x in range(1, 11) if x %2 ==0 if x %3 ==0])

print()

print("중첩 사용 컴프리헨션")
matrix =[[1,2,3], [4,5,6], [7,8,9]]
list1 = [x for row in matrix for x in row]
'''
    for 부터 해석을 시작
    matrix를 row로 가져와서, row를 x로 다시 가져와?
'''
print(list1)

print()

print("set 컴프리헨션")
set1 = {x**2 for x in [1,2,3]}
print(set1)

print()

print("1부터 10까지 수 중 짝수의 제곱을 출력해보자")
set2 = {x**2 for x in range(1, 11) if x %2==0}
print(set2)