m, n = map(int, input().split())
d = dict()

for i in range(m):
    p, v = input().split()
    d[p] = int(v)
    
for i in range(n):
    s = 0
    while True:
        t = input().split()
        if t == ['.']: break
        for p in t:
            if p in d:
                s += d[p]
    print(s)