#include <bits/stdc++.h>
using namespace std;

#define MAX 20

int main(){
    freopen("gymnastics.in", "r", stdin);
    freopen("gymnastics.out", "w", stdout);

    int k, n, v, pairs=0;
    int matrix[MAX][MAX];

    cin>>k>>n;

    for(int i=0; i<k; i++){
        for(int j=0; j<n; j++){
            cin>>v;
            matrix[i][v-1] = j;
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(i==j)continue;
            int cons=true;
            for(int l=0; l<k; l++){
                if(matrix[l][i]>matrix[l][j]){
                    cons=false;
                    break;
                }
            }
            if (cons){
                pairs++;
            }
        }
    }

    cout<<pairs<<endl;

    return 0;
}