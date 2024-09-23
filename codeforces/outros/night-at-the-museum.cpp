#include <bits/stdc++.h>
using namespace std;

int main(){
    string pal;
    int m=0;
    cin>>pal;

    char atual='a';
    for(char c : pal){
        if(atual > c) m += min(atual-c, c-atual+26);
        else m += min(atual-c+26, c-atual);
        atual = c;
    }

    cout<<m<<endl;
    return 0;
}