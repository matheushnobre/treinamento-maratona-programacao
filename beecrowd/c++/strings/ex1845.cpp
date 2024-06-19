#include <iostream>
#include <unordered_set>
#include <string>
#include <cstdio>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    unordered_set<char> consoantes = {'f', 'x', 'j', 'p', 's', 'v', 'b', 'z'};
    unordered_set<char> consoantes_maiusculas = {'F', 'X', 'J', 'P', 'S', 'V', 'B', 'Z'};
    
    string linha;
    while (getline(cin, linha)) {
        string resultado;
        bool ultimoF = false;

        for (char c : linha) {
            if (consoantes.count(c)) {
                if (!ultimoF) {
                    resultado += 'f';
                    ultimoF = true;
                }
            } else if (consoantes_maiusculas.count(c)) {
                if (!ultimoF) {
                    resultado += 'F';
                    ultimoF = true;
                }
            } else {
                resultado += c;
                ultimoF = false;
            }
        }

        cout << resultado << endl;
    }

    return 0;
}
