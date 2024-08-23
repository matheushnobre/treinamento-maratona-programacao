from math import sqrt

def distancia(x1, y1, z1, x2, y2, z2):
    return sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

n = int(input())
pontos = []

for _ in range(n):
    x, y, z = map(int, input().split())
    pontos.append((x, y, z))
    
for i in range(n):
    menor = 101
    p = pontos[i]
    for j in range(n):
        if i != j:
            p2 = pontos[j]
            d = distancia(p[0], p[1], p[2], p2[0], p2[1], p2[2])
            if d<menor:
                menor = d
    if menor<=20:
        print('A')
    elif menor<=50:
        print('M')
    else:
        print('B')
    