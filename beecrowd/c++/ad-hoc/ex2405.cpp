#include <bits/stdc++.h>
using namespace std;

int grafo[200][200];
int n, m;
int xaux[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
int yaux[8] = {-1, -1, -1, 0, 0, 1, 1, 1};

bool isValid(int x, int y){
    if(x>=0 && x<n && y>=0 && y<m)
        return grafo[x][y] == 0;
    return false;
}

int colorir(int x, int y){
    int q=1;
    queue<pair<int, int>> fila;
    fila.push({x, y});
    grafo[x][y] = 1;

    while (!fila.empty()){
        pair<int, int> par = fila.front();
        x = par.first;
        y = par.second;
        fila.pop();

        for (int i=0; i<8; i++){
            int c = x + xaux[i];
            int d = y + yaux[i];
            if(isValid(c, d)){
                fila.push({c, d});
                grafo[c][d] = 1;
                q += 1;
            }
        }
    }
    
    return q;
}

int main(){
    int x, y, k, a, b;
    cin>>n>>m>>x>>y>>k;
    memset(grafo, 0, sizeof(grafo)); 

    for (int i=0; i<k; i++){
        cin>>a>>b;
        grafo[n-a][b-1] = 2;
    }

    cout<<colorir(n-x, y-1)<<endl;

    return 0;
}