f1, f2 = map(float, input().split())
r1 = 100 + f1
r2 = (r1 + ((f2/100) * r1))
r3 = r2 - 100

print(f'{r3:.6f}')