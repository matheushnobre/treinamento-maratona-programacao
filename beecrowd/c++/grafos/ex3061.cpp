#include <bits/stdc++.h>
using namespace std;

int mapa[1000][1000];
int n, m;

int auxi[4] = {-1, 1, 0, 0};
int auxj[4] = {0, 0, -1, 1};

bool isValid(int i, int j){
    if(i >=0 && i<n && j>=0 && j<m)
        return mapa[i][j] == 1;
    return false;
}

void bfs(int i, int j){
    mapa[i][j] = 2;
    queue<pair<int, int>> fila;
    fila.push({i, j});

    while (!fila.empty()){
        i = fila.front().first, j = fila.front().second;
        fila.pop();

        for(int x=0; x<4; x++){
            if(isValid(i + auxi[x], j + auxj[x])){
                mapa[i + auxi[x]][j + auxj[x]] = 2;
                fila.push({i + auxi[x], j + auxj[x]});
            }    
        }
    }
}

int main(){
    int manchas = 0;
    cin>>n>>m;

    for (int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            cin>>mapa[i][j];

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (mapa[i][j] == 1){
                bfs(i, j);
                manchas++;
            }
        }
    }

    cout<<manchas<<endl;

    return 0;
}