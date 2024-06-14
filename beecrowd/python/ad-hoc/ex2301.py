ct = 0
while True:
    p, r = map(int, input().split())
    if p == r == 0: break
    ct += 1
    
    fila = [int(i) for i in input().split()]
    
    for _ in range(r):
        n, j, *acoes = map(int, input().split())
        e = 0
        for i, a in enumerate(acoes):
            if a != j:
                del fila[i-e]
                e += 1
    print(f'Teste {ct}')
    print(fila[0])
    print()