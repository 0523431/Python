'''
Created on 2020. 1. 13.
@author: GDJ19

'''
import operator

dicTest = {}

while True :
       
    if len(dicTest) ==0 :
        print("2 등록, 3 수정, 4 삭제, 9 종료")
        menu = input("번호를 입력하세요 => ")
        if menu !="2" :
            print("번호가 틀립니다")
        elif menu =="2" :
            eng = input("등록할 영어 단어 => ")
            if eng in dicTest :
                print("이미 등록된 단어 입니다")
            else :
                dicTest[eng] = input("등록할 한글 단어 => ")
                print("등록되었습니다")
                print()
    else :
        print("1 조회, 2 등록, 3 수정, 4 삭제, 9 종료")
        menu = input("번호를 입력하세요 => ")
        
        if menu =="1" : # 조회
            print("=====================등록된 단어 개수 : ", len(dicTest))
            
            sort = input("정렬기준(1 영문, 2 한글, 그 외 입력순서) => ")
            if sort =="1" :
                print("========== 사전 내용(영문기준) ==========")
                sortEng = sorted(dicTest.items(), key=operator.itemgetter(0))
                
                dicEng = dict(sortEng)
                for i in dicEng.keys() :
                    print("%s = %s" % (i, dicEng[i]))
                          
            elif sort =="2" :
                print("========== 사전 내용(한글기준) ==========")
                sortKor = sorted(dicTest.items(), key=operator.itemgetter(1))
                
                dicKor = dict(sortKor)
                for i in dicKor.keys() :
                    print("%s = %s" % (i, dicKor[i]))
                
            else :
                print("========== 사전내용 ==========")
                for i in dicTest.keys() :
                    print("%s = %s" % (i, dicTest[i]))
        
        elif menu =="2" : # 등록
            eng = input("등록할 영어 단어 => ")
            if eng in dicTest :
                print("이미 등록된 단어 입니다")
            else :
                dicTest[eng] = input("등록할 한글 단어 => ")
                print("등록되었습니다")
                print()
            
        elif menu =="3" : # 수정
            engMod = input("수정할 영어 단어 => ")
            if engMod in dicTest :
                dicTest[engMod] = input("수정할 한글 단어 => ")
            else :
                print("등록된 단어가 아닙니다")
            
        elif menu =="4" : # 삭제
            engDel = input("삭제할 영어 단어 => ")
            if engDel in dicTest :
                del(dicTest[engDel])
            else :
                print("등록된 단어가 아닙니다")
                
        elif menu =="9" : # 종료
            print("프로그램 종료 감사합니다")
            break
        else :
            print("번호가 틀립니다")