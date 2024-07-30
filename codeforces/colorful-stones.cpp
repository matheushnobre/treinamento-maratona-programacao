#include <bits/stdc++.h>
using namespace std;

int main(){
    string a, b;
    int p=0;
    cin>>a>>b;

    for (char c : b)
        if (a[p] == c) p++;

    cout<<p+1<<endl;
    
    return 0;
}