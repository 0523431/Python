'''
Created on 2020. 2. 7.
@author: GDJ19

    <crawling>
    - 내가 만든 HTML 분석하기
'''

from bs4 import BeautifulSoup

fp = open("books.html", encoding="UTF-8")
soup = BeautifulSoup(fp, "html.parser")

# 람다식을 이용하여 출력하기
sel = lambda q : print(soup.select_one(q).string)

sel("#nu") # id="nu" 태그 정보 출력
sel("li#nu") # li 태그이면서 id="nu" 태그 정보 출력
sel("ul > li#nu") # ul태그의 하위 태그인 li태그의 id="nu"인 태그 출력

sel("#bible #nu") # id="bible"인 태그이 하위 태그의 id="nu"인 태그 정보 출력
sel("#bible > #nu") # id="bible"인 태그이 하위 태그 중 id="nu"인 태그 출력 | > : 바로 하위에 있는 태그
sel("ul#bible > li#nu") 

sel("li[id='nu']") # li 태그 중 id 속성의 값이 nu인 태그 정보 출력
sel("li:nth-of-type(4)") # li 태그 중 4번째인 태그 정보 출력

print()
# 기존 방식으로 출력하기
print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)




