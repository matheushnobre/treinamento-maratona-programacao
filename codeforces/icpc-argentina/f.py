n = int(input())
v = list(map(int, input().split()))
c = p = 0
for valor in v:
    if valor == 1:
        p += 1
        c += 1
        if c >= 3:
            p += 1
    else:
        p -= 1
        c = 0
        
print(p)