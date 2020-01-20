'''
Created on 2020. 1. 20.
@author: GDJ19

    <mariaDB 사용하기>
        - cmd에서 아래 내용을 실행 (리눅스에서 apt-get update와 동일한 방법)
        - python -m pip install --upgrade pip
        - pip install pymysql

'''

import pymysql
conn = pymysql.connect(host="localhost", port=3306, user="scott", passwd="1234", db="classdb", charset="utf8")

try :
    # cursor : sql구문을 전달해주는 객체
    # sql구문을 실행한 결과를 cur객체가 가지고 있는거고
    # 그 결과 1건을 조회하는게 cur.fetchone()
    cur = conn.cursor()
    cur.execute("select * from item")
    
    # 실행 결과를 출력하는 방법 1
#     while True :
#         row = cur.fetchone() # 1건의 레코드
#         if row ==None :
#             break
#         print(row) # 1건의 레코드를 출력
    
    # 실행 결과를 출력하는 방법 2
    for row in cur.fetchall() :
        print(type(row), row) # type : tupel(변경불가 리스트)
        print(row[0],row[1],row[2]) # 특정 컬럼만 지정해서 출력가능
        print()
    
finally :
    cur.close()
    conn.close()