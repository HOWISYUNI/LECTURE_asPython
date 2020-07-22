num, base = map(int, input().strip().split(' '))

exponent = 0
result = 0

while num>10:
    remainder = num%10
    num = num//10
    result = result + remainder * pow(base,exponent)
    exponent = exponent+1

result = result + num*pow(base,exponent)

print(result)