#include <iostream>
using namespace std;

int main(){
    int a, b, c, n, s=0;
    cin>>n;

    for(int i=0; i<n; i++){
        cin>>a>>b>>c;
        if(a+b+c>=2){
            s+=1;
        }
    }

    cout<<s<<endl;
    
    return 0;
}