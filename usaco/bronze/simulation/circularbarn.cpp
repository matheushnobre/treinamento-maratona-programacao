#include <iostream>
using namespace std;

int main(){
    freopen("cbarn.in", "r", stdin);
    freopen("cbarn.out", "w", stdout);

    int n, min=-1, total=0;
    cin>>n;
    int vacas[n];

    for(int i=0; i<n; i++)
        cin>>vacas[i];
    
    for(int i=0; i<n; i++){
        total=0;
        for(int j=i; j<i+n; j++){
            total += (vacas[j%n] * (j-i));
        }
        if(total<min || min==-1) 
            min = total;
    }

    cout<<min<<endl;

    return 0;
}