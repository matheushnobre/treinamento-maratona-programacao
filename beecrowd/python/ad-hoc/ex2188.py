ct = 0
while True:
    ct += 1
    n = int(input())
    if n == 0: break
    a = []
    
    for i in range(n):
        x, y, u, v = map(int, input().split())
        if i == 0:
            a = [x, y, u, v]
        else:
            a[0] = max(a[0], x)
            a[1] = min(a[1], y)
            a[2] = min(a[2], u)
            a[3] = max(a[3], v)
            
    if a[3] > a[1] or a[2] < a[0]:
        a.clear()
            
    print(f'Teste {ct}')
    if len(a) == 0:
        print('nenhum')
    else:
        print(*a)
    print('')
        