n = int(input())
paises = []

for _ in range(n):
    p, g, s, b = input().split()
    paises.append([p, int(g), int(s), int(b)])

for i in range(len(paises)):
    for j in range(len(paises)-1):
        if paises[j][1] < paises[j+1][1]:
            paises[j], paises[j+1] = paises[j+1], paises[j]
        
        elif paises[j][1] == paises[j+1][1]:
            if paises[j][2] < paises[j+1][2]:
                paises[j], paises[j+1] = paises[j+1], paises[j]
            
            elif paises[j][2] == paises[j+1][2]:
                if paises[j][3] < paises[j+1][3]:
                    paises[j], paises[j+1] = paises[j+1], paises[j]
                
                elif paises[j][3] == paises[j+1][3]:
                    if paises[j][0] > paises[j+1][0]:
                        paises[j], paises[j+1] = paises[j+1], paises[j]
                

for pais in paises:
    print(*pais)
    