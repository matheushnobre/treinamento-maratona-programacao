#include <bits/stdc++.h>
using namespace std;

int matriz[5][5];
int ai[4] = {-1, 1, 0, 0};
int aj[4] = {0, 0, -1, 1};

bool isValid(int i, int j){
    if(i>=0 && i<5 && j>=0 && j<5)
        return matriz[i][j] == 0;
    return false;
}

bool labirinto(){
    queue<pair<int, int>> fila;
    fila.push({0, 0});

    while(!fila.empty()){
        int i = fila.front().first, j = fila.front().second;
        fila.pop();

        if(i==4 && j==4)
            return true;

        for(int c=0; c<4; c++){
            int a = i+ai[c], b = j + aj[c];
            if(isValid(a, b)){
                matriz[a][b] = 1;
                fila.push({a, b});
            }
        } 
    }

    return false;
}

int main(){
    int n;
    cin>>n;
    for(int ct=0; ct<n; ct++){

        for(int i=0; i<5; i++)
            for(int j=0; j<5; j++)
                cin>>matriz[i][j];

        if(labirinto())
            cout<<"COPS"<<endl;
        else
            cout<<"ROBBERS"<<endl;
    }

    return 0;
}