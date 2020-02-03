'''
Created on 2020. 2. 3.
@author: GDJ19

    <excel파일을 pandas로 읽기>
    - 폴더 안에 있는 모든 excel파일 읽기
'''

import pandas
import glob # glob : "*.xls*"와 같이 *를 사용할 수 있게 해주는 모듈 (경로명 표현시 사용되는 모듈)
import os # system을 관리해주는 모듈 / file의 위치를 가져올 수 있음

# 읽고자하는 excel파일이 있는 폴더의 절대 경로
inputPath = "D:/20190901_P/python/pythonTest/Excel/"
outputFile = "pandas_output8.xls"

# inputPath, "*.xls*" : inputPath 폴더의 몯느 xlsx 또는 xls 파일
# all_workbooks : inputPath 폴더의 모든 excel파일을 저장
all_workbooks = glob.glob(os.path.join(inputPath, "*.xls*"))

data_frames = []

for workbook in all_workbooks :
    print("workbook 한개의 엑셀 파일 ===>", workbook, "를 읽어서")
    all_worksheets = pandas.read_excel(workbook, sheet_name=None, index_col=None)
    
    for worksheet_name, data in all_worksheets.items() :
        print("worksheet_name ===>",worksheet_name)
        data_frames.append(data)
        
# all_data_concat : 모든 엑셀파일의 data를 저장
# axit=0 : row로 붙여서 출력
all_data_concat = pandas.concat(data_frames, sort=False, axis=0, ignore_index=True)

writer = pandas.ExcelWriter(outputFile)
all_data_concat.to_excel(writer, sheet_name="all_data_all_worksheet", index=False)

writer.save()