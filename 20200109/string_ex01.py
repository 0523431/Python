'''
Created on 2020. 1. 9.
@author: GDJ19

    <문자열 처리하기>
    - python에서 문자열은 배열로 처리할 수 있음
'''
print("문자열 출력하기 -배열처리 가능-")
print("안녕하세요")
print("안녕하세요"[0]) # 0번인덱스의 문자열 출력 : 안
print("안녕하세요"[4]) # 4번인덱스의 문자열 출력 : 요
print("안녕하세요"[-1]) # 뒤에서 첫번째 문자열 출력 : 요
print("안녕하세요"[-3]) # 뒤에서 세번째 문자열 출력 : 하
print()

print("부분문자열 출력하기")
print("안녕하세요"[1:3]) # 1번인덱스부터 2번인덱스까지 출력 : 녕하
print("안녕하세요"[:3]) # 0번 인덱스부터 2번 인덱스까지 출력 : 안녕
print("안녕하세요"[3:]) # 3번인덱스부터 끝까지 출력 : 세요
print("안녕하세요"[::2]) # 앞부터 2칸씩 건너서 출력: 안하요
print("일이삼사오육칠팔구십"[::3]) # 앞부터 3칸씩 건너서 출력: 일사칠십
print("안녕하세요"[::-1]) # 역순으로 출력 : 요세하녕안
print("안녕하세요"[::-2]) # 역순으로 2칸씩 건너서 출력 : 요하안
print()

print("안녕하세요의 자료형 :", type("안녕하세요"))
print("'안녕하세요'의 문자열 길이 :", len("안녕하세요"))
print("len의 자료형 :",type(len("안녕하세요")))
print()

a = "hellohello"
cnt =0
for i in range(0, len(a)) :
    if a[i].__eq__("l") :
        cnt +=1
print("l 문자의 개수 =", cnt)

cnt =0
for i in range(0, len(a)) :
    if(a[i] == "l") :
        cnt +=1
print("l 문자의 개수 =", cnt)
print()

print("l 문자의 개수 =", a.count("l"))
print("h 문자의 개수 =", a.count("h"))
print("i 문자의 개수 =", a.count("i"))
print()

print("l 문자의 위치 =", a.find("l"))
print("i 문자의 우치 =", a.find("i")) # 없을 경우 : -1 출력
print()

print("l 문자의 위치 =", a.index("l"))
print("i 문자의 위치 =", a.index("i")) # 없을 경우 : error