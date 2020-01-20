'''
Created on 2020. 1. 20.
@author: GDJ19

    <정규식>
    - 정규화 모듈 사용하기
    
    <정규식 표현법>
    - () : 그룹화
    - [] : 문자
    - {n} : 문자의 개수 (n개)
    - \d : 숫자
    - \g<1> : 첫번째 그룹
    - ? : 0 또는 1개
        "ca?t" : a문자가 없거나 1개인 경우 True
            "ct" : True
            "cat" : True
            "caat" : False
    - * : 0개이상
        "ca*t" : a문자가 없거나 여러개인 경우 True
            "ct" : True
            "cat" : True
            "caaaaaaaat" : True
    - + : 1개 이상
        "ca+t" : a문자가 1개이거나 여러개인 경우 True
            "ct" : False
            "cat" : True
            "caaaaaaaat" : True
    - {n} : n개
        "ca{2}t" : a문자가 2개인 경우 True
            "ct" : False
            "cat" : False
            "caat" : True
    - {n,m} : n개 이상 m개 이하
        "ca{2,5}t" : a문자가 2개인 경우 True
            "ct" : False
            "cat" : False
            "caat" : True
            "caaaaat" : True
            "caaaaaaaaaaaaaat" : False
    - + : 1개 이상
        "ca+t" : a문자가 1개이거나 여러개인 경우 True
            "ct" : False
            "cat" : True
            "caaaaaaaat" : True
    

    
    <해석>
    "(\d{6})[-]\d{7}"
    --> 첫번째 그룹 : 숫자 6자리
    --> 다음 문자 : -
    --> 다음 문자 : 숫자 7자리
'''

# 정규식 사용을 위한 모듈
import re

data = '''
    park 800905-1234567
    kim 700905-1234567
    choi 850101-a123456
'''

# 패턴 지정 pattern
pat = re.compile("(\d{6})[-]\d{7}")

# data문자열을 출력하는데,
# pattern에 맞는 문자열은 compile해서 출력해 
print(pat.sub("\g<1>-*******", data))
