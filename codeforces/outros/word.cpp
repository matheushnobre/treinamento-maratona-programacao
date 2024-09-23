#include <bits/stdc++.h>
using namespace std;

int main(){
    string entrada, saida;
    int upper=0, lower=0;
    cin>>entrada;

    for(char c : entrada){
        if(isupper(c)) upper+=1;
        else lower+=1;
    }

    for(char c : entrada){
        if(upper>lower)
            saida += toupper(c);
        else
            saida += tolower(c);
    }
    
    cout<<saida<<endl;

    return 0;
}