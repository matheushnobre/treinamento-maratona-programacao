g = int(input())
for ct in range(g):
    p = int(input())
    w = int(input())
    
    qtd = []
    pesos =[]
    for i in range(p):
        e, pc = map(int, input().split())
        qtd.append(e)
        pesos.append(pc)
        
    # Ideia da mochila
    aux = [[0]*(w+1) for _ in range(p+1)]
    for i in range(p):
        pc = pesos[i]
        e = qtd[i]
        for j in range(w+1):
            if j < pc:
                aux[i+1][j] = aux[i][j]
            else:
                aux[i+1][j] = max(aux[i][j], e + aux[i][j-pc])
                
    print(f'Galho {ct+1}:')
    print(f'Numero total de enfeites: {aux[-1][-1]}')
    print()