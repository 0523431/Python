'''
Created on 2020. 1. 20.
@author: GDJ19

    <mariaDB에 데이터 입력하기>
'''

import pymysql

conn = pymysql.connect(host="localhost", port=3306, user="scott", passwd="1234", db="classdb", charset="utf8")

cur = conn.cursor() # cursor : sql구문을 전달해주는 객체
# tuple형태의 list객체
# tuple이기때문에 (%s,%s,%s,%s)에서 각각의 컬럼을 읽을 수 있음
data = [(13,"바나나",3000,"바나나는 맛있다"),
        (14,"망고",30000,"망고는 열대과일 이다"),
        (15,"수박",15000,"수박은 여름에 최고다")]

for i in data :
    cur.execute(
        '''
        insert into item (id,name,price,description) values (%s,%s,%s,%s)
        ''', i
    )

# conn.commit()

cur.execute("select * from item")
for row in cur.fetchall() :
    print(row)
    
conn.rollback()
# transaction이 완료되지 않기 때문에 db에서 확인해도 13, 14, 15 아이템은 등록되지 않음