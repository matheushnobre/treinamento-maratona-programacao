#include <bits/stdc++.h>
using namespace std;

#define MAX 100001

int main(){
    long long n, s=0, p, t;
    int cows[MAX];

    cin>>n;
    for(int i=0; i<n; i++)
        cin>>cows[i];
        
    sort(cows, cows+n);

    for(int i=0; i<n; i++){
        t = cows[i] * (n-i);
        if(t > s){
            s = t;
            p = cows[i];
        }
    }

    cout<<s<<" "<<p<<endl;
    return 0;
}