#include <iostream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

int main(){
    int n;
    string sTeste;
    vector <string> vTeste;
    cin>>n;
    cin.ignore();
    for(int i=0; i<n; i++){
        getline(cin, sTeste);
        istringstream iss(sTeste);
        string pal;
        while (iss>>pal){
            vTeste.push_back(pal);
        }

        for(int i=0; i<vTeste.size(); i++){
            for(int j=0; j<vTeste.size()-1; j++){
                if (vTeste[j].length() < vTeste[j+1].length()){
                    swap(vTeste[j], vTeste[j+1]);
                }
            }
        }

        for(int i=0; i<vTeste.size(); i++){
            cout<<vTeste[i];
            if(i!=vTeste.size()-1){
                cout<<" ";
            } else{
                cout<<endl;
            }
        }

        vTeste.clear();
    }

    return 0;
}