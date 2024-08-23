auxi = [-1, 1, 0, 0]
auxj = [0, 0, -1, 1]

def isPossivel(i, j):
    return i>=0 and i<h and j>=0 and j<l and visitados[i][j] == 0

def contar(i, j):
    visitados[i][j] = 1
    fila = [(i, j)]
    area = 1
    while len(fila) != 0:
        i_atual, j_atual = fila[0]
        del fila[0]
        
        for k in range(4):
            newi = i_atual+auxi[k]
            newj = j_atual+auxj[k]
            if isPossivel(newi, newj) and matriz[i][j] == matriz[newi][newj]:
                visitados[newi][newj] = 1
                fila.append((newi, newj))
                area += 1

    return area
    
h, l = map(int, input().split())
matriz = []
for i in range(h):
    matriz.append([int(i) for i in input().split()])

visitados = [[0 for i in range(l)] for j in range(h)]

menor = 100000
for i in range(h):
    for j in range(l):
        if visitados[i][j] == 0:
            a = contar(i, j)
            if a < menor:
                menor = a
                
print(menor)