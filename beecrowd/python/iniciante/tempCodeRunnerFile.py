from math import sqrt

n = int(input())
fibo = (((1 + sqrt(5))/2)**n - ((1 - sqrt(5))/2)**n) / sqrt(5)
print(f'{fibo:.1f}')