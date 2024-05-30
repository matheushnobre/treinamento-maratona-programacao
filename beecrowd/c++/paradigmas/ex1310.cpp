#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main(){
    int n;

    while (scanf("%d", &n) != EOF){
        int custoPorDia;
        int maiorLucro = 0;
        vector<int> receitas;
        cin>>custoPorDia;
        
        for (int i=0; i<n; i++){
            int valor;
            cin>>valor;
            receitas.push_back(valor);
        }

        for (int i=0; i<n; i++){
            int lucro = 0;
            for (int j=i; j<n; j++){
                lucro += receitas[j] - custoPorDia;
                if (lucro > maiorLucro){
                    maiorLucro = lucro;
                }
            }
        }

        cout<<maiorLucro<<endl;
    }


    return 0;
}