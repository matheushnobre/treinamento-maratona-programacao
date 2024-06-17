#include <iostream>
#include <string>
#include <fstream> 

using namespace std;

int main(){
    string palavra, linha="", resultante="";
    
    while(cin>>palavra){
        
        if(palavra == "<br>"){
            cout<<linha;
            linha="";
            resultante="";
            cout<<endl;
        } else if(palavra=="<hr>"){
            cout<<linha;
            if(linha.length()!=0)
                cout<<endl;
            linha="";
            resultante="";
            cout<<"--------------------------------------------------------------------------------"<<endl;
        } else{
            if (resultante.length() != 0)
                resultante = linha+" "+palavra;
            else
                resultante = palavra;
            if (resultante.length() > 80){
                cout<<linha<<endl;
                linha=palavra;
                resultante=linha;
            }
            else
                linha = resultante;
        }
        
    }
    cout<<linha;
    cout<<endl;
    
    return 0;
}