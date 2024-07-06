def dfs(atual):
    visitados[atual] = 1
    
    for vz in grafo[atual]:
        if visitados[vz] == 0:
            dfs(vz)

pessoas = []
m, n = map(int, input().split())

visitados = [0] * m
grafo = [[] for _ in range(m)]

for _ in range(n):
    p1, r, p2 = input().split()
    if p1 not in pessoas:
        pessoas.append(p1)
    if p2 not in pessoas:
        pessoas.append(p2)
        
    ip1, ip2 = pessoas.index(p1), pessoas.index(p2)
    grafo[ip1].append(ip2)
    grafo[ip2].append(ip1)
    
fam = 0
for i in range(m):
    if(visitados[i] == 0):
        dfs(i)
        fam += 1
        
print(fam)