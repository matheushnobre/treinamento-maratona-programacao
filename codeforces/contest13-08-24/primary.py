t = int(input())
for _ in range(t):
    n = input()
    if len(n) <= 2:
        print('NO')
    elif n[:2] != '10':
        print('NO')
    elif n[2] == '0':
        print('NO')
    elif len(n) == 3 and n[2] == '1':
        print('NO')
    else:
        print('YES')