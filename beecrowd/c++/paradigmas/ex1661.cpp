#include <bits/stdc++.h>
using namespace std;

#define MAX 100000

int main(){
    int n;
    int vetor[MAX];

    while(true){
        cin>>n;
        if(n==0){
            break;
        }

        for(int i=0; i<n; i++){
            cin>>vetor[i];
        }

        unsigned long long int saida=0;
        for(int i=1; i<n; i++){
            vetor[i] += vetor[i-1];
            saida += abs(vetor[i-1]);
        }

        cout<<saida<<endl;
    }


    return 0;
}