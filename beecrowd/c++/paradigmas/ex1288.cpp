#include <bits/stdc++.h>
using namespace std;

#define MAXN 110
#define MAXK 110

int main(){
    int ct, n, x, y, r, k;
    int dp[MAXN][MAXK];
    scanf("%d", &ct);
    for(int t=0; t<ct; t++){
        memset(dp, 0, sizeof(dp)); 
        scanf("%d", &n);
        for(int i=0; i<n; i++){
            scanf("%d %d", &x, &y);
            for(int j=0; j<MAXK; j++){
                if(y>j) dp[i+1][j] = dp[i][j];
                else dp[i+1][j] = max(dp[i][j], dp[i][j-y]+x);
            }
        }
        scanf("%d", &k);
        scanf("%d", &r);
        if(dp[n][k] >= r)
            printf("Missao completada com sucesso\n");
        else
            printf("Falha na missao\n");
    }

}