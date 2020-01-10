'''
Created on 2020. 1. 10.
@author: GDJ19

    <dictionary ==> {} == java : Map>
'''

singer = {}
singer['이름'] = '레드벨벳'
singer['구성원수'] = 5
singer['최신곡'] = 'psycho'
singer['소속사'] = 'SM town'
for i in singer.keys() : #range를 쓰지않고 사용 가능
    print("%s => %s" % (i, singer[i]))

print()
singer['소속사'] = '에스엠ent' # 키값이 있으면, 바로 수정이 가능함
print(singer)
print(singer.keys())
print(type(singer))
print(type(singer.keys()))
print(singer['최신곡'])