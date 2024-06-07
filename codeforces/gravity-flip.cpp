#include <iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    int vetor[n];

    for (int i=0; i<n; i++){
        cin>>vetor[i];
    }

    for(int i=0; i<n; i++){
        int min = vetor[i], index=i;
        for(int j=i; j<n; j++){
            if (vetor[j] < min){
                min = vetor[j];
                index = j;
            }
        }
        swap(vetor[i], vetor[index]);
        cout<<vetor[i]<<" ";
    }

    return 0;
}