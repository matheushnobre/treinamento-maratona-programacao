#include <bits/stdc++.h>
using namespace std;

bool ehPrimo(int n){
    if (n==0 || n==1) return false;
    else if (n==2) return true;

    int i=2;
    while (i*i<=n){
        if (n%i==0) return false;
        i++;
    }

    return true;
}

int main(){
    int n, v;
    vector<int> lista;
    cin>>n;
    
    for(int i=0; i<n; i++){
        cin>>v;
        if (ehPrimo(v)){
            lista.push_back(v);
        }
            
    }

    sort(lista.begin(), lista.end());
    int ant = -1, qtd = 0;
    string saida = "";
    for(int n : lista){
        if(n != ant){
            ant = n;
            qtd++;
            saida += to_string(n) +", ";
        }
    }

    if (!saida.empty()) {
        saida[saida.size() - 2] = '.';
        saida.erase(saida.size() - 1);
    }
    
    cout<<qtd<<endl;
    cout<<saida<<endl;

    return 0;
}