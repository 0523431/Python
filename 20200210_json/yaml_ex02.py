'''
Created on 2020. 2. 10.
@author: GDJ19

    <yaml>
    - yaml 문서에서 alias, 주석 설정하기
    - json에서는 안되는 기능
'''

import yaml

yaml_str = '''

# <주석 부분 : 결과에 영향을 미치지 않음 (json과 다른 점)
# 정의
color_def :
    - &color1 "#FF0000"
    - &color2 "#00FF00"
    - &color3 "#0000FF"

# 별칭 정하기
color :
    title : *color1
    body : *color2
    link : *color3
    div : *color1
'''

data = yaml.load(yaml_str, Loader=yaml.FullLoader)
print("title=", data["color"]["title"])
print("body=", data["color"]["body"])
print("link=", data["color"]["link"])
print("div=", data["color"]["div"])
