#include <bits/stdc++.h>
using namespace std;

#define MAX 1000000

int lis(int vetor[MAX], int n){
    int s[MAX];
    s[0] = vetor[0];
    int tam = 1;

    for(int i=1; i<n; i++){
        if(vetor[i]>s[tam-1]){
            s[tam] = vetor[i];
            tam+=1;
        }
        else{
            int inicio=0, fim=tam-1;
            while(inicio < fim){
                int meio = inicio + (fim - inicio) / 2;
                if(s[meio] < vetor[i])
                    inicio = meio+1;
                else
                    fim = meio;
            }
            s[inicio] = vetor[i];
        }
    }
    return tam;
}

int main(){
    int n;
    int vetor[MAX];
    while(cin>>n){
        for(int i=0; i<n; i++)
            cin>>vetor[i];
        cout<<lis(vetor, n)<<endl;
    }
    return 0;
}
