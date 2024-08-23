#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("blocks.in", "r", stdin);
    freopen("blocks.out", "w", stdout);

    int n;
    int contagemA[26];
    int contagemB[26];
    int maiorContagem[26] = {0};

    string a, b;

    std::cin>>n;
    for(int i=0; i<n; i++){
        memset(contagemA, 0, sizeof(contagemA));
        memset(contagemB, 0, sizeof(contagemB));

        cin>>a>>b;
        for(char c : a)
            contagemA[c - 'a']++;
        for (char c : b)
            contagemB[c - 'a']++;
        for(int j=0; j<26; j++)
            maiorContagem[j] += max(contagemA[j], contagemB[j]);
            
    }

    for(int i=0; i<26; i++)
        cout<<maiorContagem[i]<<endl;

    return 0;
}