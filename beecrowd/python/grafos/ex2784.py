from heapq import heappush, heappop

def dijkistra(origem, lista):
    INF = 10e10
    distancias = [INF for u in range(len(lista))]
    distancias[origem] = 0
    fila_prioridade = []
    
    heappush(fila_prioridade, (0, origem))
    
    while len(fila_prioridade) > 0:
        dist, v_atual = heappop(fila_prioridade)
        if dist > distancias[v_atual]:
            continue
        
        for vizinho, peso in lista[v_atual]:
            if distancias[v_atual] + peso >= distancias[vizinho]:
                continue
            distancias[vizinho] = distancias[v_atual] + peso
            heappush(fila_prioridade, (distancias[vizinho], vizinho))
            
    return distancias

n, m = map(int, input().split())
ilhas = [[] for i in range(n)]

for i in range(m):
    u, v, p = map(int, input().split())
    ilhas[u-1].append((v-1, p))
    ilhas[v-1].append((u-1, p))
    
s = int(input())

distancias = dijkistra(s-1, ilhas)
del distancias[s-1]
print(max(distancias) - min(distancias))