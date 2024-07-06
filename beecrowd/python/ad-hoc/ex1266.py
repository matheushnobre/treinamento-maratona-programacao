while True:
    n = int(input())
    if n == 0: break
    muro = [int(i) for i in input().split()]
    
    saida = 0
    postes = 0
    
    # Jogando os zeros pro final para iniciar a verificação a partir do 1
    for i in range(n):
        if muro[0] == 0:
            del muro[0]
            muro.append(0)
            if i == n-1 and n % 2 == 1: saida += 1
        else:
            break
        
    # Verificando a saída
    for i in range(n):
        if muro[i] == 0:
            postes += 1
        else:
            saida += (postes//2)
            postes = 0
    
    saida += (postes//2)
    print(saida)