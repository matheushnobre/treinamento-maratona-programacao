#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n, m;

    while (scanf("%d %d", &n, &m) != EOF){
        vector<int> modelos;
        for (int i=0; i<n; i++){
            int valor;
            cin>>valor;
            modelos.push_back(valor);
        }
        
        //Ordenando o vetor
        for (int i=1; i<n; i++){
            int valorAtual = modelos[i];
            int posicao = i;

            while (posicao>0 && modelos[posicao-1] < valorAtual){
                modelos[posicao] = modelos[posicao-1];
                posicao -= 1;
            }

            modelos[posicao] = valorAtual;
        }

        int valor=0;
        for(int i=0; i<m; i++){
            valor += modelos[i];
        }
        cout<<valor<<endl;
    }

    return 0;
}