'''
Created on 2020. 1. 10.
@author: GDJ19
'''

ss = "홍길동"

# 문제
# > 홍#길#동# 으로 출력하기
print(ss)
print(list(ss))

for i in range(0, len(ss)) :
    print(ss[i], end="#")
print()

# 역순으로 출력하기
# 방법 1
for i in range(len(ss)-1, -1, -1) :
    print(ss[i], end="")
print()
# 방법 2
print(ss[::-1])

# ss문자열의 시작과 끝이 ()괄호가 아니면 ()괄호 추가해서 출력하기
# > (홍길동) 으로 출력하기
if ss.startswith("(") == False :
    print("(", end="")
print(ss, end="")
if ss.endswith(")") == False :
    print(")")
print()
    
# split() 함수
ss = "2020/01/10"
print("날짜 ss의 10년전 출력하기")
list = ss.split("/")
print(list)
print(int(list[0])-10, "년", list[1], "월", list[2], "일")