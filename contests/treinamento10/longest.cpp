#include <bits/stdc++.h>
using namespace std;

#define MAX 200000

int main(){
    int t;
    int n, k;
    int array[MAX];

    cin>>t;
    for(int ct=0; ct<t; ct++){
        cin>>n>>k;
        for(int i=0; i<n; i++){
            cin>>array[i];
        }
        sort(array, array+n);

        int qtd=1, left=array[0], right=array[0], maior=-1, se, sd;
        for(int i=1; i<n; i++){
            if(array[i] == array[i-1]){
                qtd++;
            }
            else{
                if(qtd>=k){
                    if(array[i]==array[i-1]+1){
                        qtd=1;
                        right=array[i];
                        continue;
                    } else{
                        if (right-left > maior){
                            maior = right-left;
                            se = left;
                            sd = right;
                        }
                        left = array[i];
                        right=array[i];
                    }
                qtd=1;
                } else{
                    qtd=1;
                    right -= 1;
                    if(right - left > maior){
                        maior = right - left;
                        se = left;
                        sd = right;
                    }
                    left = array[i];
                    right=array[i];
                }
            }
        }

        if (qtd<k){
            right -= 1;
        }

        if(right - left > maior){
            maior = right - left;
            se = left;
            sd = right;
        }
        if(maior == -1)
            cout<<-1<<endl;
        else
            printf("%d %d\n", se, sd);
    }
    return 0;
}