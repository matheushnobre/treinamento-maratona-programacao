a, b, c, d = map(int, input().split())
saiu = False

if b == 1:
    print(-1)
elif a != 1:
    while a < int(10e9):
        if a % b != 0 and c % a == 0 and d % a != 0:
            print(a)
            saiu = True
            break
        a *= 2
    if not saiu: print(-1)
else:
    while a < int(10e9):
        if a % b != 0 and c % a == 0 and d % a != 0:
            print(a)
            saiu = True
            break
        a += 1
    if not saiu: print(-1)