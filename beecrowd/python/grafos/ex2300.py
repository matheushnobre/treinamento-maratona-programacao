def bfs(o, m, v):
    # o = origem
    # m = matriz
    # v = vertices
    visitados = [0] * v
    visitados[o] = 1
    fila = [o]
    
    while len(fila) != 0:
        v_atual = fila[0]
        del fila[0]
        
        for vz in range(v):
            if visitados[vz] == 0 and m[v_atual][vz] == 1:
                visitados[vz] = 1
                fila.append(vz)
                
    return visitados

ct = 0
while True:
    ct += 1
    e, l = map(int, input().split())
    # e = estacoes
    # l = linhas
    if e == l == 0: break
    
    m = [[0] * e for _ in range(e)]
    # m = matriz
        
    for _ in range(l):
        x, y = map(int, input().split())
        m[x-1][y-1] = 1
        m[y-1][x-1] = 1

    if bfs(0, m, e) == [1] * e:
        falha = False
    else:
        falha = True
    
    print(f'Teste {ct}')
    
    if falha:
        print('falha')
    else:
        print('normal')
    
    print()