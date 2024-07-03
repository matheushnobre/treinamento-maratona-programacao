INF = int(1e9)  # INF = 1B, usado como valor sentinela para vértices não visitados

def bfs(origem, M, V):
    visitados = [INF] * (V+1)  # Inicializa todos os vértices como não visitados
    visitados[origem] = 1      # Marca o vértice de origem como visitado
    fila = [origem]            # Inicializa a fila de BFS com o vértice de origem

    while len(fila) != 0:      # Enquanto a fila não estiver vazia
        v_atual = fila[0]      # Obtém o primeiro vértice da fila
        del fila[0]            # Remove o primeiro vértice da fila

        print('Visitando o vertice %d' % v_atual)  # Imprime o vértice atual sendo visitado

        for vz in range(V+1):  # Itera sobre todos os vértices vizinhos
            if visitados[vz] == INF and M[v_atual][vz] == 1:  # Se o vizinho não foi visitado e há aresta
                visitados[vz] = 1  # Marca o vizinho como visitado
                fila.append(vz)    # Adiciona o vizinho à fila

    return visitados  # Retorna a lista de vértices visitados

# Leitura de entradas
L = input().split()
V, A = int(L[0]), int(L[1])  # Número de vértices e arestas
M = [[0 for i in range(V+1)] for j in range(V+1)]  # Inicializa a matriz de adjacência

for i in range(A):
    L = input().split()
    A, B = int(L[0])-1, int(L[1])-1  # Lê os vértices das arestas, ajusta para índices baseados em zero
    M[A][B] = 1  # Marca a aresta na matriz de adjacência
    M[B][A] = 1  # Grafo não direcionado, marca a aresta de volta também
    
print(*M, sep='\n')

print(bfs(0, M, V))  # Chama a função BFS a partir do vértice 0 e imprime o resultado
