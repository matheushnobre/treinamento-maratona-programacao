#include <iostream>

using namespace std;

int main() {
    int valor;
    int qtd = 0;
    for (int i=0; i<5; i++){
        cin>>valor;
        if (valor % 2 == 0){
            qtd++;
        }
    }
    cout<<qtd<<" valores pares"<<endl;
}