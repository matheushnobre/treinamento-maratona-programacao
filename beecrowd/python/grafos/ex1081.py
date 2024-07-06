def dfs(v_atual, grafo, nivel):
    visitados[v_atual] = 1
    espacos = '  '*nivel
    
    for vz in grafo[v_atual]:
        if visitados[vz] == 0:
            print(f'{espacos}{v_atual}-{vz} pathR(G,{vz})')
            dfs(vz, grafo, nivel+1)
        else:
            print(f'{espacos}{v_atual}-{vz}')
        
n = int(input())

for ct in range(n):
    v, a = map(int, input().split())
    visitados = [0] * v
    grafo = [[] for _ in range(v)] # Cria a lista de adjacências
    
    for _ in range(a):
        a, b = map(int, input().split())
        if b not in grafo[a]:
            grafo[a].append(b) # Cria uma aresta
    
    for linha in grafo:
        linha.sort()
    
    print(f'Caso {ct+1}:')
    for i in range(v):
        if visitados[i] == 0 and len(grafo[i]) != 0:
            dfs(i, grafo, 1)
            print()  