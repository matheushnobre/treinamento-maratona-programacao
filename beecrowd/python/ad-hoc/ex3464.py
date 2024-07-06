total = 0        
n, m = map(int, input().split())
mapa = [[0] * m for _ in range(n)]

s = int(input())
for _ in range(s):
    x, y, r = map(int, input().split())

    cima = min(r, x-1)
    baixo = min(r, n-x)
    direita = min(r, m-y)
    esquerda = min(r, y-1)
    
    total += ((cima*direita) + (cima*esquerda) + cima)
    total += ((baixo*direita) + (baixo*esquerda) + baixo)
    total += (direita + esquerda + 1)
        
print(total // (n*m))