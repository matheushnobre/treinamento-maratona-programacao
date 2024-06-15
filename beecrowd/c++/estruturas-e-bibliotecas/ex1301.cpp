#include <bits/stdc++.h>
using namespace std;

#define MAX 100100

int segmento[MAX*2];
int vetor[MAX];

int produto(int esq, int dir){
    return esq * dir;
}

void criar(long long tamanho){
    for(long long i = tamanho; i < tamanho*2; i++)
		segmento[i] = vetor[i-tamanho];

	for(long long i = tamanho-1; i > 0; i--)
		segmento[i] = produto(segmento[2*i], segmento[2*i+1]);
}

void atualizar(long long i, int valor, long long n){ 
	i += n;
    segmento[i] = valor;

	while (i > 1){
		i /= 2;
		segmento[i] = produto(segmento[2*i], segmento[2*i+1]);
	}	
}

int executar(long long inicio, long long fim, long long n){
	inicio += n;
	fim += n;
	int prod = 1;

	while (inicio < fim){
		if (inicio % 2 == 1){
			prod = produto(prod, segmento[inicio]);
			inicio++;
		}
		
		if(fim % 2 == 1){
			fim--;
			prod = produto(prod, segmento[fim]);
		}

		inicio /= 2;
		fim /= 2;
		
	}
	return prod;
	
}

int main() {
    long long tamanho, acoes;
    while (cin >> tamanho >> acoes) {
        for (long long i = 0; i < tamanho; i++) {
            int valor;
            cin >> valor;
            if(valor>0)
                vetor[i] = 1;
            else if(valor<0)
                vetor[i] = -1;
            else
                vetor[i] = 0;
        }
        criar(tamanho);

        string saida = "";
        for (long long i = 0; i < acoes; i++) {
            char comando;
            cin >> comando;
            if (comando == 'C') {
                long long x, y;
                cin >> x >> y;
                if(y>0)
                    y=1;
                else if(y<0)
                    y = -1;
                else
                    y=0;
                atualizar(x - 1, y, tamanho);
            } else if (comando == 'P') {
                long long x, y;
                cin >> x >> y;
                long long res = executar(x - 1, y, tamanho);
                if (res > 0)
                    saida += '+';
                else if (res < 0)
                    saida += '-';
                else
                    saida += '0';
            }
        }

        cout << saida << endl;
    }

    return 0;
}