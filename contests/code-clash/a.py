matriz = []
for i in range(4):
    linha = list(input())
    matriz.append(linha)
    
r = []
for i in range(len(matriz[0])):
    coluna = ''
    for j in range(4):
        coluna += matriz[j][i]
    
    r.append(int(coluna))

f = r[0]
l = r[-1]
s = ''
for i in range(1, len(matriz[0])-1):
    v = (f * r[i] + l) % 257
    s += chr(v)
    
print(s)