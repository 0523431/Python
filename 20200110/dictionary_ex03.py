'''
Created on 2020. 1. 10.
@author: GDJ19

    <dictionary 예제>
'''
import operator

dic, list = {}, []

dic = {"Thomas":"토마스","Edward":"에드워드","Henry":"헨리","Gothen":"고든","James":"제임스"}

list = sorted(dic.items(), key=operator.itemgetter(0), reverse=True)
print(list)

list = sorted(dic.items(), key=operator.itemgetter(1))
print(list)