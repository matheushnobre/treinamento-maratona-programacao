#include <iostream>
#include <string>
using namespace std;

string lower(string text){
    string r = "";
    for (char c : text){
        r += tolower(c);
    }
    return r;
}

int main(){
    string a, b;
    cin>>a>>b;

    a = lower(a);
    b = lower(b);
    
    if(a>b){
        cout<<1;
    } else if(a==b){
        cout<<0;
    } else{
        cout<<-1;
    }

    return 0;
}