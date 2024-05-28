#include <iostream>
#include <string.h>

using namespace std;

int main(){
    int n, t;
    string pulos;
    cin>>n;
    
    while(n){
        cin>>t;
        int tiros[t];
        for (int i=0; i<t; i++){
            cin>>tiros[i];
        }
        cin>>pulos;
        int atingido = 0;
        for(int i=0; i<t; i++){
            if (tiros[i] <= 2 && pulos[i] == 'S'){
                atingido++;
            } else if(tiros[i]>2 && pulos[i] == 'J'){
                atingido++;
            }
        }
        cout<<atingido<<endl;

        n--;
    }
    
    
    return 0;
}
