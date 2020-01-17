'''
Created on 2020. 1. 17.
@author: GDJ19

    <클래스에서 사용되는 메서드>
'''

class Line :
    length =0
    
    # 생성자 클래스 객체 생성시 호출되는 메서드
    def __init__(self, length) :
        self.length =length
        print(self.length, "길이의 선이 생성되었습니다")
    
    # 소멸자
    # 객체 제거시 호출되는 메서드
    def __del__(self) :
        print(self.length, "길이의 선이 제거되었습니다")
        
    # 자바의 toString 기능 메서드 : 객체를 문자열화하는데 사용하는 메서드
    # 객체 출력시 호출되는 메서드
    def __repr__(self) :
        return "선의 길이 : " + str(self.length)
    
    # 객체의 더하기 연사자 사용시 호출되는 메서드
    def __add__(self, other) :
        print("더하기 연사자가 호출되었습니다")
        return self.length + other.length
    
    # 객체의 < 연산자 사용시 호출되는 메서드
    def __lt__(self, other) :
        print("< 연산자 호출")
        return self.length < other.length
    
    # 객체의 > 연사자 사용시 호출되는 메서드
    def __gt__(self, other) :
        print("> 연산자 호출")
        return self.length > other.length
    
    # 객체의 == 연산자 사용자 호출된느 메서드
    def __eq__(self, other) :
        print("== 연산자 호출")
        return self.length == other.length
    
myLine1 = Line(400)
myLine2 = Line(400)
print(myLine1)
print(myLine2)

# myLine1, myLine2는 객체인데 더하기가 가능해
# 왜? __add__(self, other)이 호출됨
print("두 선의 길이 합 : ", myLine1 + myLine2)

# 두 선의 길이 비교
if myLine1.length < myLine2.length :
    print(".length myLine2의 길이가 더 길다")
elif myLine1.length == myLine2.length :
    print(".length 두 선의 길이는 같다")
else :
    print(".length myLine1의 길이 더 길다")

# 두 선의 길이 비교 (객체를 비교)
print()
print("메서드 __lt/gt/eq__(self, other)")
if myLine1 < myLine2 : # <일때, __lt__()가 실행이 되니까 "< 연산자 호출"이 출력이 됨
    print("myLine2의 길이가 더 길다")
elif myLine1 == myLine2 :
    print("두 선의 길이는 같다")
else :
    print("myLine1의 길이 더 길다")
    
# 프로그램 종료 : 생성된 객체가 모두 소멸됨 => 소멸자 호출됨