#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    for (int i=0; i<t; i++){
        int n;
        cin>>n;
        int saida[n];
        char c;
        for(int j=0; j<n; j++){
            for(int k=0; k<4; k++){
                cin>>c;
                if (c == '#')
                    saida[n-j-1] = k+1;
            }
        }
        for(int j=0; j<n; j++){
            cout<<saida[j]<<" ";
        }
        cout<<endl;
    }

    return 0;
}