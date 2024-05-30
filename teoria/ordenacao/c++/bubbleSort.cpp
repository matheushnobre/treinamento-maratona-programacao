#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
    // lendo a entrada
    cout << "Digite o tamanho do vetor: ";
    int n;
    cin >> n;
    
    vector<int> vetor(n);
    cout << "Digite os elementos do vetor: ";
    for (int i = 0; i < n; ++i)
        cin >> vetor[i];

    // ordenando com bubble sort
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n-1; j++){
            if (vetor[j] > vetor[j+1]){
                swap(vetor[j], vetor[j+1]);
            }
        }
    }

    // imprimindo a saída
    cout << "Vetor ordenado com BubbleSort: ";
    for (int i = 0; i < n; ++i){
        cout << vetor[i] << " ";
    }
    cout << endl;

    return 0;
}