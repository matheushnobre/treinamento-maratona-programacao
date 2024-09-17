#include <bits/stdc++.h>
using namespace std;

bool isValid(int i, int j, int n, int m){
    return (i>=0 && i<n && j>=0 && j<m);
}

int verificarSoma(vector<vector<int>> matriz, int i, int j, int n, int m){
    int soma = matriz[i][j];
    int auxi[4] = {-1, -1, 1, 1};
    int auxj[4] = {-1, 1, -1, 1};
    int novoI = i;
    int novoJ = j;

    for(int a=0; a<4; a++){
        novoI = i;
        novoJ = j;
        while(true){
            novoI = novoI + auxi[a];
            novoJ = novoJ + auxj[a];
            if (isValid(novoI, novoJ, n, m))
                soma += matriz[novoI][novoJ];
            else 
                break;
        }
    }

    return soma;
}

int main(){
    int t, n, m, soma, valor;
    vector<vector<int>> matriz;
    cin >> t;
    for(int ct=0; ct<t; ct++){
        int maior=0;
        cin>>n>>m;
        matriz.clear();
        for(int i=0; i<n; i++){
            vector<int> linha;
            for(int j=0; j<m; j++){
                cin>>valor;
                linha.push_back(valor);
            }
            matriz.push_back(linha);
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                soma = verificarSoma(matriz, i, j, n, m);
                maior = max(maior, soma);
            }
        }

        cout<<maior<<endl;
    }

    return 0;
}