days = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
t, n = input().split()
diaAtual = days[t]
n = int(n)

menor = 32
lista = list(map(int, input().split()))

for i in lista:
    num = i
    while num > 30:
        dia = (diaAtual - num) % 7
        if dia == 5:
            if num >= 32:
                dia = 0
                num -= 32
            else:
                break
        elif dia == 6:
            if num >= 31:
                dia = 0
                num -= 31     
            else: break
        else:
            num -= 30
        if dia == 0: break
    num = num % 91
    while num >= 30:
        dia = (diaAtual - num) % 7
        if dia == 3:
            if num >= 32:
                dia = 0
                num -= 32
            else:
                break
        elif dia == 4:
            if num >= 31:
                dia = 0
                num -= 31     
            else: break
        elif dia == 5:
            if num >= 32:
                dia = 0
                num -= 32
            else: break
        elif dia == 6:
            if num >= 31:
                dia = 0
                num -= 31
            else: 
                break
        else:
            num -= 30
    
    dia = (diaAtual - num) % 7
    if num == 30 and dia == 6:
        num += 1
    elif num == 30 and dia == 5:
        num += 2
        
    if num <= 30:
        faltam = 30 - num
        
        if faltam == 30 and i != 0: 
            faltam = 0
            
        dia = (faltam + diaAtual) % 7
        if dia == 5:
            faltam += 2
        elif dia == 6:
            faltam += 1
        menor = min(menor, faltam)
    elif num == 31:
        if diaAtual == 0:
            menor = 0
        elif diaAtual == 1:
            menor = min(menor, 1)
        else:
            menor = min(menor, 2)

    elif num == 32:
        if diaAtual == 1:
            menor = 0

print(menor)