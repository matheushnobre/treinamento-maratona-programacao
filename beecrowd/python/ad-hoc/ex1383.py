def verificarSudoku(matriz):
    # 1º passo: verificar linhas
    for linha in matriz:
        l = set(linha)
        if len(l) != 9:
            return 'NAO'
        
    # 2º passo: verificar colunas
    for j in range(9):
        coluna = [matriz[i][j] for i in range(9)]
        c = set(coluna)
        if len(c) != 9:
            return 'NAO'
    
    # 3º passo: verificar as submatrizes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            grupo = [matriz[k][j:j+3] for k in range(i, i+3)]
            grupo = grupo[0] + grupo[1] + grupo[2]
            g = set(grupo)
            if len(g) != 9:
                return 'NAO'
    
    return 'SIM'
    
n = int(input())

for i in range(n):
    matriz = []
    for j in range(9):
        matriz.append([int(i) for i in input().split()])
    print(f'Instancia {i+1}')
    print(verificarSudoku(matriz))
    print('')