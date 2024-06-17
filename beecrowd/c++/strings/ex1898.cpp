#include <iostream>
#include <string>
#include <cctype>
#include <cstdio>

using namespace std;

int main(){
    string cpf="", text1, text2, num1="", num2="";
    double soma;
    int cd=-1;

    cin>>text1>>text2;
    for (char c : text1){
        if (isdigit(c)){
            if (cpf.length()<11)
                cpf+=c;
            else{
                if(cd>=-1 && cd<2){
                    num1+=c;
                    if(cd>-1) cd++;
                }
            }
        } else if(c == '.'){
            num1 += c;
            cd=0;
        }
            
    }

    cd=-1;
    for(char c : text2){
        if (isdigit(c)){
            if(cd>=-1 && cd<2){
                num2+=c;
                if(cd>-1) cd++;
            }
        }
        else if(c == '.'){
            num2+=c;
            cd=0;
        }
    }

    soma = stod(num1) + stod(num2);
    std::cout<<"cpf "<<cpf<<endl;
    printf("%.2f\n", soma);

    return 0;
}