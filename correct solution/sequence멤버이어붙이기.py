# sequence 멤버를 하나로 이어붙이기
# 문제 설명
# 문자열 리스트 mylist를 입력받아, 이 리스트의 원소를 모두 이어붙인 문자열을 리턴하는 함수, solution을 만들어주세요. 예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 '110033'을 리턴하면 됩니다.

# 제한 조건
# mylist의 길이는 100 이하인 자연수입니다.
# mylist의 원소의 길이는 100 이하인 자연수입니다.

my_list = ['1', '100', '33']

# str.join(iterable) : 문자열들을 이어붙인 문자열을 리턴한다. iterable은 bytes 객체나 기타 문자열만 가능하다.
answer = ''.join(my_list)
print(answer)