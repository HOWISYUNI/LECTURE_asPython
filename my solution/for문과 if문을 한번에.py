def solution(mylist):
    answer = []
    for element in mylist:
        if element%2 != 0:
            continue
        answer.append(element**2)
    return answer

mylist = [3, 2, 6, 7]
print(solution(mylist))