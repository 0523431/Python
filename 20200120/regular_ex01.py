'''
Created on 2020. 1. 20.
@author: GDJ19

    <정규식 예제>
    - 정규화 모듈 사용 안함
'''

data = '''
    park 800905-1234567
    kim 700905-1234567
    choi 850101-a123456
'''

result =[]
for line in data.split("\n") :
    # line : park 800905-1234567
    word_result =[]
    for word in line.split(" ") :
        # word : park
        # word : 800905-1234567
        
        # 첫번째 word : park은 14자리가 아니니까
        # => word_result : [park]
        # 두번째 word : 800905-1234567은 14자리니까 if 조건에 맞고, isdigit() => 숫자인 경우 True
        # => word_resuel : [park, park 800905-*******]
        if len(word) ==14 and word[:6].isdigit() and word[7:].isdigit():
            word =word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result)) # 공백을 기준으로 append한게 result가 됨
print("\n".join(result))
