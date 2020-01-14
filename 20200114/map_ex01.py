'''
Created on 2020. 1. 14.
@author: GDJ19

    <map : 리스트의 각각의 요소를 변경>
'''

before = ["2019","07","15"]
print(type(before[0]))

# 리스트의 자료형을 변경시켜주는데 사용함 == map
# int함수를 before리스트의 값 각각에 적용
# int("값") ----> int로 변형시켜주는 함수
after = list(map(int, before))
print(type(after[0]))

mylist = [1,2,3,4,5]
# map을 이용하여 mylist 각각의 값에 10을 더해보자
add = lambda num:num +10
mylist = list(map(add, mylist))
print(mylist)

list1 = [1,2,3,4]
list2 = [10,20,30,40]
haplist = []
# haplist에 list1과 list2의 각각을 더한 값을 저장해보자 1
hap = lambda num1,num2 : num1+num2
for i in range(0,len(list1)) :
    haplist.append(hap(list1[i],list2[i]))
print(haplist)
# haplist에 list1과 list2의 각각을 더한 값을 저장해보자 2
hap = lambda num1,num2 : num1+num2
haplist = list(map(hap,list1,list2))
print("map을 사용함 : ",haplist)
# haplist에 list1과 list2의 각각을 더한 값을 저장해보자 3
haplist = list(map(lambda num1,num2 : num1+num2,list1,list2))
print("map을 사용하고 lambda 바로 적용 : ",haplist)