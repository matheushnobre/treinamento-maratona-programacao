/*
ID: matheus30
TASK: milk
LANG: C++                 
*/             

#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("milk.in", "r", stdin);
    freopen("milk.out", "w", stdout);

    int n, m, a, b, s=0;
    vector<pair<int, int>> agricultores;

    cin>>n>>m;
    for(int i=0; i<m; i++){
        cin>>a>>b;
        agricultores.push_back({a, b});
    }

    sort(agricultores.begin(), agricultores.end());

    int i=0;
    while (n > 0){
        int unidades = min(n, agricultores[i].second);
        s += (agricultores[i].first * unidades);
        n -= unidades;
        i += 1;
    }

    cout<<s<<endl;

    return 0;
}