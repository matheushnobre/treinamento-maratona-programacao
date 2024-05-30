#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main(){
    int n, tam, valor, menorElevacao=-1, idTrilha;
    vector<int> trilha;
    cin>>n;

    for(int i=0; i<n; i++){
        cin>>tam;
        trilha.clear();
        for(int j=0; j<tam; j++){
            cin>>valor;
            trilha.push_back(valor);
        }
 
        int elevacao = 0;
        for (int cont=0; cont<tam-1; cont++){
            if (trilha[cont] < trilha[cont+1]){
                elevacao += (trilha[cont+1] - trilha[cont]);
            }
        }

        if (menorElevacao == -1){
            menorElevacao = elevacao;
            idTrilha = i+1;
        }

        if (elevacao < menorElevacao){
            menorElevacao = elevacao;
            idTrilha = i+1;
        }

        elevacao = 0;
        for(int cont=tam-1; cont>0; cont--){
            if (trilha[cont] < trilha[cont-1]){
                elevacao += (trilha[cont-1] - trilha[cont]);
            }
        }

        if (elevacao < menorElevacao){
            menorElevacao = elevacao;
            idTrilha = i+1;
        }

    }

    cout<<idTrilha<<endl;

    return 0;
}