// Mesma abordagem do Coin Problem

#include <bits/stdc++.h>
using namespace std;

#define MAXN 25
#define MAXM 1000001
#define INF 1000001

int main(){
    int t, n, m;
    int blocos[MAXN] = {0};
    int resposta[MAXM];

    scanf("%d", &t);
    for(int ct=0; ct<t; ct++){
        scanf("%d %d", &n, &m);
        for(int i=0; i<n; i++){
            scanf("%d", &blocos[i]);
        }

        for(int x=1; x<=m; x++){
            resposta[x] = INF;
            for(int i=0; i<n; i++){
                int v = blocos[i];
                if(x-v >= 0){
                    resposta[x] = min(resposta[x], resposta[x-v]+1);
                }
            }
        }

        printf("%d\n", resposta[m]);
    }

    return 0;
}