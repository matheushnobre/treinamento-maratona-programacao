def trocar(lista, index):
    lista[index], lista[index+1] = lista[index+1], lista[index]

n = int(input())

seres = []
for i in range(n):
    s, p, k, m = input().split()
    p, k, m = map(int, [p, k, m])
    seres.append((s, p, k, m))
    
for i in range(n-1, 0, -1):
    for j in range(i):
        if seres[j][1] < seres[j+1][1]:
            trocar(seres, j)
        elif seres[j][1] == seres[j+1][1]:
            if seres[j][2] < seres[j+1][2]:
                trocar(seres, j)
            elif seres[j][2] == seres[j+1][2]:
                if seres[j][3] > seres[j+1][3]:
                    trocar(seres, j)
                elif seres[j][3] == seres[j+1][3]:
                    if seres[j][0] > seres[j+1][0]:
                        trocar(seres, j)

print(seres[0][0])