#include <iostream>
#include <cctype>
#include <string>

using namespace std;

int main(){
    int n;
    string texto;
    cin>>n;
    cin.ignore();

    for(int i=0; i<n; i++){
        getline(cin, texto);
        int tamanho = texto.size();

        // 1º passada
        int j=0;
        for(int j=0; j<tamanho; j++){
            char c = texto[j];
            if(isalpha(c))
                texto[j] = (c+3);
        }

        // 2º passada
        string invertido = "";
        for(int j=tamanho-1; j>=0; j--)
            invertido += texto[j];
        texto = invertido;

        // 3º passada
        for (int j=tamanho/2; j<tamanho; j++){
            char c = texto[j];
            texto[j] = c-1;
        }
        cout<<texto<<endl;

    }

    return 0;
}