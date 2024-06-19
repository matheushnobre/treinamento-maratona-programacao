#include <iostream>
#include <unordered_set>

using namespace std;

int main(){
    int ct, cs;
    string nome;
    bool facil=true;
    unordered_set<char> consoantes = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'};
    cin>>ct;

    for(int i=0; i<ct; i++){
        cin>>nome;
        cs=0;
        facil=true;

        for(char c : nome){
            if(consoantes.count(c)==1){
                cs+=1;
                if(cs>=3)
                    facil=false;
            } else{
                cs=0;
            }
        }

        if(facil)
            cout<<nome<<" eh facil"<<endl;
        else
            cout<<nome<<" nao eh facil"<<endl;
    }

    return 0;
}