# 두 변수의 값 바꾸기 - swap
# 이번 강의에서는 두 변수의 값을 바꾸는 방법을 배워봅시다. ( swap이라고 하지요 )

# 예시) a = 3, b = 'abc'를 a = 'abc', b = 3 으로 바꾸기

a = 3
b = 'abc'
print('a : '+str(a))
print('b : '+b)
print(type(a))

# swap
a,b=b,a

print('a : '+str(a))
print('b : '+str(b))