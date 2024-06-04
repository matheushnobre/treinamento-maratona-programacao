#include <bits/stdc++.h>
using namespace std;

int main(){
    int x = 2;
    vector<int> v = {0, 2, 4, 6, 8, 10};
    int menorQueX = lower_bound(v.begin(), v.end(), x) - v.begin(); // 1º elemento >= x
    cout << "lower bound: "<<v[menorQueX]<<endl;
    
    int maiorQueX = upper_bound(v.begin(), v.end(), x) - v.begin(); //1º elemento > x
    cout << "upper bound: "<<v[maiorQueX]<<endl;
    return 0;
}