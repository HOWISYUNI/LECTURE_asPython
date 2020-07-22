def solution(mylist):
    answer = list()
    for row in mylist:
        answer.append(len(row))
    
    return answer

input_val = [[1], [2]]
# input_val = [[1, 2], [3, 4], [5]]
print(solution(input_val))