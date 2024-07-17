from heapq import heappop, heappush
INF = 1e10

def dijkstra(o, d, grafo):
    v = len(grafo)
    distancias = [INF for _ in range(v)]
    distancias[o] = 0
    fila = []
    
    heappush(fila, (0, o))
    
    while len(fila) > 0:
        dist, v_atual = heappop(fila)
        if dist > distancias[v_atual]:
            continue
        for vizinho, peso in grafo[v_atual]:
            if distancias[v_atual]+peso >= distancias[vizinho]:
                continue
            distancias[vizinho] = distancias[v_atual]+peso
            heappush(fila, (distancias[vizinho], vizinho))
            
    return distancias[d]

while True:
    n, e = map(int, input().split())
    if n == 0: break
    
    grafo = [[] for _ in range(n)]

    for _ in range(e):
        x, y, h = map(int, input().split())
        aux = True
        for i, v in enumerate(grafo[y-1]):
            if v[0] == x-1:
                grafo[x-1].append((y-1, 0))
                grafo[y-1][i] = ((x-1, 0))
                aux = False
        if aux: grafo[x-1].append((y-1, h))
        
        
    k = int(input())
    for _ in range(k):
        o, d = map(int, input().split())
        s = dijkstra(o-1, d-1, grafo)
        if s == INF: print('Nao e possivel entregar a carta')
        else: print(s)
    print('')