// Resolve a 2º task do problema

#include <bits/stdc++.h>
using namespace std;

#define MAX 100001

int main(){
    long long n, k;
    long long vetor[MAX];
    long long saida[MAX] = {0};
    saida[0] = 1;

    cin>>n>>k;
    for(int i=0; i<n; i++){
        cin>>vetor[i];
    }

    for(int i=0; i<n; i++){
        if(saida[i] == 1){
            for(int j=i+1; j<n; j++){
                if (abs(vetor[j]-vetor[i])<=k){
                    saida[j] = 1;
                } 
            }
        }
    }

    for(int i=0; i<n; i++){
        cout<<saida[i]<<" ";
    }

    return 0;
}