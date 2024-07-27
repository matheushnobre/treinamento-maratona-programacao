#include <bits/stdc++.h>
using namespace std;

int main(){
    int vetor[4];
    int s=0;
    for (int i=0; i<4; i++)
        cin>>vetor[i];
    cin.ignore();
    
    string ent;
    getline(cin, ent);
    for (char c : ent){
        int num = c - '0';
        s += vetor[num-1];
    }

    cout<<s<<endl;

    return 0;
}