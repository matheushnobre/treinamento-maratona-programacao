#include <bits/stdc++.h>
using namespace std;

int main() {
    double c, i, js, jc, d;
    int n;

    while (scanf("%lf", &c) != EOF) {
        scanf("%lf", &i);
        scanf("%d", &n);

        js = c * i * n;
        jc = (c * pow((1 + i), n)) - c;
        d = jc - js;

        js = round(js * 100.0) / 100.0;
        jc = round(jc * 100.0) / 100.0;
        d = round(d * 100.0) / 100.0;

        cout << fixed << setprecision(2);
        cout << "DIFERENCA DE VALOR = " << d << endl;
        cout << "JUROS SIMPLES = " << js << endl;
        cout << "JUROS COMPOSTOS = " << jc << endl;
    }

    return 0;
}
