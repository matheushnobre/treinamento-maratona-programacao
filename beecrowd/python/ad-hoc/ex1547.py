n = int(input())
for i in range(n):
    qt, s = map(int, input().split())
    v = [int(i) for i in input().split()]
    
    p = v[0]
    for a in v:
        if a == s:
            p = a
            break
        elif abs(a-s) < abs(p-s):
            p = a
    print(v.index(p)+1)