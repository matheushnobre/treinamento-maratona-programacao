#include <bits/stdc++.h>
using namespace std;

int main(){
    long long n, menor=100000000, maior=0, valor, ant=0, vdmenor;
    bool ultMenor=false;
    cin>>n;

    for(long long i=0; i<n; i++){
        cin>>valor;
        if(valor < menor){
            menor = valor;
            vdmenor = menor+ant;
            ultMenor = false;
        } 
        if(valor > maior){
            maior = valor;
        }
        ant=valor;
        if(ultMenor) vdmenor+=valor;
        if(menor==ant) ultMenor = true;
        else ultMenor = false;
    }

    if(vdmenor <= maior)
        cout<<"POSSIVEL";
    else    
        cout<<"IMPOSSIVEL";

    return 0;
}
