n = int(input())
for i in range(n):
    m = int(input())
    f = [int(i) for i in input().split()]
    
    fo = f.copy()
    fo.sort(reverse=True)
    
    s = 0
    for j in range(m):
        if f[j] == fo[j]:
            s += 1
    print(s)