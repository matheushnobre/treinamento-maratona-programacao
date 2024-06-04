#include <bits/stdc++.h>
using namespace std;

int buscaBinaria(vector<int> vetor, int item) {
    int inicio = 0;
    int fim = vetor.size() - 1;

    while (inicio <= fim) {
        int m = inicio + (fim - inicio) / 2;

        if (vetor[m] == item)
            return m;
        else if (vetor[m] < item)
            inicio = m + 1;
        else
            fim = m - 1;
    }

    return -1;
}

int main() {
    vector<int> vetor = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89};
    int item = 13;

    int resultado = buscaBinaria(vetor, item);

    if (resultado != -1)
        cout << "Elemento encontrado no indice: " << resultado << endl;
    else
        cout << "Elemento nao encontrado." << endl;

    return 0;
}
