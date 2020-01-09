'''
Created on 2020. 1. 9.
@author: GDJ19

    <초를 입력받아서 몇시간 몇분 몇초인지 출력하기>
'''

sec = int(input("초를 입력하세요 : "))

print(sec//3600, "시간 ", (sec%3600)//60, "분", sec%60, "초초")
