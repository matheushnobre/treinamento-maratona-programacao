#include <bits/stdc++.h>
using namespace std;

int main(){
    long long t, n, m;
    cin >> t;
    for(int ct = 0; ct < t; ct++){
        cin >> n >> m;
        vector<vector<int>> jogadas(n, vector<int>(m));

        // Entrada das jogadas
        for(long long i = 0; i < n; i++){
            for(long long j = 0; j < m; j++){
                cin >> jogadas[i][j];
            }
        }

        unsigned long long int total = 0;
        for(long long j = 0; j < m; j++){
            vector<int> coluna(n);
            for(long long i = 0; i < n; i++){
                coluna[i] = jogadas[i][j];
            }

            sort(coluna.begin(), coluna.end());

            for(long long k = 0; k < n; k++){
                total += coluna[k] * k;
                total -= coluna[k] * (n - k - 1);
            }
        }

        cout << total << endl;
    }

    return 0;
}
