t = int(input())
for i in range(t):
    n = int(input())
    temp = {}
    
    for j in range(n):
        l, r = map(int, input().split())
        for t in range(l, r+1):
            try:
                temp[t] += 1
            except KeyError:
                temp[t] = 1
    
    tempLivre = False
    for valor in temp.values():
        if valor == n:
            tempLivre = True
            break
    
    if tempLivre: print('YES')
    else: print('NO')