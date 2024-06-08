#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main(){
    int n;
    scanf("%d", &n);
    while (n != 0){
        queue<int> fila;
        vector<int> discard;

        for(int i=1; i<=n; i++){
            fila.push(i);
        }

        while (!fila.empty()){
            discard.push_back(fila.front());
            fila.pop();
            fila.push(fila.front());
            fila.pop();
        }

        cout<<"Discarded cards: ";
        for(int i=0; i<n-1; i++){
            cout<<discard[i];
            if (i!=n-2){
                cout<<", ";
            }
        }

        cout<<"\nRemaining card: "<<discard[n-1]<<endl;

        scanf("%d", &n);
    }
}