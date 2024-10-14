#include <bits/stdc++.h>
using namespace std;

// Ideia da mochila
pair<vector<int>, vector<int>> somaIgualS(vector<int> valores, int s, int n){
    int aux[n+1][s+1]; 
    memset(aux, 0, sizeof(aux)); 

    for(int i=0; i<n; i++){
        int p = valores[i];
        for(int j=0; j<=s; j++){
            if(j<p){
                aux[i+1][j] = aux[i][j];
            }
            else{
                aux[i+1][j] = max(aux[i][j], p+aux[i][j-p]);
            }
        }
    }

    vector<int> alice;
    vector<int> bob;
    if(aux[n][s] == s){
        int j = s;
        for(int i=n; i>0; i--){
            if (aux[i][j] != aux[i-1][j]){
                alice.push_back(valores[i-1]);
                j -= valores[i-1];
            } 
            else{
                bob.push_back(valores[i-1]);
            }
        }   
    }
    return {alice, bob};
}

int main(){
    int n, v, s=0;
    vector<int> caramelos;

    // Lê a entrada do problema
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>v;
        s+=v;
        caramelos.push_back(v);
    }

    if(s % 2 == 1){
        // Se a quantidade total de caramelos for um valor ímpar, já sabe-se que nenhuma sequência resolverá o problema
        cout<<-1<<endl;
    } 
    else{
        // Se a quantidade total não for ímpar, veriica-se quantos caramelos cada um irá receber
        s = s/2;
        // Agora devemos resolver o seguinte problema: dado um vetor de N elementos, quais elementos juntos somam o valor de S?
        // Vamos utilizar a ideia da mochila para reunir os números cuja soma irá ser S. Caso eu encontre um valor menor, o problema não tem solução e exibo -1
        pair<vector<int>, vector<int>> par = somaIgualS(caramelos, s, n);
        vector<int> alice = par.first;
        vector<int> bob = par.second;

        // Verificando se não há solução:
        if(alice.size() == 0){
            cout<<-1<<endl;
        }

        else{
            // Recuperando a sequência correta
            int indexAlice=0, indexBob=0, pontAlice=0, pontBob=0;
            while(indexAlice < alice.size() or indexBob < bob.size()){
                if(pontAlice <= pontBob){
                    pontAlice += alice[indexAlice];
                    cout<<alice[indexAlice]<<" ";
                    indexAlice++;
                } else{
                    pontBob += bob[indexBob];
                    cout<<bob[indexBob]<<" ";
                    indexBob++;
                }
            }
        }
    }

    return 0;
}