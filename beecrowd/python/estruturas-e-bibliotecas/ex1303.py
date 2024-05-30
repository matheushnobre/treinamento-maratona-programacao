inst = 0
while True:
    n = int(input())
    if n == 0: break
    if inst != 0: print()
    inst += 1
    
    # Matriz para armazenar os times. Cada lista contém 5 inteiros, representando: o time, o número de pontos, cestas pró, cestas contra, cesta average
    times = [[int(i), 0, 0, 0, 0] for i in range(1, n+1)]
    
    for jogo in range((n * (n-1)) // 2):
        a, pa, b, pb = map(int, input().split())
        
        # Verificando quem venceu para adicionar os pontos
        if pa > pb:
            times[a-1][1] += 2
            times[b-1][1] += 1
        else:
            times[b-1][1] += 2
            times[a-1][1] += 1
            
        # Adicionando os pontos
        times[a-1][2] += pa
        times[a-1][3] += pb
        times[b-1][2] += pb
        times[b-1][3] += pa
        
    # Calculando cesta average de cada time
    for i in range(n):
        try:
            times[i][4] = times[i][2] / times[i][3]
        except ZeroDivisionError:
            times[i][4] = times[i][2]
        
    # Ordenando a tabela de classificação:
    for i in range(n):
        for j in range(n-1):
            if times[j][1] < times[j+1][1]:
                times[j], times[j+1] = times[j+1], times[j]
            elif times[j][1] == times[j+1][1]:
                if times[j][4] < times[j+1][4]:
                    times[j], times[j+1] = times[j+1], times[j]
                elif times[j][4] == times[j+1][4]:
                    if times[j][2] < times[j+1][2]:
                        times[j], times[j+1] = times[j+1], times[j]
                    elif times[2] == times[j+1][2]:
                        if times[j][0] > times[j+1][0]:
                            times[j], times[j+1] = times[j+1], times[j]
                            
    print(f'Instancia {inst}')
    c = []
    for time in times:
        c.append(time[0])
    print(' '.join(str(t) for t in c))