// Este código gera o menor caminho entre dois atores, porém está dando Memory Limit Exceeded.
// Como o caminho retornado pode ser qualquer um, não necessariamente o menor, irei fazer uma nova implementação.

#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define MAXM 1000000
 
pair<int, vii> bfs(int origem, int destino, vector<vii> grafo, int vertices){
    vector<int> visitados(vertices, 0);
    vector<int> distancias(vertices, -1);
    vii veioDeOnde(vertices);
    distancias[origem] = 1;
    visitados[origem] = 1;
    veioDeOnde[origem];
    queue<int> fila;
    fila.push(origem);
 
    while(!fila.empty()){
        int v_atual = fila.front();
        fila.pop();
 
        for (ii vz : grafo[v_atual]){
            if(visitados[vz.first] == 0){
                visitados[vz.first] = 1;
                fila.push(vz.first);
                distancias[vz.first] = distancias[v_atual] + 1;
                veioDeOnde[vz.first] = {v_atual, vz.second};
            }
        }
    }
 
    return {distancias[destino], veioDeOnde};
}
 
int main(){
    int n, m, ni, q, x, y;
    int atores[MAXM];
    cin>>n>>m;
 
    vector<vii> grafo(m+1);
 
    for(int i=0; i<n; i++){
        cin>>ni;
        for(int j=0; j<ni; j++)
            cin>>atores[j];
 
        for(int j=0; j<ni; j++){
            for(int k=j+1; k<ni; k++){
                grafo[atores[j]].emplace_back(atores[k], i+1);
                grafo[atores[k]].emplace_back(atores[j], i+1);
            }
        }
    }
 
    cin>>q;
    for(int i=0; i<q; i++){
        cin>>x>>y;
        pair<int, vii> s = bfs(x, y, grafo, m+1);
        int d = s.first;
        vii veioDeOnde = s.second;
        cout<<d<<endl;
        if(d != -1){
            vector<int> caminho;
            vector<int> filmes;
            caminho.emplace_back(y);
            while (y != x){
                int temp = veioDeOnde[y].first;
                int f = veioDeOnde[y].second;
                y = temp;
                caminho.emplace_back(y);
                filmes.emplace_back(f);
            }
            for(int k=caminho.size()-1; k>=0; k--){
                cout<<caminho[k]<<" ";
                if (k!=0)
                    cout<<filmes[k-1]<<" ";
            }
            cout<<endl;
        }
    }

    return 0;
}