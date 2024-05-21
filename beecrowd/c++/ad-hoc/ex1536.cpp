#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    int n, m, v, m1, v1, v2, m2;
    char x;
    cin>>n;
    
    for (int i=0; i<n; i++){
        cin>>m1>>x>>v1;
        cin>>v2>>x>>m2;
        m = m1 + m2;
        v = v1 + v2;
        if (m>v){
            cout<<"Time 1"<<endl;
        } else if(m<v){
            cout<<"Time 2"<<endl;
        } else{
            if (m2>v1){
                cout<<"Time 1"<<endl;
            } else if (m2<v1){
                cout<<"Time 2"<<endl;
            } else{
                cout<<"Penaltis"<<endl;
            }
            
        }
    }
    
    return 0;
}
