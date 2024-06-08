#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main(){
    int n, m, v;
    unsigned int k;
    map<int, vector<int>> dic;
    while(scanf("%d %d", &n, &m)!=EOF){
        for(int i=0; i<n; i++){
            cin>>k;
            dic[k].push_back(i+1);
        }

        for(int i=0; i<m; i++){
            cin>>k>>v;
            if (dic.count(v)==1){
                if (dic[v].size()>=k){
                    cout<<dic[v][k-1]<<endl;
                } else{
                    cout<<0<<endl;
                }
            } else{
                cout<<0<<endl;
            }
        }
        dic.clear();
    }

    return 0;
}