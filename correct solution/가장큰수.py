# 가장 큰 수, inf
# 코딩 테스트 문제 등을 풀다 보면, 최솟값을 저장하는 변수에 아주 큰 값을 할당해야 할 때가 있습니다. 이번 시간에는 이때에 사용하기 좋은 inf에 대해 알아봅시다.

# 파이썬이 제공하는 inf 를 사용해보세요. inf는 어떤 숫자와 비교해도 무조건 크다고 판정됩니다.

min_val = float('inf')
alwaysTrue = min_val > 999999999999999999999999999999999999999999999999999999
print(alwaysTrue)

# inf에는 음수 기호를 붙이는 것도 가능합니다
min_val_2 = float('-inf')
alwaysTrue_2 = min_val_2 < -9999999999999999999999999999999999999999999999999999
print(alwaysTrue_2)