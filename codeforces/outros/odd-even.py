n, k = map(int, input().split())

if k*2 - 1 <= n:
    print(k*2-1)
else:
    if n % 2 == 0:
        m = n // 2
    else:
        m = n // 2 + 1
    print((k-m)*2)