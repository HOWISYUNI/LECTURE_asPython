# 문제 설명
# base 진법으로 표기된 숫자를 10진법 숫자 출력해보세요.

# 입력 설명
# 입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
# 첫 번째 숫자는 num을 나타내며, 두 번째 숫자는 base를 나타냅니다.

# 출력 설명
# base 진법으로 표기된 num을 10진법 숫자로 출력해보세요.

# 제한 조건
# base는 10 이하인 자연수입니다.
# num은 3000 이하인 자연수입니다.
# 예시
# input	output
# 12 3	5
# 444 5	124

# -------------------------------------------------------------------------------
# TODO
# int(num, base) 함수는 base(항상 int형)가 주어졌을 때 num으로 stirng, byte, bytearray형식을 받아야한다.

# SOLUTION 1
num, base = map(int, input().strip().split(' ')) #  -> num과 base 모두 int 형으로 변환된다.
answer = int(str(num), base)
print('[sol1]answer : '+str(answer)) # string 두개를 묶기 위해 answer를 str로 캐스팅

# SOLUTION 2
num, base = input().strip().split(' ') # string 형 num과 base생성
answer = int(num, int(base))
print('[sol2]answer : '+str(answer)) # string 두개를 묶기 위해 answer를 str로 캐스팅