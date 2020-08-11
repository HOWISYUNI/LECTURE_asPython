# 2차원 리스트 뒤집기
# 문제 설명
# 다음을 만족하는 함수, solution을 완성해주세요.

# solution 함수는 이차원 리스트, mylist를 인자로 받습니다
# solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
# 예를 들어 mylist [ [1,2,3], [4,5,6], [7,8,9] ]가 주어진 경우, solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.

# 제한 조건
# mylist의 원소의 길이는 모두 같습니다.
# mylist의 길이는 mylist[0]의 길이와 같습니다.
# 각 리스트의 길이는 100 이하인 자연수입니다.


mylist = [ [1,2,3], [4,5,6], [7,8,9] ]

# zip(*iterables) :  각 iterables의 요소(element)들을 모으는 tuple(튜플) iterator(반복자)를 만들어 리턴한다.
# '*iterables'은 여러개의 iterable(반복가능객체)로 생각할것. zip(list1, list2, list3)와 같이 unpacking이 아니라 여러개 리스트를 전달하기도한다.
new_list = list(map(list,zip(*mylist)))
# *mylist의 결과  [1,2,3], [4,5,6], [7,8,9]  가 리턴된다
# zip함수를 씌우면 ((1,4,7), (2,5,8), (3,6,9)) 튜플 iterator가 리턴된다. zip()함수는 tuple을 리턴한다.
# map 함수를 이용해 각 튜플에 list함수를 적용시킨다. [[1,4,7], [2,5,8], [3,6,9]]의 iterator들이 리턴된다. map()함수는 list를 리턴한다.
# list함수로 iterator들을 list로 만든다. [[1,4,7], [2,5,8], [3,6,9]]
