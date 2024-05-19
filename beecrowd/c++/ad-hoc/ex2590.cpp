#include <stdio.h>
 
int main() {
    int t;
    int resultados[4] = {1, 7, 9, 3};
    scanf("%d", &t);
    for(int i=0; i<t; i++){
        int n;
        scanf("%d", &n);
        printf("%d\n", resultados[n%4]);
    }
 
    return 0;
}