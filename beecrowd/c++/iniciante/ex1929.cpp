#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    int a, b, c, d;
    char s;
    cin>>a>>b>>c>>d;

    if (a+b>c && a+c>b && b+c>a){
        s = 'S';
    } else if(a+b>d && a+d>b && b+d>a){
        s = 'S';
    } else if(a+c>d && a+d>c && d+c>a){
        s = 'S';
    } else if(b+c>d && b+d>c && c+d>b){
        s = 'S';
    } else{
        s = 'N';
    }

    cout<<s<<endl;

    return 0;
}