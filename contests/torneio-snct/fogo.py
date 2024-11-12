def verificarVizinhos(i, j, n):
    global matriz
    global controle
    
    # Verificando se vizinhos já analisados são igual a 1. Caso positivo, este foco já foi analisado
    if i-1 >= 0 and matriz[i-1][j] == 1: 
        return 0
    if j-1 >= 0 and matriz[i][j-1] == 1: 
        return 0
    
    # Verificando qual será o tamanho do quadrado
    qtdJ = 0
    for newJ in range(j, j+4):
        if newJ < n and matriz[i][newJ] == 1:
            qtdJ += 1
        else: 
            break

    # Se o quadrado tiver lado 1, não é um foco controlado
    if qtdJ == 1: 
        return 0
    
    # Verificando se o quadrado não irá possuir lado maior do que 4
    if qtdJ == 4 and j+4 < n and matriz[i][j+4] == 1:
        return 0
    
    # Verificando as linhas que formam o nosso quadrado
    for newI in range(i+1, i+qtdJ):
        # Verificando se o I já excedeu o limite da matriz
        if newI >= n:
            return 0
        
        # Verificando se não continua a ter incêndio antes do quadrado
        if j-1 > 0 and matriz[newI][j-1] == 1: 
            return 0
        
        # Verificando pontos do quadrado
        for newJ in range(j, j+qtdJ):
            if matriz[newI][newJ] == 0:
                return 0
            
        # Verificando se não continua a ter incêndio depois do quadrado
        if j+qtdJ < n and matriz[newI][j+qtdJ] == 1:
            return 0

    return 1

n = int(input())
matriz = []

for _ in range(n):
    matriz.append(list(map(int, input().split())))

saida = 0
for i in range(n):
    for j in range(n):
        if matriz[i][j] == 1:
            saida += verificarVizinhos(i, j, n)
                
print(saida)