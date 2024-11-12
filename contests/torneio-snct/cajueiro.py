dic = {0: 'FRANCISCO', 1: 'ALVES', 2: 'MENDES', 3: 'FILHO', 4: 'CHICO'}
lista = []
saida = []

for i in range(5):
    lista.append(int(input()))
maior = max(lista)

for i in range(5):
    if lista[i] == maior:
        saida.append(dic[i])

saida.sort()
print(*saida, sep=' ')