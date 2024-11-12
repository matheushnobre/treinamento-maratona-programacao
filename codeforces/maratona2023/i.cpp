#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long int
#define MOD 1000000007

int main(){
    string s;
    ll n, ans=0;
    map<char, int> alf;
    string letras = "abcdefghijklmnopqrstuvwxyz";
    for(int i=0; i<26; i++)
        alf[letras[i]] = i;
    int freq[26] = {0};

    cin>>s>>n;
    n = n%MOD; 

    for(int i=s.size()-1; i>=0; i--){
        int index = alf[s[i]];
        freq[index] += 1;
        for(int j=0; j<index; j++){
            ll gauss = ((n*(n+1))/2) % MOD;
            ans = (ans + freq[j] * gauss) % MOD;
        }
    }

    for(int i=0; i<26; i++)
        freq[i] = 0;

    if(n!=1){
        for(int i=0; i<=s.size()-1; i++){
            int index = alf[s[i]];
            freq[index] += 1;
            for(int j=0; j<index; j++){
                ll gauss = ((n*(n-1))/2) % MOD;
                ans = (ans + freq[j] * gauss) % MOD;
            }
        }
    }

    cout<<ans;

    return 0;
}

