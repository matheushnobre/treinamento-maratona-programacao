#include <bits/stdc++.h>
using namespace std;

int main(){
    set<char> letras;
    char atual;
    while(atual != '}'){
        cin>>atual;
        if(atual != '{' && atual != '}' and atual != ',')
            letras.insert(atual);
    }

    cout<<letras.size()<<endl;

    return 0;
}