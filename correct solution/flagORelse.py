
# 문제 설명
# 본 문제에서는 자연수 5개가 주어집니다.

# 숫자를 차례로 곱해 나온 수가 제곱수1가 되면 found를 출력하고
# 모든 수를 곱해도 제곱수가 나오지 않았다면 not found를 출력하는
# 코드를 작성해주세요.

import math

input_value = [int(input()) for _ in range(5)] 
# 입력값을 바로 리스트로 만든다 -> 리스트 표현식
# 단순히 5회 반복만을 위한 for문이므로 for 키워드 다음에 아무 문자나 넣어준다. 공백은 안된다.

#1 FLAG
flag = True
multiplied = 1

for value in input_value:
    multiplied *= value
    if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
        flag = False
        print('found')
        break

if flag:
    print('Not found')

#2 for-else
multiplied = 1
for value in input_value:
    multiplied *= value
    if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
        print('found')
        break
else: # for문이 break로 끝나는 경우에만 else문을 통과한다.
    print('Not found')