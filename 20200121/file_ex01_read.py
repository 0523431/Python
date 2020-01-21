'''
Created on 2020. 1. 21.
@author: GDJ19

    <파일 읽기>
    - open(파일이름, 파일모드, 인코딩방식)
    - 파일이름 : 경로가 중요
    - 파일모드 :
            "r" 읽기모드
            "w" 쓰기모드, 파일이 존재하지 않으면 생성
            "r+" 읽기/쓰기 겸용
            "a" 쓰기모드 append, 파일이 존재하지 않으면 생성, 존재하는 경우는 기존 내용 이후에 추가
            "t" 텍스트 모드, 기본형
            "b" 이진 모드, binary
    - 인코딩 방식 : 생략가능 (2바이트 한글의 경우 UTF-8로 인코딩)
'''

infp =None
inStr =""
infp = open("../20200120/regular_ex03.py", "rt", encoding="UTF-8") # rt : read text
while True :
    inStr =infp.readline() # 한줄씩 읽겠어
    if inStr ==None : # EOF(End of File) 상태 (java:null / python:none)
        break
    print(inStr, end="") # 한줄씩 읽은 inStr 출력
infp.close()