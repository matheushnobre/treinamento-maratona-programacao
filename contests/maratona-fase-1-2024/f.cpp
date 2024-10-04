#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;

    int ant=1, at=2;
    if (n<=2)
        cout<<n<<endl;
    else{
        for(int i=2; i<n; i++){
            int t = at;
            at = at + ant;
            ant = t;
        }
        cout<<at<<endl;
    }


    return 0;
}