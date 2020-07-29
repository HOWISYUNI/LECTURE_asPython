
mylist = [[1],[2]]
# answer = mylist[0]
# print(answer)

def solution(mylist):
    answer = list()
    for iterable in mylist:
        for idx in range(len(iterable)):
            answer.append(iterable[idx])
    return answer

print(solution(mylist))