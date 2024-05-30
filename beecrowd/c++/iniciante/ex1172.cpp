#include <iostream>

using namespace std;

int main(){
    int vetor[10];
    int valor;
    
    for (int i=0; i<10; i++){
        scanf("%d", &valor);
        if (valor <= 0){
            valor = 1;
        }
        vetor[i] = valor;
    }
    
    for (int i=0; i<10; i++){
        cout<<"X["<<i<<"] = "<<vetor[i]<<endl;;
    }

    return 0;
}
