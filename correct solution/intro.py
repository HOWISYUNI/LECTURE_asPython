# 정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 코드를 작성해주세요.
# mylist의 길이는 100 이하인 자연수입니다.
# mylist 각 원소의 길이는 100 이하인 자연수입니다.
# input	output
# [[1], [2]]	[1,1]
# [[1, 2], [3, 4], [5]]	[2,2,1]


def solution(mylist):
    return list(map(len,mylist))

# input_val = [[1], [2]]
input_val = [[1, 2], [3, 4], [5]]
print(solution(input_val))