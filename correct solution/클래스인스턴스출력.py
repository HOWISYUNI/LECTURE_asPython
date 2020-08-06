# 클래스 인스턴스 출력하기 - class의 자동 string casting
# 문자열화 __str__() 함수를 이용한다

class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        """문자열화 함수
        print()에 인스턴스를 전달하면 자동으로 __str__()함수를 호출한다"""
        return f'({self.x}, {self.y})'

point = Coord(1, 2) # Instance 초기화
print(point)