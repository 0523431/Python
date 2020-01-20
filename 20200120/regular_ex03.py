'''
Created on 2020. 1. 20.
@author: GDJ19

    <정규식 예제>
'''

import re

string ="The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile("The")
count =0

for word in string_list :
    # word 중에 pattern이 있니?
    if pattern.search(word) :
        count +=1
print("output #1 : {0:d} ".format(count))
print("output #1 : {0:d} => {1:s} ".format(count,"개"))
print("output #1 : {1:s} => {0:d} ".format(count,"개"))
print()

# re.I : 대소문자 구분 x
# 대소문자 구문없이 the라는 문자는 match_word에 저장이 됨..?
pattern =re.compile("(?P<match_word>The)", re.I)
print("output #2 :")
for word in string_list :
    if pattern.search(word) :
        print("{0}".format(pattern.search(word).group("match_word")))

# 치환
# re.I : 대소문자 구분 x
# 대소문자 구분없이 the 문자열을 a 문자열로 치환
string_to_find =r"The"
pattern = re.compile(string_to_find, re.I)
print("output #3 : {0}".format(pattern.sub("a", string)))
print("")