#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

bool isSubstring(string palavra, string sub){
    int tamPal = palavra.size();
    int tamSub = sub.size();
    for(int i=0; i<=tamPal-tamSub; i++){
        int j=0, v=i;
        while (v < tamPal){
            if(palavra[v] == sub[j]){
                j++;
            }
            if(j==tamSub){
                return true;
            }
            v++;
        }
    }
    return false;
}


int main(){
    int testes, queries;
    string palavra, sub;
    cin>>testes;

    for(int i=0; i<testes; i++){
        cin>>palavra;
        cin>>queries;
        for (int j=0; j<queries; j++){
            cin>>sub;
            if(isSubstring(palavra, sub)==true){
                cout<<"Yes"<<endl;
            } else{
                cout<<"No"<<endl;
            }
        }
    }

    return 0;
}