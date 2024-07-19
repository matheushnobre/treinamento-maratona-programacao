dic = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}

auxi = [-1, -1, -2, -2, 1, 1, 2, 2]
auxj = [-2, 2, -1, 1, -2, 2, -1, 1]

def isValid(i, j, graf):
    return i>=0 and i<8 and j>=0 and j<8 and graf[i][j] == 0

def busca(inicial, final):
    visitados = [[0]*8 for i in range(8)]
    visitados[inicial[0]][inicial[1]] = 1
    distancias = [[-1]*8 for i in range(8)]
    distancias[inicial[0]][inicial[1]] = 0
    fila = [inicial]

    while len(fila) != 0:
        i, j = fila[0]
        del fila[0]
        
        for k in range(8):
            newI = i+auxi[k]
            newJ = j+auxj[k]
            
            if isValid(newI, newJ, visitados):
                visitados[newI][newJ] = 1
                distancias[newI][newJ] = distancias[i][j] + 1
                fila.append((newI, newJ))
                if newI == final[0] and newJ == final[1]:
                    return distancias[newI][newJ]

while True:
    try:
        a, b = input().split()
        inicial = (8-int(a[1]), dic[a[0]])
        final = (8-int(b[1]), dic[b[0]])
        
        if a==b: mov = 0
        else: mov = busca(inicial, final)
        print(f'To get from {a} to {b} takes {mov} knight moves.')
    except EOFError: 
        break