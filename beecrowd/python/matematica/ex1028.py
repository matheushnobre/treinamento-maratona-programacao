def mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(mdc(a, b))