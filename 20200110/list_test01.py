'''
Created on 2020. 1. 10.
@author: GDJ19

    <리스트 문제>
    - aa, bb 배열을 생성
    - aa 배열은 0부터 짝수 100개를 저장
    - bb 배열은 aa배열의 역순으로 값을 저장
    -> aa[0]~aa[9], bb[99]~bb[90] 값을 출력
'''

aa = []
bb = []
even =0
for i in range(0,100) :
    aa.append(even)
    even +=2
print("list aa`s length :", len(aa))

for i in range(0,10) :
    print("aa[%2d] =%3d" % (i, aa[i]), end=", ")
print()

# 방법1
for i in range(len(aa)-1,-1,-1) :
    bb.append(aa[i])

# 방법 2
# for i in range(-1, -101, -1) :
#     bb.append(aa[i])

# 방법 3
# for i in range(0,100) :
#     bb.append(aa[99-i])

for i in range(len(bb)-1,89,-1) :
    print("bb[%2d] =%3d" % (i,bb[i]), end=", ")
