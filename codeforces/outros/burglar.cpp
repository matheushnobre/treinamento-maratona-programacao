#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, m, a, b, ans=0;
    vector<pair<int, int>> containers;

    cin>>n>>m;
    for(int i=0; i<m; i++){
        cin>>a>>b;
        containers.push_back({b, a});
    }
    sort(containers.begin(), containers.end());

    int i=m-1;
    while(n!=0 && i>=0){
        int temp=n;
        n -= min(n, containers[i].second);
        ans += containers[i].first * (temp-n);
        i--;
    }

    cout<<ans<<endl;
    return 0;
}