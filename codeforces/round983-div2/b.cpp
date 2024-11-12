#include <bits/stdc++.h>
using namespace std;

int main(){
    int t, n, k;
    cin>>t;
    for(int ct=0; ct<t; ct++){
        cin>>n>>k;
        if(k==n and n != 1){
            cout<<-1<<endl;
        } else if(k==1 and n!=1){
            cout<<-1<<endl;
        } else if(k==1 and n==1){
            cout<<1<<endl;
            cout<<1<<endl;
        }
        else{
            if (k % 2 == 0){
                cout<<3<<endl;
                cout<<1<<" "<<k<<" "<<k+1<<endl;
            } else{
                cout<<3<<endl;
                cout<<1<<" "<<k-1<<" "<<k+2<<endl;
            }
        }
    }

    return 0;
}