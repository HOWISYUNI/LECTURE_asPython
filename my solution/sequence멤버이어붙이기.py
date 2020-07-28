

def solution(mylist):
    answer = ''

    for string in mylist:
        answer = answer+string
    return answer

mylist = ['1', '100', '33'] 
print(solution(mylist))