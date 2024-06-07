#include <iostream>
#include <string>
using namespace std;

int main(){
    int n, a=0, d=0;
    string ent;
    cin>>n>>ent;

    for(int i=0; i<n; i++){
        if (ent[i] == 'A'){
            a+=1;
        } else{
            d+=1;
        }
    }

    if(a>d){
        cout<<"Anton"<<endl;
    } else if(a==d){
        cout<<"Friendship"<<endl;
    } else{
        cout<<"Danik"<<endl;
    }

    return 0;
}