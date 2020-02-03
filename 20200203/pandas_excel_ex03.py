'''
Created on 2020. 2. 3.
@author: GDJ19

    <excel파일을 pandas로 읽기>
    - 컬럼 중 값이 '01/24/2013'과 '01/31/2013'인 행만 조회하여 pandas_output3.xls에 저장하기
'''

import pandas as pd

input_file = "sales_2013.xlsx"
output_file = "pandas_output3.xls"

# 읽을거야(파일명,sheet명,???)
# 즉, sales_2013.xlsx 파일의 january_2013 sheet의 모든 내용
data_frame = pd.read_excel(input_file, "january_2013", index_col=None)
select_date = ['01/24/2013', '01/31/2013']

# isin() : 함수
# 즉, 괄호의 값에 속한 값인 경우에만 선택
# data_frame_value : select_date 날짜에 해당하는 모든 데이터
data_frame_value = data_frame[data_frame['Purchase Date'].isin(select_date)]

writer = pd.ExcelWriter(output_file)
data_frame_value.to_excel(writer, sheet_name="jan_13_output",index=False)
# 이 부분에서 파일로 생성 됨
writer.save()