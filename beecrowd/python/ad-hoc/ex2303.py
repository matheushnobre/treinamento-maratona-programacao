l, c, m, n = map(int, input().split())

plan = []
for i in range(l):
    plan.append([int(i) for i in input().split()])

maior = 0
for i in range(0, l, m):
    for j in range(0, c, n):
        lote = [plan[k][j:j+n] for k in range(i, i+m)]
        soma = 0
        for l in lote:
            soma += sum(l)
        if soma > maior:
            maior = soma
            
print(maior)