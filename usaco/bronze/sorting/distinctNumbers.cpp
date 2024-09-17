#include <bits/stdc++.h>
using namespace std;

#define MAX 200000

int main(){
    int n, d=1;
    int v[MAX] = {0};

    cin>>n;
    for(int i=0; i<n; i++)
        cin>>v[i];

    sort(v, v+n);
    for(int i=1; i<n; i++)
        if(v[i] != v[i-1])
            d+=1;

    cout<<d<<endl;

    return 0;
}