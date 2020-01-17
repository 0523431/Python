'''
Created on 2020. 1. 17.
@author: GDJ19

    <sqlite db 사용하기>
    - python자체에 들어가있는 DB
    - lite 가벼운 버전
'''

import sqlite3

# 프로그램이 정상적으로 실행이 되면, db내용이 저장된 test.sqlite 파일이 생성됨
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)
cur = conn.cursor() # cursor : sql구문을 전달하는 객체 (java에서 statement 기능)
cur.executescript('''
    drop table if exists items;
    
    create table items (
         item_id integer primary key,
         name text unique,
         price integer
    );
    
    insert into items (name, price) values ('Apple', 800);
    insert into items (name, price) values ('Fig', 5000);
    insert into items (name, price) values ('Strawberry', 2500);
''') # ''' < 원래는 주석인데, 이 안에서는 다중문자열이 허용될 수 있게 만들어줌

conn.commit() # commit :transaction 종료

cur = conn.cursor()
cur.execute("select item_id, name, price from items")
# executescript : 다중 문자열
# execute : 단일 문자열

item_list = cur.fetchall() # 모든 레코드 리턴
print(type(item_list))
print(item_list)
for item in item_list :
    print(item)
