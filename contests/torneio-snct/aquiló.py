n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
soma = 0
for i in range(1, n):
    soma += lista[i] - lista[i-1]
media = soma / n

if media % 1 != 0:
    media += 1

print(int(lista[-1] + media))