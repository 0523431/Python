'''
Created on 2020. 1. 9.
@author: GDJ19

    <for구문 예제 : 구구단 출력하기>
'''

i, j =0,0
for i in range(2, 10) :
    print("%5d단" % i)
    for j in range(1, 10) :
        print(i,"x",j,"=",(i*j))
    print()

for i in range (2, 10) :
    print("%6d단 %20s" % (i," "), end="")
print()
for j in range(1, 10) :
    for i in range(2, 10) :
        print("%2d x%2d =%3d   " % (i, j, (i*j)), end="")
    print()