#include <iostream>
using namespace std;

int main(){
    freopen("lostcow.in", "r", stdin);
    freopen("lostcow.out", "w", stdout);

    int x, y;
    cin>>x>>y;

    bool avancar = true, achou=false;
    int pulo=1, position=x, dis=0;

    while(achou==false){
        if(avancar){
            for(int i=position+1; i<=x+pulo; i++){
                dis+=1;
                if(i==y){
                    achou=true;
                    break;
                }
            }
            position = x+pulo;
        } else{
            for(int i=position-1; i>=x-pulo; i--){
                dis+=1;
                if(i==y){
                    achou=true;
                    break;
                }
            }
            position = x-pulo;
        }

        avancar = !avancar;
        pulo *= 2;
    }

    std::cout<<dis<<endl;

    return 0;
}