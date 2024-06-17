while True:
    n, m = input().split()
    if n == m == '0': break
    
    while len(n) > 1:
        n = str(sum(map(int, n)))
        
    while len(m) > 1:
        m = str(sum(map(int, m)))
        
    n, m = map(int, [n, m])
    if n > m: print(1)
    elif n < m: print(2)
    else: print(0)
        