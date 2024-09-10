#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("diamond.in", "r", stdin);
    freopen("diamond.out", "w", stdout);
    
    int n, k, v;
    int contagem[10001] = {0};
    cin>>n>>k;

    for(int i=0; i<n; i++){
        cin>>v;
        contagem[v] += 1;
    }

    int soma = 0;
    for(int i=0; i<=k; i++)
        soma += contagem[i];
    int maior = soma;
    
    for(int i=1; i<10001-k; i++){
        soma -= contagem[i-1];
        soma += contagem[i+k];
        maior = max(maior, soma);
    }

    cout<<maior<<endl;

    return 0;
}