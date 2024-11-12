#include <bits/stdc++.h>
using namespace std;

int main(){
    int t, n;
    long long int v;
    cin>>t;
    for(int i=0; i<t; i++){
        int answer=0;
        cin>>n;
        vector<int> lista;
        for(int i=0; i<n; i++){
            cin>>v;
            lista.push_back(v);
        }
        
        for(int i=0; i<n; i++){
            int contador=0;
            for(int j=i; j<n; j++){
                if(lista[j] <= lista[i]){
                    contador++;
                }
            }
            answer = max(contador, answer);
        }
        cout<<n-answer<<endl;
    }


    return 0;
}