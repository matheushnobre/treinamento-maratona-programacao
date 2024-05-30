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

    // ordenando com insertion sort
    for (int step = 1; step < n; step++) {
        int key = vetor[step];
        int j = step - 1;

        while (key < vetor[j] && j>=0){
            vetor[j+1] = vetor[j];
            j--;
        }
        vetor[j+1] = key;
    }

    // imprimindo a saída
    cout << "Vetor ordenado com InsertionSort: ";
    for (int i = 0; i < n; ++i){
        cout << vetor[i] << " ";
    }
    cout << endl;

    return 0;
}