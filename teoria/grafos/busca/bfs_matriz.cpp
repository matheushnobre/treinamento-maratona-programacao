#include <bits/stdc++.h> // Inclui todas as bibliotecas padrão do C++. 

#define MAX 505 // Define um valor constante MAX como 505.
using namespace std; // Usa o namespace padrão std.

int M[MAX][MAX]; // Declara uma matriz de adjacência M para o grafo.
int visitados[MAX]; // Declara um array para marcar os vértices visitados.
int V; // Declara uma variável para o número de vértices.

// Função BFS para percorrer o grafo a partir de um vértice de origem.
void bfs(int origem)
{
    queue<int> fila; // Declara uma fila para a BFS.
    fila.push(origem); // Insere o vértice de origem na fila.
    visitados[origem] = 1; // Marca o vértice de origem como visitado.

    while (!fila.empty()) // Enquanto a fila não estiver vazia.
    {
        int v_atual = fila.front(); // Pega o vértice na frente da fila.
        fila.pop(); // Remove o vértice da fila.

        printf("Visitando vertice %d\n", v_atual); // Imprime o vértice sendo visitado.

        for (int vz = 0; vz <= V; vz++) // Itera por todos os vértices.
            if (visitados[vz] == 0 and M[v_atual][vz] == 1) // Se o vértice vz não foi visitado e é adjacente ao vértice atual.
            {
                fila.push(vz); // Adiciona o vértice vz à fila.
                visitados[vz] = 1; // Marca o vértice vz como visitado.
            }
    }
}

int main()
{
    int A; // Declara uma variável para o número de arestas.
    memset(M, 0, sizeof(M)); // Inicializa a matriz de adjacência M com zeros.
    memset(visitados, 0, sizeof(visitados)); // Inicializa o array de visitados com zeros.
    scanf("%d%d", &V, &A); // Lê o número de vértices e arestas.
    int v1, v2, peso; // Declara variáveis para ler as arestas.

    for (int k = 0; k < A; k++) // Loop para ler todas as arestas.
    {
        scanf("%d%d", &v1, &v2); // Lê uma aresta entre v1 e v2.
        M[v1 - 1][v2 - 1] = 1; // Marca a aresta na matriz de adjacência.
        M[v2 - 1][v1 - 1] = 1; // Marca a aresta na matriz de adjacência (grafo não direcionado).
    }

    bfs(0); // Chama a BFS a partir do vértice 0.

    for (int i = 0; i < V; i++) // Loop para imprimir os vértices visitados.
        printf("%d ", visitados[i]); // Imprime o array de visitados.

    return 0; // Retorna 0 para indicar que o programa terminou com sucesso.
}
