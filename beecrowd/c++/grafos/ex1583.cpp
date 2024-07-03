#include <bits/stdc++.h>
using namespace std;

#define MAX 50
char mapa[MAX][MAX];
int n, m;

int vx[4] = {-1, 1, 0, 0};
int vy[4] = {0, 0, -1, 1};

bool isValid(int i, int j){
    if (i >= 0 && i < n && j >=0 && j < m)
        return mapa[i][j] == 'A';

    return false;
    
}

void contaminar(int i, int j){
    mapa[i][j] = 'T';
    for(int x=0; x<4; x++){
        if(isValid(i + vx[x], j + vy[x])){
            contaminar(i + vx[x], j + vy[x]);
        }
    }
}

int main(){
    cin>>n>>m;
    do{
        for(int i=0; i<n; i++)
            scanf("%s", mapa[i]);

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(mapa[i][j] == 'T'){
                    contaminar(i, j);
                }
            }
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                cout<<mapa[i][j];
            } 
            cout<<endl;
        }
        cout<<endl;

        cin>>n>>m;
    } while(n != 0);

    return 0;
}