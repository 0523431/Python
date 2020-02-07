'''
Created on 2020. 2. 7.
@author: GDJ19
    
    <crawling>
    - 크롤링 : java의 jsoup과 비슷함
    - pip install beautifulsoup4
'''

from bs4 import BeautifulSoup

html = '''
    <html>
        <body>
            <div id="potal">
                <h1>포털목록</h1>
                <ul class="items">
                    <li><a href="http://www.naver.com">naver</a></li>
                    <li><a href="http://www.daum.net">daum</a></li>
                </ul>
            </div>
        </body>
    </html>
'''

soup = BeautifulSoup(html, "html.parser") # html을 파싱해(해석)
print(type(soup)) # class 'bs4.BeautifulSoup'

links = soup.find_all("a") # find_all : a태그 전부를 가져와
for a in links :
    href = a.attrs["href"] # 속성 값을 가져옴
    text = a.string # 문자열 값
    print(text, ">", href)

h1 = soup.select_one("div#potal > h1").string # select_one : div태그 밑에 id가 potal이고 h1태그인 값 한개만 가져와
print("h1 =", h1)

li_list = soup.select("div#potal > ul.items > li") # select
for li in li_list :
    print("li =", li.string)
    
    
    
    