while True:
    m, n, p = map(int, input().split())
    if m == n == p == 0: break
    
    l = 0
    for i in range(p):
        e = int(input())%n
        if e == 0: e = n
        l += ((n-e)+1)
        
    print(f'Lights: {l}')