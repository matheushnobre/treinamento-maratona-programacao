#include <iostream>
#include <stack>

using namespace std;

int main(){
    unsigned long int n, valor, soma=0;
    stack<unsigned long int> monte;

    while(scanf("%d", &n) != EOF){
        for(int i=0; i<n; i++){
            cin>>valor;
            while(!monte.empty()){
                if (monte.top()>valor){
                    soma += monte.top();
                    monte.pop();
                } else break;
            }
            monte.push(valor);
        }
        cout<<soma<<endl;
        soma=0;
        while(!monte.empty()){
            monte.pop();
        }  
    }

    return 0;
}