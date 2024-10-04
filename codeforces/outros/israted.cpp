#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, a, b;
    vector<int> p;
    vector<int> o;
    bool isRated=false;
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>a>>b;
        if(a != b)
            isRated = true;
        p.push_back(a);
        o.push_back(a);
    }

    if(!isRated){
        sort(o.begin(), o.end(), std::greater<int>());
        bool maybe=true;
        for(int i=0; i<n; i++){
            if (o[i] != p[i])
                maybe=false;
        }
        if(maybe)
            cout<<"maybe"<<endl;
        else
            cout<<"unrated"<<endl;
    } else{
        cout<<"rated"<<endl;
    }

    return 0;
}