#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int dij(int origem, int numVertices, vector<vii>lista){
    const int INF = 1e9;
    priority_queue<ii, vector<ii>, greater<ii>> fila_prioridade;
    fila_prioridade.push({0, origem});
    vi distancias(numVertices, INF);
    distancias[origem] = 0;

    while (!fila_prioridade.empty()){
        int dist = fila_prioridade.top().first;
        int v_atual = fila_prioridade.top().second;
        fila_prioridade.pop();

        if(dist > distancias[v_atual])
            continue;

        for (ii v : lista[v_atual]){
            int peso = v.second;
            int vz = v.first;
            if(distancias[v_atual] + peso >= distancias[vz])
                continue;
            distancias[vz] = distancias[v_atual] + peso;
            fila_prioridade.push({distancias[vz], vz});
        }
    }

    int menor, maior=0;
    if (distancias[0] !=0) 
        menor = distancias[0];
    else
        menor = distancias[1];
    for (int u=0; u<numVertices; u++){
        if(distancias[u] < menor && distancias[u] > 0)
            menor = distancias[u];
        if(distancias[u] > maior)
            maior = distancias[u];
    }

    return maior - menor;

}

int main(){
    int n, m, u, v, p, s;
    cin>>n>>m;

    vector<vii> lista(n, vii());
    for(int i=0; i<m; i++){
        cin>>u>>v>>p;
        lista[u-1].emplace_back(v-1, p);
        lista[v-1].emplace_back(u-1, p);
    }

    cin>>s;

    cout<<dij(s-1, n, lista)<<endl;

    return 0;
}