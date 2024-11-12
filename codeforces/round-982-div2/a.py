t = int(input())
for _ in range(t):
    w = []
    h = []
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        w.append(a)
        h.append(b)
    h.sort()
    w.sort()
    print(h[-1]*2 + w[-1]*2)