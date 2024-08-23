#include <bits/stdc++.h>
using namespace std;

int couting[201];

int main(){
    int c = 0, n;
    long long tconsumo, tpessoas; 
    while (true) {
        c += 1;
        if (c != 1) cout << endl;
        cin >> n;
        if (n == 0) break;

        tconsumo = 0, tpessoas = 0;
        memset(couting, 0, sizeof(couting)); 

        for (int i = 0; i < n; i++) {
            int x, y;
            cin >> x >> y;
            int con = y / x;
            tconsumo += y;
            tpessoas += x;
            couting[con] += x;
        }

        double cm = static_cast<double>(tconsumo) / tpessoas; 

        cout << "Cidade# " << c << ":" << endl; 
        int aux = 0;

        for (int j = 0; j <= 200; j++) {
            int v = couting[j];
            if (v != 0) {
                cout<<v<<"-"<<j<<" ";
                aux += v;
            }
            if (aux == tpessoas) break;
        }
        cout<<endl;
        cout << fixed << setprecision(2) << "Consumo medio: " << floor(cm * 100) / 100 << " m3.";
    }

    return 0;
}
