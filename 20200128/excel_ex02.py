'''
Created on 2020. 1. 28.
@author: GDJ19

    <xlsx 파일 모두 읽기2>
    - excel_ex01은 sheet를 1개만 가져와서 읽어서 출력
'''

import openpyxl

filename = "sales_2015.xlsx"
book = openpyxl.load_workbook(filename)

for sheet in book.worksheets : # 모든 sheet
    data = []
    for row in sheet.rows :
        line = []
        for l, d in enumerate(row) : # l : cell, 열 값 / d : data value
            line.append(d.value) # 한줄의 셀의 값들을 list로 저장
        print(line)
        data.append(line)
    print(data)

    for i, a in enumerate(data) : # i :index / a :값
        if(i >=10) :
            break;
        print(i+1, a)
        
'''
    <enumerate>
    - 리스트에서 데이터와 index 값을 제공
    - index와 값을 동시에 알 수 있음
'''