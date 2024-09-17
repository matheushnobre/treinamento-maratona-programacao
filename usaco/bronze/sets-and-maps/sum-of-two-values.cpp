#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x;
    cin>>n>>x;
    vector<int> array(n);

    for (int i=0; i<n; i++) {
        cin>>array[i];
    }

    map<int, int> dic;
    for (int i=0; i<n; i++) {
        dic[array[i]] = i;
    }

    bool hasOutput = false;
    for (int i=0; i<n; i++) {
        int element = array[i];
        int saida = x - element;

        if(dic.count(saida) == 1){
            int j = dic[saida];
            if (j != i) {
                    cout << i+1 << " " << j+1 << endl;
                    hasOutput = true;
                    break;
                }
            }
        }
    if (!hasOutput) {
        cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}
