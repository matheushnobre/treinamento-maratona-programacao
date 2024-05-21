#include <iostream>
using namespace std;

int main(){
    int cedulas[7] = {100, 50, 20, 10, 5, 2, 1};
    int n, qtd;
    cin>>n;
    cout<<n<<endl;
    for (int i=0; i<7; i++){
        qtd = n / cedulas[i];
        n = n % cedulas[i];
        cout<<qtd<<" nota(s) de R$ "<<cedulas[i]<<",00"<<endl;
    }

    return 0;
}
