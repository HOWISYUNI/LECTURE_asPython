# 이중for문 사용

def solution(mylist):
    answer = []
    
    for idx in range(len(mylist[0])):
        temp = []
        for row in mylist:
            temp.append(row[idx])
        answer.append(temp)

    return answer

# 혹은 이런 스타일
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = [[],[],[]]

for i in range(3):
    for j in range(3):
        new_list[i].append( mylist[j][i] )