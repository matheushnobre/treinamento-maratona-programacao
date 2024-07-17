ax = [-1, -1, -1, 0, 0, 1, 1, 1]
ay = [-1, 0, 1, -1, 1, -1, 0, 1]

def isValid(graf, x, y):
    return x>=0 and x<len(graf) and y>=0 and y<len(graf[0]) and graf[x][y][0]==1

def dias(graf, x, y):
    graf[x][y] = (2, 0)
    s=0
    fila = [(x, y)]
    
    while len(fila) != 0:
        i, j = fila[0]
        del fila[0]
        
        for c in range(8):
            newi, newj = i+ax[c], j+ay[c]
            if isValid(graf, newi, newj):
                graf[newi][newj] = (2, graf[i][j][1]+1)
                s=graf[newi][newj][1]
                fila.append((newi, newj))
    
    return s

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    graf = []
    for i in range(a):
        graf.append([(int(g), 0) for g in input().split()])
    x, y = map(int, input().split())
    print(dias(graf, x-1, y-1))