#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int n, wi, im=5000000;
    vector<int> v;
 
    cin>>n;
    for(int i=0; i<2*n; i++){
        cin>>wi;
        v.push_back(wi);
    }
 
    sort(v.begin(), v.end());
 
    for(int i=0; i<v.size(); i++){
        for(int j=0; j<v.size(); j++){
            if(j==i){
                continue;
            }
            int it=0;
            int first, second, control=0;
            for(int k=0; k<v.size(); k++){
                if(k==i || k==j){
                    continue;
                }
                if (control % 2 == 0){
                    first = v[k];
                } else{
                    second = v[k];
                    it+=second-first;
                }
                control++;
            }
            im = min(it, im); 
        }
    }
 
    std::cout<<im<<endl;
 
    return 0;
}