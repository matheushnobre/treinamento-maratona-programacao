// Tentativa de resolver o problema por completo
// Tempo Limite Excedido

#include <bits/stdc++.h>
using namespace std;

#define MAX 100001

int main(){
    long long n, k, c=1;
    long long vetor[MAX];
    long long saida[MAX] = {0};
    int faltam[MAX];
    queue<int> fila;
    fila.push(0);
    saida[0] = 1;


    cin>>n>>k;
    for(int i=0; i<n; i++){
        cin>>vetor[i];
        faltam[i] = i;
    }

    swap(faltam[0], faltam[n-c]);
    c++;

    while(!fila.empty()){
        int i = fila.front();
        fila.pop();
        if(saida[i] == 1){
            int j=0;
            while (j<=n-c){
                if (abs(vetor[faltam[j]]-vetor[i])<=k && faltam[j]>i){
                    saida[faltam[j]] = 1;
                    fila.push(faltam[j]);
                    swap(faltam[j], faltam[n-c]);
                    c++;
                } else{
                    j++;
                } 
            }
        }
    }

    for(int i=0; i<n; i++){
        cout<<saida[i]<<" ";
    }

    return 0;
}