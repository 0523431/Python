'''
Created on 2020. 1. 15.
@author: GDJ19

    <lotto 로또 번호 생성기>
'''

import random

def getNumber() :
    return random.randrange(1, 46)

# 자료형 dictionary
lotto = {}
print(type(lotto))

# lotto[]를 쓴 식은 dict인 경우에만 가능함
for num in range (1, 7) :
    lotto[num] = getNumber()

# set으로 만들어주려면
lotto = set()
print(type(lotto))

while len(lotto) <6 :
    lotto.add(getNumber())
    # 함수를 쓰지않으려면
    # lotto.add(random.randrange(1, 46))

print("추첨된 로또 번호 =>", sorted(lotto))
