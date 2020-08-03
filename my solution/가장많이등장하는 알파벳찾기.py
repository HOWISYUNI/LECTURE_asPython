my_str = input().strip()
# 문자별 횟수 세기
string_dict = dict() # 문자마다 갯수파악하기 쉽게 딕셔너리에 저장
for char in my_str:
    if char in string_dict.keys():
        # 있으면 +1
        string_dict[char] += 1 # 딕셔너리는 sequence 객체가 아니므로 인덱스 자리에 키값을 넣어줘서 접근할 수 있다.
    else:
        # 없으면 추가
        string_dict.setdefault(char,1) # 딕셔너리의 기본값으로 1을 주고 추가

# 정렬
    # key값 지정에 
    # 1. 람다표현식
    # 2. operator 모듈 함수의 itemgetter(), attrgetter()사용 https://docs.python.org/ko/3/howto/sorting.html#operator-module-functions
alphabet_list = sorted(string_dict.items(),key = lambda value:value[1],reverse=True)

# 가장 많이 나온 문자 출력
result = []
for tup in alphabet_list:
    if tup[1] < alphabet_list[0][1]:
        break
    result.append(tup[0])

# sorted()함수를 사용해야 정렬된 리스트를 리턴해서 join함수에서 사용할 수 있다.
# list내장함수인 list.sort()는 list에만 사용한다.
# sorted()함수는 모든 iterable에 사용할 수 있다.
answer = ''.join(sorted(result)) 
print(answer)