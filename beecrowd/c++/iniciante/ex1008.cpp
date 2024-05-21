#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int numero, horas;
    float valor, salario;

    cin >> numero >> horas >> valor;
    salario = valor * horas;

    printf("NUMBER = %d\n", numero);
    printf("SALARY = U$ %.2f\n", salario);
    return 0;
}