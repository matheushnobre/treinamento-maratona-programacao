#include <bits/stdc++.h>
using namespace std;

char tab[8][8];
bool col[8], diag1[15], diag2[15]; // diag1 e diag2 para controlar as diagonais
int qtd = 0;

void solve(int row) {
    if (row == 8) {
        qtd++;
        return;
    }
    
    for (int c = 0; c < 8; c++) {
        if (tab[row][c] == '*' || col[c] || diag1[row - c + 7] || diag2[row + c]) 
            continue;
        
        // Marcar a coluna e diagonais
        col[c] = diag1[row - c + 7] = diag2[row + c] = true;
        
        // Tentar posicionar a próxima rainha
        solve(row + 1);
        
        // Desmarcar a coluna e diagonais
        col[c] = diag1[row - c + 7] = diag2[row + c] = false;
    }
}

int main() {
    // Ler o tabuleiro
    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++)
            cin >> tab[i][j];
    
    // Resolver o problema
    solve(0);
    
    // Imprimir o número de soluções
    cout << qtd << endl;

    return 0;
}
