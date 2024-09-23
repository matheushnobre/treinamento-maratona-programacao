n = int(input())
numbers = [0] * (n+1)
maior = n
lista = list(map(int, input().split()))

for valor in lista:
    numbers[valor] = 1
    if valor == maior:
        i = valor
        while numbers[i] == 1:
            print(i, end=' ')
            i -= 1
        maior = i
        print('')
    else:
        print('')