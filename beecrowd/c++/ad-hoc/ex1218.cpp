#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>

using namespace std;

int main(){
    int n, ct=0;
    string desc;
    while (cin>>n){
        if(ct != 0){
            cout<<endl;
        }
        int paresIguais=0, f=0, m=0;
        ct++;
        cin.ignore();
        getline(cin, desc);

        istringstream iss(desc);
        int numSapato;
        char sexo;

        while (iss>>numSapato>>sexo){
            if (numSapato==n){
                paresIguais++;
                if (sexo=='M'){
                    m++;
                } else{
                    f++;
                }
            }
        }

        cout<<"Caso "<<ct<<":"<<endl;
        cout<<"Pares Iguais: "<<paresIguais<<endl;
        cout<<"F: "<<f<<endl;
        cout<<"M: "<<m<<endl;
    }

    return 0;
}