#include <bits/stdc++.h>
using namespace std;

char tab[3][3];
int s1=0, s2=0;
set<char> ind;
set<string> eq;

bool isInLine(string line, char c){
    for (int i=0; i<3; i++)
        if (line[i] == c)
            return true;
    return false;
}

void qtd(string aux){
    string line = "---";
    int qtd=0;
    for(int i=0; i<3; i++){
        if (!isInLine(line, aux[i]))
            qtd++;
        line[i] = aux[i];
    }
    
    if(qtd==1)
        ind.insert(line[0]);
    else if(qtd==2){
        string letters;
        if(line[1] != line[0])
            letters = line[0] + line[1];
        else
            letters = line[0] + line[2];
        sort(letters.begin(), letters.end());
        eq.insert(letters);
    }
}

int main(){
    freopen("tttt.in", "r", stdin);
    freopen("tttt.out", "w", stdout);

    for(int i=0; i<3; i++)
        for(int j=0; j<3; j++)
            cin>>tab[i][j];
        
    
    for(int i=0; i<3; i++){
        string line = "---";
        for(int j=0; j<3; j++)
            line[j] = tab[i][j];
        qtd(line);
    }

    for(int j=0; j<3; j++){
        string collumn = "---";
        for(int i=0; i<3; i++)
            collumn[i] = tab[i][j];
        qtd(collumn);
    }

    string aux = "";
    for(int i=0; i<3; i++)
        aux = aux + tab[i][i];
    qtd(aux);

    aux = "";
    for(int i=0; i<3; i++)
        aux = aux + tab[i][2-i];
    qtd(aux);
    
    cout<<ind.size()<<endl<<eq.size()<<endl;
    return 0;
}