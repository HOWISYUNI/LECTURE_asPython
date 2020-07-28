# 문제 설명
# 문자열 리스트 mylist를 입력받아, 이 리스트를 정수형 리스트로 바꾼 값을 리턴하는 함수, solution을 만들어주세요. 예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 [1, 100, 33] 을 리턴하면 됩니다.

# 제한조건
# mylist의 길이는 100 이하인 자연수입니다.
# mylist의 원소는 10진수 숫자로 표현할 수 있는 문자열입니다. 즉, 'as2' 와 같은 문자열은 들어있지 않습니다.
# 예시
# input	output
# ['1', '100', '33']	[1, 100, 33]

list1 = ['1', '100', '33']

# map(function, iterable, ...) : iterable의 모든 항목에 function을 적용해 iterator를 리턴한다.
list2 = list(map(int, list1))
print(list2)
