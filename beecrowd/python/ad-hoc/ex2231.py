ct = 0
while True:
    ct += 1
    n, m = map(int, input().split())
    if n == 0: break
    lista = []
    for i in range(n):
        lista.append(int(input()))
    
    soma = sum(lista[:m])
    media = int(soma / m)
    menor = media
    maior = media
    
    for j in range(m, n):
        i = j-m
        soma -= lista[i]
        soma += lista[j]
        media = int(soma / m)
        maior = max(maior, media)
        menor = min(menor, media)
    
    print(f'Teste {ct}')
    print(f'{menor} {maior}')
    print()