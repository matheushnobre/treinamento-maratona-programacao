from math import sqrt

def distancia(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

c = int(input())
for _ in range(c):
    n = int(input())
    xbranca, ybranca = map(int, input().split())
    menor = 100000000000
    s = 0
    for i in range(1, n+1):
        x, y = map(int, input().split())
        d = distancia(x, y, xbranca, ybranca)
        if d < menor:
            menor = d
            s = i
    print(s)