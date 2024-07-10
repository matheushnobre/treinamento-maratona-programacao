def bfs(lp, g):
    v = len(lp)
    visitados = [0] * v
    visitados[0] = 1
    distancias = [-1] * v
    distancias[0] = 0
    fila = [0]
    
    while len(fila) != 0:
        v_atual = fila[0]
        del fila[0]
        
        for vz in grafo[v_atual]:
            if visitados[vz] == 0:
                visitados[vz] = 1
                distancias[vz] = distancias[v_atual] + 1
                fila.append(vz)

    cont = 0
    convidados = []
    for i, d in enumerate(distancias):
        if 0 < d <= g:
            cont += 1
            convidados.append(lp[i])
            
    return cont, convidados

lp = ['Rerisson']
grafo = [[]]
n, g = map(int, input().split())

for i in range(n):
    a, b = input().split()
    if a not in lp: 
        lp.append(a)
        grafo.append([])
    if b not in lp: 
        lp.append(b)
        grafo.append([])
    
    ia = lp.index(a)
    ib = lp.index(b)
    grafo[ia].append(ib)
    grafo[ib].append(ia)
    
c, conv = bfs(lp, g)
print(c)
conv.sort()
print(*conv, sep='\n')
    
    