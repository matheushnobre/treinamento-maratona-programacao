#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    double q, d, p;
    while (true){
        cin>>q;
        if (q==0){
            break;
        }
        cin>>d>>p;
        double x = (p*d) / (p-q);        
        int resp = x * q;
        if (resp != 1){
            cout<<resp<<" paginas"<<endl;
        } else{
            cout<<"1 pagina"<<endl;
        }
    }
        

    return 0;
}