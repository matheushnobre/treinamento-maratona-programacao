#include <iostream>
#include <stack>

using namespace std;

int main(){
    int n;
    string mina;
    stack<char> pilha;

    cin>>n;
    cin.ignore();
    for(int i=0; i<n; i++){
        int qtd=0;
        getline(cin, mina);
        for (char c : mina){
            if (c=='<'){
                pilha.push('<');
            } else if(c=='>'){
                if(!pilha.empty()){
                    qtd+=1;
                    pilha.pop();
                }
            }
        }
        cout<<qtd<<endl;
        while(!pilha.empty()){
            pilha.pop();
        }
    }

    return 0;
}