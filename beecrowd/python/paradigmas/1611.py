t = int(input())
for _ in range(t):
    n, c, m = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort(reverse=True)
    a = 0
    for i in range(0, m, c):
        a += p[i]
    a *= 2
    print(a)