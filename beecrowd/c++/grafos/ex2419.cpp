#include <iostream>
using namespace std;

int main(){
    int m, n, crosta=0;
    cin>>m>>n;
    char mapa[m][n];

    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            cin>>mapa[i][j];
        }
    }

    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if(mapa[i][j] == '#'){
                if(i==0 || i==m-1)
                    crosta += 1;

                else if(j==0 || j==n-1)
                    crosta += 1;
                
                else if(mapa[i-1][j] == '.')
                    crosta += 1;

                else if(mapa[i][j-1] == '.')
                    crosta += 1;

                else if(mapa[i][j+1] == '.')
                    crosta += 1;

                else if(mapa[i+1][j] == '.')
                    crosta += 1;
            }
        }
    }

    std::cout<<crosta<<endl;

    return 0;
}