#include <bits/stdc++.h>
using namespace std;

int gemeos[1000001];

bool isPrime(int n){
    if(n<=1) return false;
    else if(n==2) return true;
    int i=3;
    while(i*i<=n){
        if(n%i==0) return false;
        i+=2;
    }
    return true;
}

void qtdgemeos(){
    int ultimoPrimo = 3;
    for(int i=3; i<=1000000; i+=2){
        if (isPrime(i)){
            if(ultimoPrimo==i-2){
                gemeos[i-2] = gemeos[i-3]+1;
                gemeos[i-1] = gemeos[i-2];
                gemeos[i] = gemeos[i-1]+1;
            }
            else{
                gemeos[i-1] = gemeos[i-2];
                gemeos[i] = gemeos[i-1];
            }
            ultimoPrimo = i;
        }
        else{
            gemeos[i-1] = gemeos[i-2];
            gemeos[i] = gemeos[i-1];
        }
    }
}

int main(){
    memset(gemeos, 0, sizeof(gemeos));
    qtdgemeos();
    int n, x, y;
    cin>>n;
    while(n){
        cin>>x>>y;
        int maior = max(x, y);
        int menor = min(x, y);
        cout<<gemeos[maior]-gemeos[menor-1]<<endl;
        n--;
    }

    return 0;
}