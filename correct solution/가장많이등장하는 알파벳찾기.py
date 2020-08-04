# 가장 많이 등장하는 알파벳 찾기
# 문제 설명
# 이 문제에는 표준 입력으로 문자열, mystr이 주어집니다. mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.

# 제한 조건
# mystr의 원소는 알파벳 소문자로만 주어집니다.
# mystr의 길이는 1 이상 100 이하입니다.
# 예시
# input	output
# 'aab'	'a'
# 'dfdefdgf'	'df'
# 'bbaa'

import collections

my_str = input().strip()
countered = collections.Counter(my_str) # Counter 클래스는 collections에 속하고, collections는 dictionary를 상속하므로 Counter는 dictionary의 operation을 사용할 수 있다.
print(countered)
print(countered.most_common()) # Counter.most_common() : (key, value) 튜플로 이루어진 리스트를 반환
print(countered.most_common(2)) # 숫자 인자를 넘겨주면 (key,value)리스트중 앞에서 인자갯수만큼 반환함.

frequent_letter = countered.most_common(1)
answer = []

for key, value in countered.items():
    if value == frequent_letter[0][1]:
        answer.append(key)

for letter in sorted(answer):
    print(letter,end='')# end : print() 끝난 후 입력할 문자, sep은 string여러개가 하나의 print()로 출력될때 string사이 구분문자 지정

# for lettter in frequent_letter:
#     print(lettter)

# for key in frequent_letter.keys():
#     print(key)

# for key, value in frequent_letter.items():
#     print(key, value)

# for item in frequent_letter.items():
#     print(item)