#include <iostream>
using namespace std;

int main(){
    int a, b, d=0;
    cin>>a>>b;

    while(a<=b){
        a*=3;
        b*=2;
        d+=1;
    }

    cout<<d<<endl;

    return 0;
}