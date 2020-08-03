# 순열과 조합
# 문제 설명
# 숫자를 담은 일차원 리스트, mylist에 대해 mylist의 원소로 이루어진 모든 순열을 사전순으로 리턴하는 함수 solution을 완성해주세요.

# 제한 조건
# mylist 의 길이는 1 이상 100 이하인 자연수입니다.
# 예시
# mylist	output
# [2, 1]	[[1, 2], [2, 1]]
# [1, 2, 3]	[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

import itertools

pool = [1,2,3]
print(list(itertools.permutations(pool)))
print(list(itertools.permutations(pool,2)))

char_pool = ['a','b','c']
print(list(map(''.join,itertools.permutations(char_pool))))