#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int busca(vector<int> marm, int b){
    int inicio = 0, fim = marm.size()-1;
    while(inicio <= fim){
        int m = (inicio+fim)/2;
        if (marm[m] == b){
            while(m>=0){
                if(marm[m-1] == b){
                    m -= 1;
                } else{
                    return m;
                }
            }
            return m;
        }
        else if(marm[m] < b){
            inicio = m+1;
        } 
        else{
            fim = m-1;
        }
    }

    return -1;
}


int main(){
    int n, q, ct=0;
    vector<int> marm;

    while (true){
        ct += 1;
        cin>>n>>q;
        if (n==0 && q==0)
            break;

        for (int i=0; i<n; i++){
            int valor;
            cin>>valor;
            marm.push_back(valor);
        }
        
        sort(marm.begin(), marm.end());
        cout<<"CASE# "<<ct<<":"<<endl;
        for (int i=0; i<q; i++){
            int cons;
            cin>>cons;
            int p = busca(marm, cons);
            if (p==-1){
                cout<<cons<<" not found"<<endl;
            } else{
                cout<<cons<<" found at "<<p+1<<endl;
            }
        }

        marm.clear();
    }

    return 0;
}