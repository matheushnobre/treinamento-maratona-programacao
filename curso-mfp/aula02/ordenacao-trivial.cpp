#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
    // lendo a entrada
    cout << "Digite o tamanho do vetor: ";
    int n;
    cin >> n;
    
    vector<int> v(n);
    cout << "Digite os elementos do vetor: ";
    for (int i = 0; i < n; ++i)
        cin >> v[i];

    // ordenando com bubble sort
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n-1; j++){
            if (v[j] > v[j+1]){
                swap(v[j], v[j+1]);
            }
        }
    }

    // imprimindo a saída
    cout << "Vetor ordenado com BubbleSort: ";
    for (int i = 0; i < n; ++i){
        cout << v[i] << " ";
    }
    cout << endl;

    // ordenando com selection sort
    for (int inicio = 0; inicio < n; inicio++) {
        int indexMenor = inicio;
        for (int j = inicio+1; j < n; j++){
            if (v[j] < v[indexMenor]){
                indexMenor = j;
            }
        }
        swap(v[inicio], v[indexMenor]);
    }

    // imprimindo a saída
    cout << "Vetor ordenado com SelectionSort: ";
    for (int i = 0; i < n; ++i){
        cout << v[i] << " ";
    }
    cout << endl;


    return 0;
}