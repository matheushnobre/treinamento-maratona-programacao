#include <iostream>
using namespace std;

int main(){
    int n, m, valor, minJ=0;
    bool isEscada = true;
    cin>>n>>m;
    int matriz[n][m];

    for(int i=0; i<n; i++){
        bool verifica = false;
        for(int j=0; j<m; j++){
            cin>>valor;
            if(valor>0){
                if(!verifica){
                    if (j<minJ)
                        isEscada = false;
                    else{
                        verifica = true;
                        minJ = j+1;
                    }
                }
                    
            }
        }
        if(!verifica)
            minJ = m;
    }
    if(isEscada)
            cout<<"S"<<endl;
        else
            cout<<"N"<<endl;

    return 0;
}