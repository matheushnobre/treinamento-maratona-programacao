t = int(input())
for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    s = 'YES'
    for i in range(1, n):
        if abs(m[i] - m[i-1]) not in [5, 7]:
            s = 'NO'
    print(s)