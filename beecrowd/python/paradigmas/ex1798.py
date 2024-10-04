INF = 1e10
def solucao(precos, t):
    aux = [-INF] * (t+1)
    aux[0] = 0
    
    for j in range(1, t+1):
        q = -INF
        for i in range(1, j+1):
            q = max(q, precos[i] + aux[j-i])
        aux[j] = q
        
    return aux[t]
   
n, t = map(int, input().split())
p = [0] * (t+1)

for _ in range(n):
    c, v = map(int, input().split())
    if c <= t:
        p[c] = max(p[c], v)

print(solucao(p, t))