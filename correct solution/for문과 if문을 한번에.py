# for 문과 if문을 한번에
# 문제 설명
# 정수를 담은 리스트 mylist를 입력받아, 이 리스트의 원소 중 짝수인 값만을 제곱해 담은 새 리스트를 리턴하는 solution함수를 완성해주세요. 예를 들어, [3, 2, 6, 7]이 주어진 경우

# 3은 홀수이므로 무시합니다.
# 2는 짝수이므로 제곱합니다.
# 6은 짝수이므로 제곱합니다.
# 7은 홀수이므로 무시합니다.
# 따라서 2의 제곱과 6의 제곱을 담은 리스트인 [4, 36]을 리턴해야합니다.

# 제한 조건
# mylist는 길이가 100이하인 배열입니다.
# mylist의 원소는 1이상 100 이하인 정수입니다.

# 1
mylist = [3, 2, 6, 7]
def solution(mylist):
    answer = [element**2 for element in mylist if element%2==0]
    return answer
print(solution(mylist))

# 2
# 비트연산 : 숫자가 커질경우 mod연산보다 비트연산이 권장된다.
answer = [element**2 for element in mylist if element&1==0]
print(answer)

# 참고
# 거듭제곱은 내장함수 pow(base,exp[,mod])를 사용하기도 한다.
print('2의 3승 : ',end='')
print(pow(2,3))
print('2의 3승은 짝수이다 : ',end='')
print(pow(2,3,mod=2)==0)