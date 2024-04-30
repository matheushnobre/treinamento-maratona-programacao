fita, r = map(int, input().split())
fita = [0]*fita

for i in input().split():
    fita[int(i)-1] = 1
    
dias, distancia = 0, 0
isExtremidade = True

for index, reagente in enumerate(fita):
    if reagente == 0:
        distancia += 1
        if index == len(fita)-1:
            if distancia > dias:
                dias = distancia
                
    if reagente == 1:
        if isExtremidade:
            dias = distancia
            isExtremidade = False
        else:
            if distancia % 2 == 0:
                diasTemp = distancia // 2
            else:
                diasTemp = distancia // 2 + 1
            if diasTemp > dias:
                dias = diasTemp
        distancia = 0

print(dias)