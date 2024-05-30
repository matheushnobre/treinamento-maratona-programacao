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

    // ordenando com selection sort
    for (int inicio = 0; inicio < n; inicio++) {
        int indexMenor = inicio;
        for (int j = inicio+1; j < n; j++){
            if (vetor[j] < vetor[indexMenor]){
                indexMenor = j;
            }
        }
        swap(vetor[inicio], vetor[indexMenor]);
    }

    // imprimindo a saída
    cout << "Vetor ordenado com SelectionSort: ";
    for (int i = 0; i < n; ++i){
        cout << vetor[i] << " ";
    }
    cout << endl;


    return 0;
}