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
answer = collections.Counter(my_str)
print(answer)
