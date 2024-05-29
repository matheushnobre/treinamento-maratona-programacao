#include <iostream>
#include <cstdio>
#include <string>

using namespace std;
 
int main() {
    double distancia=0;
    int numAmigos=0;
    string nome;

    while(getline(cin, nome)){
        int valor;
        cin>>valor;
        cin.ignore();

        distancia += valor;
        numAmigos++;
    }

    double saida = distancia / numAmigos;
    printf("%.1f\n", saida);

    return 0;
}