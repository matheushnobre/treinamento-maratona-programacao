#include <bits/stdc++.h>
using namespace std;

#define MAX 100000

int o, d, k;
int cp[100];

int visitados[MAX+1];
int distancias[MAX+1];

bool isProibido(int b){
    for (int i=0; i<k; i++)
        if (cp[i] == b)
            return true;
    return false;
}

int botao(int v, int i){
    switch(i){
        case 0: if(v-1>0) return v-1;
        case 1: if(v+1<=MAX) return v+1;
        case 2: if(v%2==0) return v/2;
        case 3: if(v*2<=MAX) return v*2;
        case 4: if(v*3<=MAX) return v*3;
    }
    return v;
}

int bfs(){
    memset(visitados, 0, sizeof(visitados));
    visitados[o] = 1;
    queue<int> fila;
    fila.push(o);
    
    memset(distancias, -1, sizeof(distancias));
    distancias[o] = 0;

    while(!fila.empty()){
        int atual = fila.front();
        fila.pop();

        for(int i=0; i<5; i++){
            int b = botao(atual, i);
            if(visitados[b] == 0 && !isProibido(b)){
                visitados[b] = 1;
                distancias[b] = distancias[atual] + 1;
                fila.push(b);
                if(b == d)
                    return distancias[b];
            }
        }
    }

    return -1;
}

int main(){
    while(true){
        cin>>o>>d>>k;
        if(o==0) break;

        if(k!=0)
            for(int i=0; i<k; i++)
                cin>>cp[i];

        cout<<bfs()<<endl;
    }

    return 0;
}