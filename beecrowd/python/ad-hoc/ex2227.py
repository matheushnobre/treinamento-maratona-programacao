ct = 1
while True:
    a, v = map(int, input().split())
    if a == v == 0: break
    
    voos = {i+1: 0 for i in range(a)}
    for i in range(v):
        x, y = map(int, input().split())
        voos[x] += 1
        voos[y] += 1
        
    mt, amt = 0, []
    for chave, valor in voos.items():
        if valor == mt:
            amt.append(chave)
        elif valor > mt:
            amt.clear()
            amt.append(chave)
            mt = valor
    
    print(f'Teste {ct}')
    print(' '.join(map(str, amt)),'')
    print()
    
    ct += 1