#include <bits/stdc++.h>
using namespace std;

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

int main(){
    vector<pair<int, int>> gemeos;
    bool ultimoprimo = false;

    int i=3;
    while (gemeos.size()<10000){
        if(isPrime(i)){
            if(ultimoprimo)
                gemeos.push_back({i-2, i});
            ultimoprimo=true;
        } else ultimoprimo = false;
        i+=2;
    }

    int num;
    vector<int> entradas;
    while(scanf("%d", &num) != EOF)
        entradas.push_back(num);
    
    for(int i=0; i<entradas.size(); i++){
        num = entradas[i];
        cout<<"("<<gemeos[num-1].first<<","<<gemeos[num-1].second<<")"<<endl;
    }
    return 0;
}


