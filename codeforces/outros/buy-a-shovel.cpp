#include <bits/stdc++.h>
using namespace std;

int main(){
    int k, r, qtd=1;
    cin>>k>>r;

    while (true){
        if((k*qtd)%10==0) break;
        else if((k*qtd)%10==r) break;
        qtd+=1;
    }

    cout<<qtd<<endl;

    return 0;
}