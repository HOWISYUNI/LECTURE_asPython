"""
with ~ as 방법의 장점
1. 파일을 close하지 않아도 된다.
2. while문 안에서 EOF을 계속 체크하지 않아도 된다."""

with open('myfile.txt') as file:
    for line in file.readlines():
        print(line)
        # print(line.strip().split('\t')) # 위 코드와 비교


"""
open ~ while ~ close 방법의 단점
1. close를 호출해야한다.
2. while문 안에서 계속 EOF을 확인해야한다.
"""

f = open('myfile.txt','r')
while True:
    line = f.readline()
    if not line: break
    # raw = line.split()
    print(line)
    # print(raw)
f.close()