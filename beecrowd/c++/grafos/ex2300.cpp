#include <bits/stdc++.h> 
using namespace std;

int matriz[100][100];
int visitados[100];
int v;

void bfs(int origem){
    queue<int> fila;
    fila.push(origem);
    visitados[origem] = 1;

    while(!fila.empty()){
        int v_atual = fila.front();
        fila.pop();

        for (int vz=0; vz <= v; vz++){
            if (visitados[vz] == 0 and matriz[v_atual][vz] == 1){
                fila.push(vz);
                visitados[vz] = 1;
            }
        }
    }
}

int main(){
    int ct = 0;
    int e, l;
    cin>>e>>l;
    do{
        ct++;
        memset(matriz, 0, sizeof(matriz)); 
        memset(visitados, 0, sizeof(visitados));
        v = e;

        for(int i=0; i<l; i++){
            int x, y;
            cin>>x>>y;
            matriz[x-1][y-1] = 1;
            matriz[y-1][x-1] = 1;
        }

        bfs(0);
        bool falha = false;
        for(int i=0; i<v; i++){
            if(visitados[i] == 0) 
                falha = true;
        }

        cout<<"Teste "<<ct<<endl;
        if(falha)
            cout<<"falha"<<endl;
        else   
            cout<<"normal"<<endl;

        cout<<endl;
        cin>>e>>l;

    } while(e != 0 && l != 0);

}