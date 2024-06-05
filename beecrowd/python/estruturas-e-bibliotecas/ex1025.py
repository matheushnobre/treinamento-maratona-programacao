def busca(marm, p):
    i = 0
    f = len(marm) - 1
    
    while i <= f:
        m = (i+f) // 2
        if marm[m] == p:
            while m >= 0:
                if marm[m-1] == p:
                    m -= 1
                else:
                    return m
            return m
        elif marm[m] < p:
            i = m+1
        else:
            f = m-1
            
    return -1

ct = 0
while True:
    ct += 1
    n, q = map(int, input().split())
    if n == q == 0: break
    
    marm = []
    for i in range(n):
        marm.append(int(input()))
    marm.sort()
    print(f'CASE# {ct}:')
    for i in range(q):
        cons = int(input())
        p = busca(marm, cons)
        if p == -1:
            print(f'{cons} not found')
        else:
            print(f'{cons} found at {p+1}')
    