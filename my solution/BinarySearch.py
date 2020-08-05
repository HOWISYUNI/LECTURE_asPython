
# binary search는 항상 정렬돼야한다.
my_list =  [1, 2, 3, 7, 9, 11, 33]
lookfor = 4

def bi_search(mylist, target):
    mid = len(mylist)//2
    if mid == 0:
        if mylist[mid] == target:
            return mid
        return -1

    elif target<=mylist[mid]:
        if target == mylist[mid]:
            return mid
        target_idx = bi_search(mylist[:mid],target)

    elif mylist[mid] < target:
        target_idx = bi_search(mylist[mid:],target)

    return target_idx

print(bi_search(my_list,lookfor))