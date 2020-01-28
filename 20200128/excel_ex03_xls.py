'''
Created on 2020. 1. 28.
@author: GDJ19

    <xls 파일 읽기>
    - xlsx와 읽는 방법이 아예 다름
    - cmd > pip install xlrd
'''

# xlrd : xls파일 읽기
from xlrd import open_workbook

input_file = "ssec1804.xls"
workbook = open_workbook(input_file) # xlrd에서 가져온 open_workbook 함수

print("worksheets의 개수 : ", workbook.nsheets)
for worksheet in workbook.sheets() :
    print("worksheet 이름 : ", worksheet.name, "\n행수 : ", worksheet.nrows, "\n컬럼수 : ", worksheet.ncols)