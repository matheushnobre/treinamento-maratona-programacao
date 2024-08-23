from heapq import heappush, heappop
INF = int(10e10)

def dijkstra(adjacencias, origem, destino):
    dPar = [(INF, 0) for _ in range(len(adjacencias))]
    dPar[origem] = (0, 0)
    
    dImpar = [(INF, 0) for _ in range(len(adjacencias))]
    dImpar[origem] = (INF, 0)  
    fila = []
    
    heappush(fila, (0, origem, 0))  
    
    while len(fila) > 0:
        dist, v_atual, paridade = heappop(fila)
        
        if paridade == 0 and dist > dPar[v_atual][0]:
            continue
        if paridade == 1 and dist > dImpar[v_atual][0]:
            continue
        
        for vz, peso in adjacencias[v_atual]:
            novo_custo = dist + peso
            nova_paridade = (paridade + 1) % 2
            
            if nova_paridade == 0:  
                if dPar[vz][0] >= novo_custo:
                    dPar[vz] = (novo_custo, dPar[v_atual][1] + 1)
                    heappush(fila, (novo_custo, vz, nova_paridade))
            else: 
                if dImpar[vz][0] >= novo_custo:
                    dImpar[vz] = (novo_custo, dImpar[v_atual][1] + 1)
                    heappush(fila, (novo_custo, vz, nova_paridade))
    
    if dPar[destino][0] == INF:
        return -1
    return dPar[destino][0]


c, v = map(int, input().split())
adjacencias = [[] for _ in range(c + 1)]

for _ in range(v):
    c1, c2, g = map(int, input().split())
    adjacencias[c1].append((c2, g))
    adjacencias[c2].append((c1, g))

print(dijkstra(adjacencias, 1, c))
