INF = int(1e9)  # Define uma constante para representar infinito (1 bilhão)
V = None  # Inicializa a variável V, que irá armazenar o número de vértices
visitados = []  # Inicializa a lista de visitados como vazia
M = []  # Inicializa a matriz de adjacência como vazia

def dfs(v_atual):  # Define a função DFS que recebe o vértice atual como parâmetro
    visitados[v_atual] = 1  # Marca o vértice atual como visitado
    print('Visitando o vertice %d' % v_atual)  # Imprime o vértice atual sendo visitado

    for vz in range(V+1):  # Itera sobre todos os possíveis vértices
        if visitados[vz] == INF and M[v_atual][vz] == 1:  # Se o vizinho não foi visitado e há uma aresta
            visitados[vz] = 1  # Marca o vizinho como visitado
            dfs(vz)  # Chama recursivamente a DFS para o vizinho

L = input().split()  # Lê a primeira linha de entrada e divide em uma lista de strings
V, A = int(L[0]), int(L[1])  # Converte os dois primeiros elementos da lista para inteiros, V (número de vértices) e A (número de arestas)
M = [[0 for i in range(V+1)] for j in range(V+1)]  # Inicializa a matriz de adjacência com zeros
visitados = [INF] * (V+1)  # Inicializa a lista de visitados com infinito para cada vértice

for i in range(A):  # Loop para ler todas as arestas
    L = input().split()  # Lê uma linha de entrada e divide em uma lista de strings
    A, B = int(L[0]) - 1, int(L[1]) - 1  # Converte os elementos da lista para inteiros e ajusta para índice zero
    M[A][B] = 1  # Adiciona uma aresta na matriz de adjacência
    M[B][A] = 1  # Adiciona a aresta na direção oposta (grafo não-direcionado)

dfs(0)  # Chama a função DFS a partir do vértice 0
print(visitados)  # Imprime a lista de vértices visitados
