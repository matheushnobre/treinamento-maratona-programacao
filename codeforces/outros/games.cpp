#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, qtd=0;
    cin>>n;
    int matriz[n][2];

    for(int i=0; i<n; i++){
        cin>>matriz[i][0]>>matriz[i][1];
    }

    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            if(i!=j and matriz[i][0] == matriz[j][1])
                qtd++;
        
    cout<<qtd<<endl;

    return 0;
}