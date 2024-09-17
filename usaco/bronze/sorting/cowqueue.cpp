#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("cowqueue.in", "r", stdin);
    freopen("cowqueue.out", "w", stdout);

    int n, a, b, ta=0;
    vector<pair<int, int>> cows;

    cin>>n;
    for(int i=0; i<n; i++){
        cin>>a>>b;
        cows.push_back({a, b});
    }

    sort(cows.begin(), cows.end());
    for(int i=0; i<n; i++){
        ta = max(ta, cows[i].first) + cows[i].second;
    }

    cout<<ta<<endl;

    return 0;
}