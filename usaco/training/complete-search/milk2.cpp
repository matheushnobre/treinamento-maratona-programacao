/*
ID: matheus30
TASK: milk2
LANG: C++                 
*/             

#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("milk2.in", "r", stdin);
    freopen("milk2.out", "w", stdout);

    int n, a, b, ordenha=0, naoOrdenha=0, inicio, fim;
    vector<pair<int, int>> entradas;

    cin>>n;
    for (int i=0; i<n; i++){
        cin>>a>>b;
        entradas.push_back({a, b});
    }

    sort(entradas.begin(), entradas.end());
    ordenha = entradas[0].second - entradas[0].first;
    inicio = entradas[0].first;
    fim = entradas[0].second;

    int i=1;
    while (i<n){
        if(entradas[i].first <= fim){
            fim = max(fim, entradas[i].second);
        }
        else{
            ordenha = max(ordenha, fim - inicio);
            naoOrdenha = max(naoOrdenha, entradas[i].first - fim);
            inicio = entradas[i].first;
            fim = entradas[i].second;
        }
        i++;
    }

    std::cout<<ordenha<<" "<<naoOrdenha<<endl;

    return 0;
}
