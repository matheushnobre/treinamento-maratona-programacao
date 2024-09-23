#include <bits/stdc++.h>
using namespace std;

#define MAX 200001

int main(){
    int t, n;
    long long vetor[MAX];

    cin>>t;
    for(int ct=0; ct<t; ct++){
        cin>>n;
        for(int i=0; i<n; i++){
            cin>>vetor[i];
        }

        long long valor = vetor[n-2];
        for(int j=n-3; j>=0; j--){
            valor = valor - vetor[j];
        }
        
        valor = vetor[n-1] - valor;
        cout<<valor<<endl;
    }


    return 0;
}