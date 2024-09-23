#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, s=0;
    string entrada;
    cin>>n;
    cin>>entrada;

    for(int i=1; i<n; i++){
        if(entrada[i] == entrada[i-1])
            s+=1;
    }

    cout<<s<<endl;

    return 0;
}