#include <iostream>
#include <string>

using namespace std;

int main(){
    int t, p1, p2, d;
    string certo, time1, time2;
    cin>>t;
    cin.ignore();

    for(int ct=1; ct<=t; ct++){
        getline(cin, certo);
        getline(cin, time1);
        getline(cin, time2);

        p1=0, p2=0;
        d=0;
        for(int i=0; i<certo.size(); i++){
            if(certo[i] == time1[i]){
                p1 += 1;
                if (d==0 && certo[i] != time2[i])
                    d=1;
            } 

            if(certo[i] == time2[i]){
                p2 += 1;
                if (d==0 && certo[i] != time1[i])
                    d=2;
            }
        }

        cout<<"Instancia "<<ct<<endl;
        if(p1 > p2)
            cout<<"time 1"<<endl<<endl;
        else if(p1 < p2)
            cout<<"time 2"<<endl<<endl;
        else{
            if(d==0)
                cout<<"empate"<<endl<<endl;
            else
                cout<<"time "<<d<<endl<<endl;
        }
    }

    return 0;
}