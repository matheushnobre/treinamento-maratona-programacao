from math import sqrt

def distancia(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

bolinhas = []
t = int(input())
for _ in range(t):
    x, y, r = map(int, input().split())
    bolinhas.append((x, y, r))
    
s = 0
for i in range(t):
    b = 0
    for j in range(t):
        if i != j:
            b1 = bolinhas[i]
            b2 = bolinhas[j]
            x1, y1, x2, y2, r1, r2 = b1[0], b1[1], b2[0], b2[1], b1[2], b2[2]
            if distancia(x1, y1, x2, y2) < r1 + r2:
                b += 1
    if b > s:
        s = b
        
print(s)
    