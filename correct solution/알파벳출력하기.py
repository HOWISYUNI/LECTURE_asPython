# 문제 설명
# 입력으로 0이 주어지면 영문 소문자 알파벳을, 입력으로 1이 주어지면 영문 대문자 알파벳을 사전 순으로 출력하는 코드를 짜세요.

# 예시 1
# 입력

# 0
# 출력

# abcd... (생략)
# 예시 2
# 입력

# 1
# 출력

# ABCD... (생략)

import string


for i in range(3):

    num = int(input().strip())

    if num == 0:
        print(string.ascii_lowercase) # 소문자 abcdefghijklmnopqrstuvwxyz
        print(type(string.ascii_lowercase)) # str
    elif num == 1:
        print(string.ascii_uppercase) # # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
        print(type(string.ascii_uppercase)) # str
    else:
        print(string.ascii_letters) # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        print(type(string.ascii_letters)) # str
        print(string.digits) # 숫자 0123456789
        print(type(string.digits)) # str