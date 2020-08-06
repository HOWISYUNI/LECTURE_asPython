
# binary search는 항상 정렬돼있음을 가정한다.
my_list =  [1, 2, 3, 7, 9, 11, 33]
lookfor = 34

"""
일반적인 binary search
    1. 값을 찾았다 -> 찾은 위치 리턴
        1.1 [중간]에 찾았다
        1.2 [first와 last가 1칸 차이]에서 찾았다.
    2. 찾지 못했다
        -> -1을 리턴
"""
def bi_search_usual(mylist, target, lo=0, hi=None):
    # init
    if hi is None:
        hi = len(mylist)-1

    # return
    if hi-lo == 1:
        if target == mylist[hi]:
            return hi
        elif target == mylist[lo]:
            return lo
        else:
            return -1

    # find
    mid = (hi+lo)//2

    if target<=mylist[mid]:
        if target == mylist[mid]:
            return mid
        target_idx = bi_search_usual(mylist,target,hi=mid)

    elif mylist[mid] < target:
        target_idx = bi_search_usual(mylist,target,lo=mid,hi=hi)

    return target_idx


def bi_search_usual_refactoring(mylist, target, lo=0, hi=None):
    # init
    if hi is None:
        hi = len(mylist)-1

    mid = (lo+hi)//2
    if lo<hi:
        if target==mylist[mid]:return mid
        elif target < mylist[mid]:
            hi=mid-1
            lo = bi_search_usual_refactoring(mylist,target,hi=hi)
        else:
            lo=mid+1
            lo = bi_search_usual_refactoring(mylist,target,lo=lo)

    return lo


"""
python에서 값을 끼워넣을 위치를 찾을 용도로 binary search를 사용한다.
    1. 값을 찾았다면
        -> 찾은 위치의 인덱스를 리턴
    2. 값을 찾지 못했다면
        -> 들어가야할 위치 인덱스를 리턴
"""

def bi_search_py(mylist,target):
    first, last = 0, len(mylist)-1
    while first<last:
        mid = (first+last)//2
        if target == mylist[mid]: 
            return mid
        if target < mylist[mid]: 
            last = mid-1
        else: 
            first = mid+1
    return first

# 결과

''' 1. bi_search_usual() '''
answer = bi_search_usual(my_list,lookfor)
# f-string is best remedy for python string
if answer == -1: # is : 같은 object(객체)를 판단       == : 같은 value(값)를 판단
    print(f'cannot find [{lookfor}]')
else:
    print(f"'{lookfor}' is on [{answer}]")

'''2. bi_search_py()'''
print(bi_search_py(my_list,lookfor))

'''3. bi_search_usual_refactor()'''
print(bi_search_usual_refactoring(my_list,lookfor))