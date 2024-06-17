#include <iostream>
#include <map>
#include <string>

using namespace std;

map<int, string> unid = {{0, "zero"}, {1, "um"}, {2, "dois"}, {3, "tres"}, {4, "quatro"}, {5, "cinco"}, {6, "seis"}, {7, "sete"}, {8, "oito"}, {9, "nove"}};
map<int, string> esp = {{10, "dez"}, {11, "onze"}, {12, "doze"}, {13, "treze"}, {14, "quatorze"}, {15, "quinze"}, {16, "dezesseis"}, {17, "dezessete"}, {18, "dezoito"}, {19, "dezenove"}, {100, "cem"}};
map<int, string> dez = {{2, "vinte"}, {3, "trinta"}, {4, "quarenta"}, {5, "cinquenta"}, {6, "sessenta"}, {7, "setenta"}, {8, "oitenta"}, {9, "noventa"}};
map<int, string> cen = {{1, "cento"}, {2, "duzentos"}, {3, "trezentos"}, {4, "quatrocentos"}, {5, "quinhentos"}, {6, "seiscentos"}, {7, "setecentos"}, {8, "oitocentos"}, {9, "novecentos"}};

string retornar10a99(int num){
    string text="";
    
    if(esp.count(num) == 1)
        return esp[num];

    int d = num / 10;
    text = dez[d];
    int u = num % 10;
    if(u != 0) text+=" e "+unid[u];
    
    return text;
}

string retornar100a999(int num){
    if (num == 100)
        return "cem";
    string text = "";
    int c = num / 100;
    text = cen[c];
    num = num % 100;

    string aux;
    if (num < 10)
        aux = unid[num];
    else
        aux = retornar10a99(num);
    if (aux != "zero")
        text += " e "+aux;
    
    return text;
}

string retornar100000a999999(int num){
    string aux="";
    if(num == 1000)
        return "mil";
    string text="";

    if (num<10000){
        int um = num / 1000;
        if(um != 1)
            text = unid[um] + " mil";
        else
            text = "mil";
    } else if(num<100000)
        text = retornar10a99(num/1000) + " mil";
    else
        text = retornar100a999(num/1000) + " mil";

    num = num % 1000;
    
    if(num>0 && num<10)
        text += " e "+unid[num];
    else if(num>0 && num<100)
        text += " e "+retornar10a99(num);
    else
        aux = retornar100a999(num);
        if(aux=="cem" || aux=="duzentos" || aux=="trezentos" || aux=="quatrocentos" || aux=="quinhentos" || aux=="seiscentos" || aux=="setecentos" || aux=="oitocentos" || aux=="novecentos")
            text += " e "+aux;
        else
            if(aux.length()>1)
                text += " "+aux;

    return text;
}

int main(){
    int num;
    while(cin>>num){
        if(num<10)
            cout<<unid[num];

        else if(num< 100)
            cout<<retornar10a99(num);

        else if(num < 1000)
            cout<<retornar100a999(num);
    
        else if(num < 1000000)
            cout<<retornar100000a999999(num);

        else
            cout<<"um milhao";

        cout<<endl;
    }

    return 0;
}