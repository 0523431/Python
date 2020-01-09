'''
Created on 2020. 1. 9.
@author: GDJ19

    <랜덤함수를 사용하여 숫자 맞추기>
    - 1부터 99까지의 임의의수를 저장하고 화면에 숫자를 입력받아 그 숫자 맞추기
    - 정답인 경우, 입력 건수를 출력하고 프로그램 종료
'''
import random
answer = random.randrange(1, 100) # 1부터 99까지의 임의의 수

cnt =0
'''
<boolean 예약어>
    - True
    - False
'''
while True :
    inputNum = int(input("숫자를 입력하세요 : "))
    if inputNum > answer :
        print("정답은 더 작은 수 입니다")
    elif inputNum < answer :
        print("정답은 더 큰 수 입니다")
    else : # elif inputNum == answer :
        print("정답입니다")
        break
    cnt = cnt +1

print("%d번만에 맞췄습니다 ^_^" % cnt)
