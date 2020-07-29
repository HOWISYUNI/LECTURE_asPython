# 곱집합(Cartesian product) 구하기 - product
# 이번 강의에서는 iterable으로 곱집합을 구하는 방법을 알아봅니다.

# 예시) 두 스트링 'ABCD', 'xy' 의 곱집합은 Ax Ay Bx By Cx Cy Dx Dy 입니다.


import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

cartesian = itertools.product(iterable1,iterable2,iterable3)
print([''.join(i) for i in cartesian])
# print(*cartesian)
# print(tuple(cartesian))

