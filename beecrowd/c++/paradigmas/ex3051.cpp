#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, k, i=0, j=0, soma, valor;
    long r=0;
    cin>>n>>k;
    int vetor[n];
    int sum[n];
    map<int, int> hashmap;
    hashmap[0] = 1;

    for(int i=0; i<n; i++){
        cin>>valor;
        vetor[i] = valor;
        if(i==0) sum[i] = valor;
        else sum[i] = sum[i-1] + valor;
    }
        
    
    for(int i=0; i<n; i++){
        if(hashmap.count(sum[i]-k)==1)
            r+=hashmap[sum[i]-k];
        if(hashmap.count(sum[i])==1)
            hashmap[sum[i]] += 1;
        else
            hashmap[sum[i]] = 1;
    }

    cout<<r<<endl;
    return 0;
}