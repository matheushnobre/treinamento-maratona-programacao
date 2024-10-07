#include <bits/stdc++.h>
using namespace std;


int main(){
    int n;
    cin>>n;
    vector<pair<int, char>> cows;

    int ans=n;
    for(int i=0; i<n; i++){
        char d;
        int v;
        cin>>d>>v;
        cows.push_back({v, d});
    }
    sort(cows.begin(), cows.end());

    for(int i=0; i<n; i++){
        int liars=0;
        for(int j=0; j<i; j++)
            if(cows[j].second=='L') liars++;
        for(int j=i+1; j<n; j++)
            if(cows[j].second=='G') liars++;        
        ans = min(ans, liars);
    }

    cout<<ans<<endl;
    return 0;
}