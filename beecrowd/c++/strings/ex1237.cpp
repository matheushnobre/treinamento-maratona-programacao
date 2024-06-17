#include <iostream>
#include <string>

using namespace std;

int main(){
    string str1, str2;
    int a, s;
    
    while (getline(cin, str1) && getline(cin, str2)){
        s=0;

        for(int i=0; i<str1.size(); i++){
            a=0;
            for(int j=0; j<str2.size(); j++){
                int aux = i;

                while (aux < str1.size() && j < str2.size() && str1[aux] == str2[j]) {
                    aux++;
                    j++;
                    a++;
                }
                if (a > s) {
                    s = a;
                }
                a = 0; 
            }
        }
        cout<<s<<endl;    
    }

    return 0;
}