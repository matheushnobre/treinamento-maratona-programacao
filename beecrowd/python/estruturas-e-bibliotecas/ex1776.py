for casoTeste in range(int(input())):
    totalRenas, renasTreno = map(int, input().split())
    listaRenas = []
    
    for rena in range(totalRenas):
        nome, peso, idade, altura = input().split()
        listaRenas.append((nome, int(peso), int(idade), float(altura)))
    
    for i in range(totalRenas):
        for j in range(totalRenas-1):
            if listaRenas[j][1] < listaRenas[j+1][1]:
                listaRenas[j], listaRenas[j+1] = listaRenas[j+1], listaRenas[j]
            elif listaRenas[j][1] == listaRenas[j+1][1]:
                if listaRenas[j][2] > listaRenas[j+1][2]:
                    listaRenas[j], listaRenas[j+1] = listaRenas[j+1], listaRenas[j]
                elif listaRenas[j][2] == listaRenas[j+1][2]:
                    if listaRenas[j][3] > listaRenas[j+1][3]:
                        listaRenas[j], listaRenas[j+1] = listaRenas[j+1], listaRenas[j]
                    elif listaRenas[j][3] == listaRenas[j+1][3]:
                        if listaRenas[j][0] > listaRenas[j+1][0]:
                            listaRenas[j], listaRenas[j+1] = listaRenas[j+1], listaRenas[j]
    
    print('CENARIO {{{}}}'.format(casoTeste+1))
    for i in range(renasTreno):
        print(f'{i+1} - {listaRenas[i][0]}')