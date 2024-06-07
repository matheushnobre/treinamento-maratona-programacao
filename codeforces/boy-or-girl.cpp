#include <iostream>
#include <string>
#include <set>
using namespace std;

int main(){
    string text;
    cin >> text;
    set <char> letras;

    for(char c : text){
        letras.insert(c);
    }

    if (letras.size() % 2 == 0){
        cout<<"CHAT WITH HER!"<<endl;
    } else{
        cout<<"IGNORE HIM!"<<endl;
    }
    
    return 0;
}