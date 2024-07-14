#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

int distancia(int origem, int destino, int proibido, vvi grafo, int numVertices){
    vi visitados(numVertices, 0);
    visitados[origem] = 1;
    vi distancias(numVertices, -1);
    distancias[origem] = 0;
    queue<int> fila;
    fila.push(origem);

    while (!fila.empty()){
        int v_atual = fila.front();
        fila.pop();

        for (int vizinho : grafo[v_atual]){
            if(visitados[vizinho] == 0 and vizinho != proibido){
                visitados[vizinho] = 1;
                distancias[vizinho] = distancias[v_atual] + 1;
                fila.push(vizinho);
                if (vizinho == destino)
                    return distancias[vizinho];
            }
        }
    }
    return 0;
}

int main(){
    int n, m, a, b, c, r, e; 
    // n = número de vértices, m = número de arestas
    // a, b para ler cidades que são ligadas por uma aresta
    // c = cidade de origem, r = cidade de destino, e = cidade proibida
    while(scanf("%d %d", &n, &m) != EOF){
        vvi grafo(n);
        for(int i=0; i<m; i++){
            cin>>a>>b;
            grafo[a-1].emplace_back(b-1);
            grafo[b-1].emplace_back(a-1);
        }
        cin>>c>>r>>e;
        cout<<distancia(c-1, r-1, e-1, grafo, n)<<endl;
    }
}