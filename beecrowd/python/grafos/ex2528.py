def rota(origem, destino, proibido, lista):
    visitados = [0] * len(lista)
    distancia = [-1] * len(lista)
    visitados[origem] = 1
    distancia[origem] = 0
    fila = [origem]
    
    while len(fila) != 0:
        v_atual = fila[0]
        del fila[0]
        
        for vizinho in lista[v_atual]:
            if visitados[vizinho] == 0 and vizinho != proibido:
                visitados[vizinho] = 1
                distancia[vizinho] = distancia[v_atual] + 1
                fila.append(vizinho)
                if vizinho == destino:
                    return distancia[vizinho]
    
while True:
    try:
        n, m = map(int, input().split())
        cidades = [[] for i in range(n)]
        for i in range(m):
            a, b = map(int, input().split())
            cidades[a-1].append(b-1)
            cidades[b-1].append(a-1)
        c, r, e = map(int, input().split())
        print(rota(c-1, r-1, e-1, cidades))
    except EOFError:
        break