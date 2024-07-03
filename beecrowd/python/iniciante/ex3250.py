def bfs(f, s, g, u, d):
    s -= 1
    g -= 1
    visitados = [0] * f
    distancia = [-1] * f
    visitados[s] = 1
    fila = [s]
    distancia[s] = 0
    
    while len(fila) != 0:
        v_atual = fila[0]
        del fila[0]
        
        # Movimento UP
        up = v_atual + u
        if up < f:
            if visitados[up] == 0:
                visitados[up] = 1
                distancia[up] = distancia[v_atual] + 1
                fila.append(up)
                if up == g:
                    return distancia[up] 
                   
        # Movimento DOWN
        down = v_atual - d
        if down >= 0:
            if visitados[down] == 0:
                visitados[down] = 1
                distancia[down] = distancia[v_atual] + 1
                fila.append(down)
                if down == g:
                    return distancia[down] 

    return -1             

f, s, g, u, d = map(int, input().split())
if s == g:
    print(0)
else:
    r = bfs(f, s, g, u, d)
    if r != -1: print(r)
    else: print('use the stairs')