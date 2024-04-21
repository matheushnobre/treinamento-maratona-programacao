import math

n = int(input())
for i in range(n):
    c = float(input())
    d = math.log(1/c, 0.5)
    d = int(d) + 1 if d % 1 != 0 else int(d)
    print(f'{d} dias')