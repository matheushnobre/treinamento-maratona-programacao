#include <iostream>
#include <string>
using namespace std;

int main(){
    int casosTeste;
    cin>>casosTeste;
    
    for (int i=0; i<casosTeste; i++){
        int minutos;
        string tempo;
        
        cin>>minutos>>tempo;
        if (tempo == "1T"){
            if (minutos > 45){
                cout<<"45+"<<minutos-45<<endl;
            } else{
                cout<<minutos<<endl;
            }
        } else{
            if (minutos>45){
                cout<<"90+"<<minutos-45<<endl;
            } else{
                cout<<minutos+45<<endl;
            }
        }
        
    
    }
    
    return 0;
}
