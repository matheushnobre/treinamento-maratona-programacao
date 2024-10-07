#include <bits/stdc++.h>
using namespace std;
 
#define MAX 5000
 
int main(){
    int vx[MAX], vy[MAX];
    int n, m=0;
    cin>>n;
 
    for(int i=0; i<n; i++)
        cin>>vx[i];
    for(int i=0; i<n; i++)
        cin>>vy[i];
        
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            int dx = vx[i] - vx[j];
            int dy = vy[i] - vy[j];
            m = max(m, dx*dx + dy*dy);
        }
    }
 
    cout<<m<<endl;
 
    return 0;
}