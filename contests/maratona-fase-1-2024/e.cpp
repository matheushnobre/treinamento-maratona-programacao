#include <bits/stdc++.h>
using namespace std;

#define MAX 50

int main(){
    int n, saida;
    int matriz[MAX][MAX];
    
    cin>>n;
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            cin>>matriz[i][j];

    int m1 = min(matriz[0][0], matriz[0][n-1]);
    int m2 = min(matriz[n-1][0], matriz[n-1][n-1]);
    int menor = min(m1, m2);

    if (menor == matriz[0][0])
        saida = 0;
    else if (menor == matriz[0][n-1])
        saida = 1;
    else if (menor == matriz[n-1][n-1])
        saida = 2;
    else   
        saida = 3;

    cout<<saida<<endl;

    return 0;
}