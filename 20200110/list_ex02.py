'''
Created on 2020. 1. 10.
@author: GDJ19

    <리스트의 기본 함수>
'''

mylist = [30, 10, 20]
print("리스트 : %s" % mylist) # %s : 내부적으로 list를 문자열로 인식함을 알 수 있음

mylist.append(40)
print("mylist.append(40) 이후 리스트 : %s" % mylist)

print("pop()-마지막에 들어간 값을 꺼냄- 메서드 결과 : %s" % mylist.pop())
print("mylist.pop() 이후 리스트 : %s" % mylist)

mylist.sort()
print("mylist.sort()-정렬- 이후 리스트 : %s" % mylist)

mylist.reverse()
print("mylist.reverse() 이후 리스트 : %s" % mylist)

print("20의 위치 : %d" % mylist.index(20))

mylist.insert(2, 222)
print("mylist.insert(2, 222) 이후 리스트 : %s" % mylist)

mylist.remove(222)
print("mylist.remove(222) 이후 리스트 : %s" % mylist)

mylist.extend([77, 88, 77])
print("mylist.extend([77, 88, 77]) 이후 리스트 : %s" % mylist)

print("77의 개수 : %d" % mylist.count(77))