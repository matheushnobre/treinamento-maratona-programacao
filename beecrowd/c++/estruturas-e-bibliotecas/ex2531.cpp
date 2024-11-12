#include <bits/stdc++.h>
using namespace std;

#define MAXN 100010
#define INF 1000010

int vetor[MAXN];
int maxTree[4*MAXN];
int minTree[4*MAXN];

int buildMaxTree(int node, int l, int r){
    if(l == r) return maxTree[node] = vetor[l];
    int m = (l+r)/2;
    return maxTree[node] = max(buildMaxTree(2*node, l, m), buildMaxTree(2*node+1, m+1, r));
}

int queryMaxTree(int node, int l, int r, int a, int b){
    if(b < l or r < a) return -INF;
    if(a <= l and r <= b) return maxTree[node];
    int m = (l+r) / 2;
    return max(queryMaxTree(2*node, l, m, a, b), queryMaxTree(2*node+1, m+1, r, a, b));
}

void updateMaxTree(int node, int l, int r, int i, int x){
    if(i < l or r < i) return;
    if(l == r){
        maxTree[node] = x;
        return;
    }
    int m = (l+r) / 2;
    updateMaxTree(2*node, l, m, i, x);
    updateMaxTree(2*node+1, m+1, r, i, x);
    maxTree[node] = max(maxTree[2*node], maxTree[2*node+1]);
}

int buildMinTree(int node, int l, int r){
    if(l == r) return minTree[node] = vetor[l];
    int m = (l+r)/2;
    return minTree[node] = min(buildMinTree(2*node, l, m), buildMinTree(2*node+1, m+1, r));
}

int queryMinTree(int node, int l, int r, int a, int b){
    if(b < l or r < a) return INF;
    if(a <= l and r <= b) return minTree[node];
    int m = (l+r) / 2;
    return min(queryMinTree(2*node, l, m, a, b), queryMinTree(2*node+1, m+1, r, a, b));
}

void updateMinTree(int node, int l, int r, int i, int x){
    if(i < l or r < i) return;
    if(l == r){
        minTree[node] = x;
        return;
    }
    int m = (l+r) / 2;
    updateMinTree(2*node, l, m, i, x);
    updateMinTree(2*node+1, m+1, r, i, x);
    minTree[node] = min(minTree[2*node], minTree[2*node+1]);
}

int main(){
    int n, q, o, a, b;
    while(scanf("%d", &n) != EOF){
        for(int i=0; i<n; i++)
            scanf("%d", &vetor[i]);
        buildMaxTree(1, 0, n-1);
        buildMinTree(1, 0, n-1);
        scanf("%d", &q);
        for(int i=0; i<q; i++){
            scanf("%d %d %d", &o, &a, &b);
            if(o==1){
                updateMaxTree(1, 0, n-1, a-1, b);
                updateMinTree(1, 0, n-1, a-1, b);
            }
            else
                printf("%d\n", queryMaxTree(1, 0, n-1, a-1, b-1) - queryMinTree(1, 0, n-1, a-1, b-1));
        }
    }

    return 0;
}