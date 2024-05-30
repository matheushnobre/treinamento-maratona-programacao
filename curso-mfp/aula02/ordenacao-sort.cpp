#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    cout << "Digite o tamanho do vetor: ";
    int n;
    cin >> n;

    vector<int> v(n);
    cout << "Digite os elementos do vetor: ";
    for (int i = 0; i < n; ++i)
        cin >> v[i];


    // ordenando
    sort(v.begin(), v.end());

    // imprimindo a saída
    cout << "Vetor ordenado: ";
    for (int i = 0; i < n; ++i)
        cout << v[i] << " \n"[i+1 == n];

    return 0;
}