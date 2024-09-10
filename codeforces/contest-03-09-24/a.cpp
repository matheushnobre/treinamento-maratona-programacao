#include <bits/stdc++.h>
using namespace std;

int main(){
    int ct, a, b, c, s;
    cin>>ct;
    for (int i=0; i<ct; i++){
        cin>>a>>b;
        c = (a+b)/2;
        s = c-a+b-c;
        cout<<s<<endl;
    }

    return 0;
}