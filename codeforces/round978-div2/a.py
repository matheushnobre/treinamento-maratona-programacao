t = int(input())
for _ in range(t):
    n, r = map(int, input().split())
    d=0
    s=0
    for f in input().split():
        f = int(f)
        d += f//2
        s += f%2
    f = d*2
    t = 2*r
    fil = r-d
    if s < fil:
        f += s
    else: 
        f += (fil*2-s)
    print(f)