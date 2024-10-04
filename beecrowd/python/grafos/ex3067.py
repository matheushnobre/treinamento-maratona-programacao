def verificaInicial(pecas):
    impares = 0
    for p in range(7):
        if len(pecas[p]) % 2 == 1:
            impares += 1
    return impares == 0 or impares == 2

def bfs(pecas):
    if not verificaInicial(pecas):
        return False
    
    fila = []
    visitados = [0] * 7
    for p in range(7):
        if len(pecas[p]) > 0:
            fila.append(p)
            break
    visitados[p] = 1
    
    while len(fila) != 0:
        p = fila[0]
        del fila[0]
        
        if len(pecas[p]) == 0:
            break 
        
        for a, b in pecas[p]:
            if visitados[b] == 0:
                visitados[b] = 1
                fila.append(b)
        
    for p in range(7):
        if len(pecas[p]) > 0 and not visitados[p]:
            return False
    
    return True 

ct = 0
while True:
    ct += 1
    pecas = [[] for i in range(7)]
    n = int(input())
    if n == 0: break
    
    for i in range(n):
        a, b = map(int, input().split())
        pecas[a].append((a, b))
        pecas[b].append((b, a))
       
    print(f'Teste {ct}') 
    if bfs(pecas):
        print('sim')
    else:
        print('nao')
    print()
    