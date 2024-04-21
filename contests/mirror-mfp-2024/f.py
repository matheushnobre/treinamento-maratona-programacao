n = int(input())
t1 = 0
t2 = 0
for i in range(n):
    e = input()
    if e[5] == '1':
        t1 += int(e[8])
    else:
        t2 += int(e[8])
print(f'{t1} x {t2}')