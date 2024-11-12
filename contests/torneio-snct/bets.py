frase = [p.lower() for p in input().split()]
frase = [p.replace('?', '') for p in frase]
palavra = input().lower()
valor = int(input())

if valor <= 100:
    print('EFETUADA')
elif palavra[0] == palavra[-1]:
    if valor > 500:
        saida = True
        for index, p in enumerate(frase):
            if p[0] != palavra[index]:
                saida = False
        if saida and valor % len(frase) == 0: 
            print('EFETUADA')
        else: 
            print('BLOQUEADA')
    else:
        print('BLOQUEADA')
else:
    saida = True
    for index, p in enumerate(frase):
        if p[0] != palavra[index]:
            saida = False
    if saida and valor % len(frase) == 0: 
        print('EFETUADA')
    else: 
        print('BLOQUEADA')