from heapq import heappush, heappop
INF = 10e10

def dijkstra(adjacenias, origem, destino, rota):
    distancias = [INF for _ in range(len(adjacencias))]
    distancias[origem] = 0 
    fila = []   

    heappush(fila, (origem, 0))
    while len(fila) > 0:
        v_atual, dist = heappop(fila)
        if dist > distancias[v_atual]:
            continue
        for vz, peso in adjacencias[v_atual]:
            if v_atual in rota[:-1]:
                if vz != v_atual + 1: 
                    continue
            if distancias[v_atual] + peso >= distancias[vz]:
                continue
            distancias[vz] = distancias[v_atual] + peso
            heappush(fila, (vz, distancias[vz]))

    return distancias[destino]
    
while True:
    n, m, c, k = map(int, input().split())
    if n == 0: break
    
    adjacencias = [[] for _ in range(n)]
    rota = [i for i in range(c)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        adjacencias[u].append((v, p))
        adjacencias[v].append((u, p))
        
    print(dijkstra(adjacencias, k, c-1, rota))