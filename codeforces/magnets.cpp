#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, qtd=0;
    string polo;
    char last='*';
    cin>>n;

    for(int i=0; i<n; i++){
        cin>>polo;
        if(polo[0]!=last){
            last=polo[0];
            qtd++;
        }
    }

    cout<<qtd;

    return 0;
}