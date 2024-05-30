#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    int n, d;
    while (true){
        cin>>n>>d;
        if (n==0 && d==0){
            break;
        }
        bool saida=false;
        int sala[d][n];
        for (int i=0; i<d; i++){
            for (int j=0; j<n; j++){
                cin>>sala[i][j];
            }
        }

        for(int j=0; j<n; j++){
            bool foi = true;
            for(int i=0; i<d; i++){
                if (sala[i][j] == 0){
                    foi=false;
                }
            }
            if (foi==true){
                saida=true;
            }
        }

        if (saida==true){
            cout<<"yes"<<endl;
        } else{
            cout<<"no"<<endl;
        }

    }

    return 0;
}