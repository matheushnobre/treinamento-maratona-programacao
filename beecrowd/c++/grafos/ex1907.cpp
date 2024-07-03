// Não passa em Python
// DFS não resolve, apenas BFS

#include <bits/stdc++.h>
using namespace std;

char mapa[1030][1030];
int n, m;

void colorir(int i, int j)
{
    mapa[i][j] = 'o';
    queue<pair<int, int>> fila;
    fila.push({i, j});

    while (!fila.empty())
    {
        i = fila.front().first, j = fila.front().second;
        fila.pop();

        if (i + 1 < n){
            if (mapa[i + 1][j] == '.'){
                mapa[i+1][j] = 'o';
                fila.push({i+1, j});
            }
        }

        if (i - 1 >= 0){
            if (mapa[i - 1][j] == '.'){
                mapa[i-1][j] = 'o';
                fila.push({i-1, j});
            }
        }

        if (j + 1 < m){
            if (mapa[i][j + 1] == '.'){
                mapa[i][j+1] = 'o';
                fila.push({i, j+1});
            }
        }

        if (j - 1 >= 0){
            if (mapa[i][j - 1] == '.'){
                mapa[i][j-1] = 'o';
                fila.push({i, j-1});
            }
        }
    }
}

int main()
{
    int cor = 0;
    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++)
    {
        scanf("%s", mapa[i]);
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (mapa[i][j] == '.')
            {
                colorir(i, j);
                cor++;
            }
        }
    }

    printf("%d\n", cor);

    return 0;
}