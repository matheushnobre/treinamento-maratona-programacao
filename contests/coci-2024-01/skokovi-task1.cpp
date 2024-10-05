// Resolve a 1º task do problema

#include <bits/stdc++.h>
using namespace std;

#define MAX 200001

int main(){
    long long n, k;
    long long vetor[MAX];
    long long saida[MAX] = {0};
    saida[0] = 1;

    cin>>n>>k;
    for(int i=0; i<n; i++){
        cin>>vetor[i];
    }

    for(int i=1; i<n; i++){
        if(vetor[i] - vetor[i-1] <= k){
            saida[i] = 1;
        } else{
            break;
        }
    }

    for(int i=0; i<n; i++){
        cout<<saida[i]<<" ";
    }

    return 0;
}