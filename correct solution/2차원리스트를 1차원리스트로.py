# 2차원 리스트를 1차원 리스트로 만들기
# 문제 설명
# 문자열을 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist를 일차원 리스트로 만들어 리턴하도록 코드를 작성해주세요.

# 제한 조건
# arr의 길이는 1 이상 100 이하인 자연수입니다.
# arr 원소의 길이는 5를 넘지 않습니다.
# 예시
# input	output
# [[1], [2]]	[1, 2]
# [['A', 'B'], ['X', 'Y'], ['1']]	['A', 'B', 'X' ,'Y', '1']

mylist = [['A', 'B'], ['X', 'Y'], ['1']]

# SOLUTION 1
def solution(mylist):
    answer = []
    for iter in mylist:
        answer += iter
    return answer

print(solution(mylist))