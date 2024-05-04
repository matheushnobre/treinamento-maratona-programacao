n = int(input())
mapa = []

maior, atual = 0, 0
for i in range(n):
    lin = input()
    if i % 2 == 0:
        start = 0
        fim = len(lin)
        step = 1
    else:
        start = len(lin)-1
        fim = -1
        step = -1
    for j in range(start, fim, step):
        if lin[j] == 'o':
            atual += 1
        elif lin[j] == 'A':
            if atual > maior:
                maior = atual
            atual = 0
    if atual > maior:
        maior = atual
            
print(maior)