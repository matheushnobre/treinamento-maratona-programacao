t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    
    g = s = 0
    for p in l:
        if p >= k:
            g += p
        elif p == 0:
            if g > 0:
                g -= 1
                s += 1
                
    print(s)