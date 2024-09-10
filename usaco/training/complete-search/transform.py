"""
ID: matheus30
LANG: PYTHON3
TASK: transform
"""

fin = open('transform.in', 'r')
fout = open('transform.out', 'w')

def rota90(matriz, n):
    novamatriz = [[0]*n for i in range(n)]
    for i in range(n):
        novacoluna = n-i-1
        for j in range(n):
            novamatriz[j][novacoluna] = matriz[i][j]
    return novamatriz

def rota180(matriz, n):
    m1 = rota90(matriz, n)
    return rota90(m1, n)

def rota270(matriz, n):
    m1 = rota180(matriz, n)
    return rota90(m1, n)

def reflete(matriz, n):
    novamatriz = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            novamatriz[i][n-j-1] = matriz[i][j]
    return novamatriz

def combina1(matriz, n):
    m1 = reflete(matriz, n)
    return rota90(m1, n)

def combina2(matriz, n):
    m1 = reflete(matriz, n)
    return rota180(m1, n)

def combina3(matriz, n):
    m1 = reflete(matriz, n)
    return rota270(m1, n)
    
n = int(fin.readline())
matriz1 = []
for i in range(n):
    matriz1.append(list(fin.readline().strip()))

matriz2 = []
for i in range(n):
    matriz2.append(list(fin.readline().strip()))
    
if matriz2 == rota90(matriz1, n):
    fout.write("1\n")
elif matriz2 == rota180(matriz1, n):
    fout.write("2\n")
elif matriz2 == rota270(matriz1, n):
    fout.write("3\n")
elif matriz2 == reflete(matriz1, n):
    fout.write("4\n")
elif matriz2 == combina1(matriz1, n) or matriz2 == combina2(matriz1, n) or matriz2 == combina3(matriz1, n):
    fout.write("5\n")
elif matriz1 == matriz2:
    fout.write("6\n")
else:
    fout.write("7\n")