import copy

my_list = [1,2,3]

def solution(mylist):
    answer = []
    idx = 0

    while idx<len(mylist):
        # pre processing
        copied_list = copy.deepcopy(mylist)
        insert_element = copied_list[idx]
        del(copied_list[idx])

        for i in range(len(copied_list)+1):
            temp = copy.deepcopy(copied_list)
            temp.insert(i,insert_element)
            if temp in answer:
                continue
            else:
                answer.append(temp)

        idx += 1

    return  answer

print(solution(my_list))