#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    double a, b, c;
    cin>>a>>b>>c;
    
    if (a<b){
        swap(a, b);
    }
    if (a<c){
        swap(a, c);
    }
    if (b<c){
        swap(b, c);
    }
    
    if (a >= b+c){
        cout<<"NAO FORMA TRIANGULO"<<endl;
    } else{
        if (a*a == b*b + c*c){
            cout<<"TRIANGULO RETANGULO"<<endl;
        } else if (a*a > b*b + c*c){
            cout<<"TRIANGULO OBTUSANGULO"<<endl;
        } else{
            cout << "TRIANGULO ACUTANGULO"<<endl;
        }
        
        if (a == b && b == c){
            cout<<"TRIANGULO EQUILATERO"<<endl;
        } else if (a == b || a == c || b == c){
            cout<<"TRIANGULO ISOSCELES"<<endl;
        }
    } 
    
    return 0;
}