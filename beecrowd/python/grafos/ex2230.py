def bfs(o, g, v, p):
    visitados = [0] * v
    visitados[o] = 1
    fila = [o]
    
    distancia = [-1] * v
    distancia[o] = 0
    
    while len(fila) != 0:
        v_atual = fila[0]
        del fila[0]
        
        for vz in range(v):
            if visitados[vz] == 0 and g[v_atual][vz] == 1:
                visitados[vz] = 1
                distancia[vz] = distancia[v_atual] + 1
                fila.append(vz)
        
    retorno = [i+1 for i in range(v) if 0 < distancia[i] <= p]
    return retorno

ct = 0
while True:
    ct += 1
    c, e, l, p = map(int, input().split())
    if c == 0: break
    
    grafo = [[0] * c for _ in range(c)]
    
    for _ in range(e):
        x, y = map(int, input().split())
        grafo[x-1][y-1] = 1
        grafo[y-1][x-1] = 1
        
        saida = bfs(l-1, grafo, c, p)
    
        print(f'Teste {ct}')
        for n in saida:
            print(n, end=' ')
        print('\n')