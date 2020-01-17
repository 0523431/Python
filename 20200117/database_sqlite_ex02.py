'''
Created on 2020. 1. 17.
@author: GDJ19

    <화면에서 내용을 입력받아 sqlite db에 내용 저장하기>
'''
import sqlite3

dbpath = "usertable.sqlite"
con = sqlite3.connect(dbpath)
cur = con.cursor() # cursor : sql구문을 전달하는 객체 (java에서 statement 기능)
cur.executescript('''
    drop table if exists usertable;
    
    create table usertable (
         user_id varchar(15) primary key,
         name text,
         email varchar(30) unique,
         byear integer
    );
''')

while True :
    data1 = input("사용자 ID를 입력하세요 : ")
    if data1 == "" :
        break
    data2 = input("사용자 이름을 입력하세요 : ")
    data3 = input("사용자 email을 입력하세요 : ")
    data4 = input("사용자 birth_year을 입력하세요 : ")
    
    sql = "insert into usertable (user_id, name, email, byear) values ('"+data1+"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)
    con.commit()
    
# 등록된 내용을 select로 조회하기
cur = con.cursor()
cur.execute("select * from usertable")
user_list = cur.fetchall() # 모든 레코드 리턴
print(type(user_list))
for user in user_list :
    print(user)
con.close()