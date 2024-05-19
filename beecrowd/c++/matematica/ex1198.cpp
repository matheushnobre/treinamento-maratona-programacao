#include <iostream>
#include <cstdio>
#include <cstdlib>
 
using namespace std;
 
int main(){
    unsigned long long a, b, diferenca;
    while (scanf("%lld %lld", &a, &b) != EOF){
        if (a > b){
            diferenca = a - b;
        } else{
            diferenca = b - a;
        }
        printf("%lld\n", diferenca);
    }
 
    return 0;
}
