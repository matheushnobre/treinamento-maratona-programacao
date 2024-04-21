while True:
    b, n = map(int, input().split())
    if b == n == 0: break
    
    r = [int(i) for i in input().split()]
    db = dict()
    for i, r1 in enumerate(r):
        db[i+1] = r1
    
    for i in range(n):
        d, c, v = map(int, input().split())
        db[d] -= v
        db[c] += v
        
    p = True
    for valor in db.values():
        if valor < 0:
            p = False
            break
    print('S') if p else print('N')