#include <iostream>
using namespace std;

int main(){
    int n, h, a, s=0;
    cin>>n>>h;

    for(int i=0; i<n; i++){
        cin>>a;
        if(a<=h){
            s+=1;
        } else{
            s+=2;
        }
    }
    
    cout<<s<<endl;

    return 0;
}