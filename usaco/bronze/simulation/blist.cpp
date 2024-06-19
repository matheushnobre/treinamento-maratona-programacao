#include <iostream>
using namespace std;

int main(){
    freopen("blist.in", "r", stdin);
    freopen("blist.out", "w", stdout);

    int n;
    cin>>n;

    int vacas[n][3];
    for(int i=0; i<n; i++){
        cin>>vacas[i][0]>>vacas[i][1]>>vacas[i][2];
    }

    int b=0, s=0;
    for(int i=1; i<=1000; i++){
        for(int j=0; j<n; j++){
            if(vacas[j][0] == i){
                b+=vacas[j][2];
                break;
            } else if(vacas[j][1] == i){
                b-=vacas[j][2];
                break;
            }
        }
        if(b>s){s=b;}
    }
    
    cout<<s<<endl;

    return 0;
}