'''
Created on 2020. 1. 9.
@author: GDJ19

    <연산자 연습>
'''

num1 = int(input('첫번째 점수 입력 : '))
num2 = int(input('두번째 점수 입력 : '))

print(num1,"+",num2,"=",(num1+num2))
print(num1,"-",num2,"=",(num1-num2))
print(num1,"*",num2,"=",(num1*num2))
print(num1,"/",num2,"=",(num1/num2)) # java : 정수 몫 / python : 몫 전체
print(num1,"/",num2,"=",(num1//num2)) # 정수 몫
print(num1,"%",num2,"=",(num1%num2))
print(num1,"제곱",num2,"=",(num1**num2)) # 제곱

print("a"+"b"+"c") #abc
print("abc" *3) #abcabcabc

print("안녕하세요 길고 긴말 어쩌구 저쩌구(1)"
      + "안녕하세요 길고 긴말 어쩌구 저쩌구(2)"
      + "안녕하세요 길고 긴말 어쩌구 저쩌구(3) 한줄로 출력됨") # 한줄로 출력

print("""안녕하세요 길고 긴말 어쩌구 저쩌구(1)
                안녕하세요 길고 긴말 어쩌구 저쩌구 따옴표 세개를 쓰면 이렇게 출력됨(2)""")

print('''안녕하세요 길고 긴말 어쩌구 저쩌구 (1)
안녕하세요 길고 긴말 어쩌구 저쩌구 따옴표 세개를 쓰면 이렇게 출력됨(2)''')