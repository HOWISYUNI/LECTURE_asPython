import copy

answer = []
def solution(mylist, start, end):
    if start == end:
        copied_list = copy.deepcopy(mylist)
        return copied_list
    else :
        for idx in range(start,end+1):
            mylist[idx], mylist[start] = mylist[start], mylist[idx]
            temp = solution(mylist, start+1, end)
            if temp is not None:
                answer.append(temp)
            mylist[idx], mylist[start] = mylist[start], mylist[idx]


mylist = [1,2,3,4]
solution(mylist,0,len(mylist)-1)
print(answer)