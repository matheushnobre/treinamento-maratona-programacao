#include <bits/stdc++.h>
using namespace std;

int main(){
    int a, b, n, d=6;
    cin>>a>>b;
    a = max(a, b);

    n = 6-a+1;
    if(n==d){
        n=1;
        d=1;
    }
    else if(n%2==0){
        n /= 2;
        d /= 2;
    } else if(n==3){
        n = 1;
        d = 2;
    }

    std::cout<<n<<"/"<<d<<endl;
    return 0;
}