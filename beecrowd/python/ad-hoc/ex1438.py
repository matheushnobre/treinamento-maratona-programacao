while True:
    n, p = map(int, input().split())
    if n == p == 0: break
    
    vetorPilhas = []
    for i in range(p):
        v, *pilha = map(int, input().split())
        if 1 in pilha: pilhaDo1 = i
        vetorPilhas.append(pilha)
    
    qtd = 0
    while(vetorPilhas[pilhaDo1][-1] != 1):
        vetorPilhas[pilhaDo1].pop()
        qtd += 1
            
    if pilhaDo1 != 0 and pilhaDo1 != p-1:
        qtdEsq = qtdDir = 0
        
        esq = pilhaDo1-1
        while(esq>=0):
            if(len(vetorPilhas[esq]) >= len(vetorPilhas[pilhaDo1])):
                while(len(vetorPilhas[esq]) >= len(vetorPilhas[pilhaDo1])):
                    vetorPilhas[esq].pop()
                    qtdEsq += 1
                esq -= 1
            else: break
            
        dir = pilhaDo1+1
        while(dir<=p-1):
            if(len(vetorPilhas[dir]) >= len(vetorPilhas[pilhaDo1])):
                while(len(vetorPilhas[dir]) >= len(vetorPilhas[pilhaDo1])):
                    vetorPilhas[dir].pop()
                    qtdDir += 1
                dir += 1
            else: break
        
        '''
        if(len(vetorPilhas[pilhaDo1-1]) <= len(vetorPilhas[pilhaDo1+1])):
            menor = pilhaDo1-1
        else:
            menor = pilhaDo1+1
            
        while(len(vetorPilhas[menor]) >= len(vetorPilhas[pilhaDo1])):
            vetorPilhas[menor].pop()
            qtd += 1
        '''
        
        qtd += min(qtdEsq, qtdDir)
    
    print(qtd)