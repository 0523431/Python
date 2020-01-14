'''
Created on 2020. 1. 14.
@author: GDJ19

    <리스트에서 중복된 요소를 제거하기>
'''

list1 = [1,1,1,2,2,3,3,3,4,4,5]
list1 = list(set(list1))
print(list1)

for i in range(len(list1)-1) :
    if list1[i] == list1[i+1] :
        del(list[i])
print(list1)
