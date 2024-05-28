#include <iostream>
using namespace std;

int main(){
    int t, n;
    cin>>t;
    
    for(int ct=1; ct<=t; ct++){
        cin>>n;
        int vetor[n];
        for(int i=0; i<n; i++){
            int valor;
            cin>>valor;
            vetor[i] = valor;
        }
        cout<<"Case "<<ct<<": "<<vetor[n/2]<<endl;
    }

    return 0;
}