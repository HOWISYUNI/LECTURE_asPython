
# binary search는 항상 정렬돼야한다.
# binary search종결조건
#     1. 중간에 찾는다
#         찾은 위치를 리턴한다.
#     2. first와 last가 1칸 차이일때
#         찾았다 -> 찾은 위치를 리턴
#         못찾았다 -> -1을 리턴
my_list =  [1, 2, 3, 7, 9, 11, 33]
lookfor = 8

"""
일반적인 binary search
    1. 값을 찾았다 -> 찾은 위치 리턴
        1.1 [중간]에 찾았다
        1.2 [first와 last가 1칸 차이]에서 찾았다.
    2. 찾지 못했다
        -> -1을 리턴
"""

# 1 나무위키
def binary_search (arr, val):
    first, last = 0, len(arr)
    while first<=last:
        mid = (first + last) // 2
        if arr[mid] == val: return mid
        if arr[mid] > val: last = mid-1
        else: first = mid+1
    return -1

print(binary_search(my_list,lookfor))

"""
python에서 binary search는 2가지 결과를 보장한다.
    1. 값을 찾았다면
        -> 찾은 위치의 인덱스를 리턴
    2. 값을 찾지 못했다면
        -> 들어가야할 위치 인덱스를 리턴
"""

# 2-1 programmers
def bisect(a, x, lo=0, hi=None): # 기본값 설정. 함수 호출시 lo나 hi에 값을 전달하지 않는다면 lo=0, hi=None이 매개변수에 저장된다.
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

print(bisect(my_list, lookfor))

#2-2 programmers
import bisect
print(bisect.bisect(my_list, lookfor))