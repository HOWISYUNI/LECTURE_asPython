
# binary search는 항상 정렬돼야한다.
my_list =  [1, 2, 3, 7, 9, 11, 33]
lookfor = 3

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

# 2-1 programmers
def bisect(a, x, lo=0, hi=None):
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
print(bisect.bisect(my_list, 3))