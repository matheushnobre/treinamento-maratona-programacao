#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    int n, m;
    int maior=0;
    cin>>n>>m;
    int campo[n][m];

    for (int i=0; i<n; i++){
        for (int j=0; j<m; j++){
            cin>>campo[i][j];
        }
    }

    // Verificando linhas
    for (int i=0; i<n; i++){
        int valor=0;
        for (int j=0; j<m; j++){
            valor += campo[i][j];
        }
        if (valor > maior){
            maior = valor;
        }
    }

    // Verificando colunas
    for (int j=0; j<m; j++){
        int valor=0;
        for (int i=0; i<n; i++){
            valor += campo[i][j];
        }
        if (valor > maior){
            maior = valor;
        }
    }

    cout<<maior<<endl;

    return 0;
}