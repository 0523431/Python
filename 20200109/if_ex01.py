'''
Created on 2020. 1. 9.
@author: GDJ19

    <if구문 연습>
'''

score = int(input("학점을 입력하세요 : "))
if score >=90 :
    print("A학점")
else :
    if score >=80 :
        print("B학점")
    else :
        if score >=70 :
            print("C학점")
        else :
            if score >= 60 :
                print("D학점")
            else :
                print("F학점")
                
# java식 if else
print("if elif 구문 연습")
if score >=90 :
    print("A학점")
elif score >=80 :
    print("B학점")
elif score >=70 :
    print("C학점")
elif score >=60 :
    print("D학점")
else :
    print("F학점")