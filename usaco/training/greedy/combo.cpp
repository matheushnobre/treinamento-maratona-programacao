/*
ID: matheus30
TASK: combo
LANG: C++                 
*/        

#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("combo.in", "r", stdin);
    freopen("combo.out", "w", stdout);

    int n, a, b, c, d, e, f;
    cin>>n>>a>>b>>c>>d>>e>>f;
    
    vector<int> jhon = {a, b, c};
    vector<int> master = {d, e, f};
    vector<int> nova;
    set<vector<int>> combinacoes;

    for(int i=-2; i<=2; i++){
        for(int j=-2; j<=2; j++){
            for(int k=-2; k<=2; k++){
                a = jhon[0] + i;
                b = jhon[1] + j;
                c = jhon[2] + k;
                if (a <= 0) a = n + a;
                if (b <= 0) b = n + b;
                if (c <= 0) c = n + c;
                if (a > n) a = a % n;
                if (b > n) b = b % n;
                if (c > n) c = c % n;
                nova = {a, b, c};
                combinacoes.insert(nova);
            }
        }
    }
    
    for(int i=-2; i<=2; i++){
        for(int j=-2; j<=2; j++){
            for(int k=-2; k<=2; k++){
                a = master[0] + i;
                b = master[1] + j;
                c = master[2] + k;
                if (a <= 0) a = n + a;
                if (b <= 0) b = n + b;
                if (c <= 0) c = n + c;
                if (a > n) a = a % n;
                if (b > n) b = b % n;
                if (c > n) c = c % n;
                nova = {a, b, c};  
                combinacoes.insert(nova);
            }
        }
    }

    if(n == 1)
        cout<<1<<endl;
    else
        cout<<combinacoes.size()<<endl;

    return 0;
}