#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int nc, populacao;
    cin>>nc;
    while(nc){
        cin>>populacao;
        vector<short int> alturas;
        short int leitura;
        for(int i=0; i<populacao; i++){
            cin>>leitura;
            alturas.push_back(leitura);
        }

        sort(alturas.begin(), alturas.end());
        for (int i=0; i<populacao; i++){
            cout<<alturas[i];
            if(i !=populacao-1)
                cout<<" ";
        }
        cout<<endl;
        nc--;
    }
}
