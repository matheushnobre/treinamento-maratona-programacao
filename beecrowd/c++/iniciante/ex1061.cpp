#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    int di, hi, mi, si, df, hf, mf, sf, d, h, m, s;
    
    scanf(" Dia %d", &di);
    scanf("%d : %d : %d", &hi, &mi, &si);
    scanf(" Dia %d", &df);
    scanf("%d : %d : %d", &hf, &mf, &sf);

    if (sf>=si){
        s = sf - si;
    } else{
        s = 60 + sf - si;
        mf -= 1;
    }

    if (mf>=mi){
        m = mf - mi;
    } else{
        m = 60 + mf - mi;
        hf -= 1;
    }

    if (hf>=hi){
        h = hf - hi;
    } else{
        h = 24 + hf - hi;
        df -= 1;
    }

    d = df - di;

    cout<<d<<" dia(s)"<<endl<<h<<" hora(s)"<<endl<<m<<" minuto(s)"<<endl<<s<<" segundo(s)"<<endl;
    
    return 0;
}