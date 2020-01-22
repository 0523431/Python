'''
Created on 2020. 1. 22.
@author: GDJ19
    
    <xlsx 파일 읽기>
    
    <엑셀 파일의 종류>
    - xlsx : 신버전(xml파일을 내부적으로 포함하고 있음) | pip install openpyxl
    - xls : 구버전(2진파일) | pip install xlrd
'''

import openpyxl

filename = "sales_2015.xlsx"

book = openpyxl.load_workbook(filename)
sheet = book.worksheets[0] # 첫번째 sheet
data =[]

# 한번에 읽어냄 sheet.rows
for row in sheet.rows :
    line =[]
    for l, d in enumerate(row) : # l : cell, 열 값 / d : data value
        line.append(d.value) # 한 줄의 cell 값들을 list로 저장
#         print(l, end="\t")
    print(line)
    data.append(line)
print(type(data))
print(data) # 리스트의 리스트

print("============================== 리스트 data를 보기좋게 다시 출력해보자")
for index, data_value in enumerate(data) :
    if(index >=5) :
        break;
    print(index +1, data_value)

'''
    <enumerate>
    - 리스트에서 데이터와 index 값을 제공
    - index와 값을 동시에 알 수 있음
'''