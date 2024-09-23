t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    if k % 2 == 0:
        if k % 4 == 0: print('YES')
        else: print('NO')
    else:
        if n % 2 == 0:
            if (k+1) % 4 != 0:
                print('YES')
            else:
                print('NO')
        else:
            if (k+1) % 4 == 0:
                print('YES')
            else:
                print('NO')