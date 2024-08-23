INF = int(1e10)

l, c = map(int, input().split())
matriz = []

for i in range(l):
    matriz.append(list(map(int, input().split())))
    
distancias = [[INF for i in range(c)] for i in range(l)]
distancias[0] = matriz[0]

for i in range(l):
    for j in range(c):
        if j>0:
            if distancias[i][j] + matriz[i][j-1] < distancias[i][j-1]:
                distancias[i][j-1] = distancias[i][j] + matriz[i][j-1]
            
        if j < c-1:
            if distancias[i][j] + matriz[i][j+1] < distancias[i][j+1]:
                distancias[i][j+1] = distancias[i][j] + matriz[i][j+1]
                    
        if i < l-1:
            if distancias[i][j] + matriz[i+1][j] < distancias[i+1][j]:
                distancias[i+1][j] = distancias[i][j] + matriz[i+1][j]
    
    for j in range(c-1, -1, -1):
        if j>0:
            if distancias[i][j] + matriz[i][j-1] < distancias[i][j-1]:
                distancias[i][j-1] = distancias[i][j] + matriz[i][j-1]
            
        if j < c-1:
            if distancias[i][j] + matriz[i][j+1] < distancias[i][j+1]:
                distancias[i][j+1] = distancias[i][j] + matriz[i][j+1]
                    
        if i < l-1:
            if distancias[i][j] + matriz[i+1][j] < distancias[i+1][j]:
                distancias[i+1][j] = distancias[i][j] + matriz[i+1][j]
    
menor, index = INF, 0
for i in range(c):
    if distancias[-1][i] < menor:
        menor = distancias[-1][i]
        index = i+1

print(menor, index)