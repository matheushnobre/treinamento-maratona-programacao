p, c, n = map(int, input().split())
v = [int(i) for i in input().split()]

r = 0
for i in range(n):
    pt = p+c
    if p > v[i]:
        break
    if (pt) > v[i]:
        c -= (pt-v[i])
        if i != 0:
            r += 1
            
print(r)