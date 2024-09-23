#include <bits/stdc++.h>
using namespace std;

int main(){
    int e, p=0, c=0, o;
    cin>>e;
    for(int i=0; i<e; i++){
        cin>>o;
        if(o==-1){
            if(p==0) c+=1;
            else p-=1;
        }
        else
            p+=o;
    }
    cout<<c<<endl;
}