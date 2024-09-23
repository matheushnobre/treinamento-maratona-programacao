#include <iostream>
using namespace std;

int main(){
    int v, n, m, s=0;
    for (int i=0; i<5; i++){
        for (int j=0; j<5; j++){
            cin>>v;
            if(v==1){
                n=i;
                m=j;
            }
        }
    }

    s += abs(n-2);
    s += abs(m-2);
    cout<<s<<endl;

    return 0;
}