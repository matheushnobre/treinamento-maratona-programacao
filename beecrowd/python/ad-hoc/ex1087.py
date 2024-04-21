while True:
    # lendo a entrada do caso de teste
    valores = input().split(' ')
    x1, y1, x2, y2 = int(valores[0]), int(valores[1]), int(valores[2]), int(valores[3])
    
    # inicializando contador de movimentos necessários
    movimentos_necessarios=0
    
    # verificando se a entrada digitada é a entrada de saída
    if (x1==0) & (y1==0) & (x2==0) & (y2==0):
        break
    
    if(x1==x2) & (y1==y2): # valores iguais
        movimentos_necessarios = 0
    elif (x1==x2) | (y1==y2): # mesma linha ou mesma coluna
        movimentos_necessarios = 1
    elif abs(x2-x1) == abs(y2-y1): # mesma diagonal
        movimentos_necessarios = 1
    else:
        movimentos_necessarios = 2
    
    print(movimentos_necessarios)
    
    