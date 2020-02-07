'''
Created on 2020. 2. 7.
@author: GDJ19

    <네이버 환율 조회하기>
'''

from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser", from_encoding="EUC-KR")

hlist = soup.select("div.head_info")
htitle = soup.select("h3.h_lst")

for tag, title in zip(hlist, htitle) :
    print(title.select_one("span.blind").string, end="\t\t\t")
    value = tag.select_one("span.value").string
    print(value, end=" ")
    change = tag.select_one("span.change").string
    print(change, end="\t")
    
    blinds = tag.select("sapn.blind")
    b = tag.select("span.blind")[-1].string
    print(b, end="*******\n")