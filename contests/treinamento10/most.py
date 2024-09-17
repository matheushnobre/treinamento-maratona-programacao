t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    pal = []
    for j in range(n):
        pal.append(input())
    
    d = 10e9
    for a in range(len(pal)):
        for b in range(a+1, len(pal)):
            p1 = pal[a]
            p2 = pal[b]
            dif = 0
            for c in range(m):
                c1 = ord(p1[c])-97
                c2 = ord(p2[c])-97
                dif += abs(c1 - c2)
            d = min(dif, d)
    
    print(d)