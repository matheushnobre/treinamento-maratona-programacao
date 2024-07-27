#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int i=0, j=n-1, s=0, d=0, p;
    int vetor[n];

    for (int c=0; c<n; c++)
        cin>>vetor[c];

    int jog=0;
    while(i<=j){
        if (vetor[i]>vetor[j]){
            p=vetor[i];
            i+=1;
        } else{
            p=vetor[j];
            j-=1;
        }
        
        jog%2==0 ? s+=p : d+=p;
        jog+=1;
    }

    cout<<s<<" "<<d<<endl;

    return 0;
}