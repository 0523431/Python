'''
Created on 2020. 1. 10.
@author: GDJ19

    <tuple : 변경불가 리스트(상수처리된 리스트)>
'''

# tuple 선언
tp1 = (10, 20, 30)
print(tp1)
#tp1.append(10) 변경불가
print(tp1[0],tp1[1],tp1[2])
#tp1[0] = 100 변경불가

# 그럼에도 tuple을 바꾸고 싶다면 list로 변환시키면 됨
print(type(tp1)) # <class 'tuple'>
list = list(tp1)
print(type(list)) # <class 'list'>
list.append(40)
tp1 = tuple(list) # list를 tuple로 변환
print(tp1)

print()
print("tp1의 크기", len(tp1), "/ list의 크기", len(list))
print("tp1[1:3]=", tp1[1:3], "/ list[1:3]=", list[1:3])
print("tp1[:3]=", tp1[:3], "/ list[:3]=", list[:3])
print("tp1[2:]=", tp1[2:], "/ list[2:]=", list[2:])
print("tp1[::2]=", tp1[::2], "/ list[::2]=", list[::2])
print("결론 : tuple과 list는 동일하다")