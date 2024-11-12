t = int(input())
for _ in range(t):
    n = int(input())
    lista = list(map(int, input().split()))
    maior = max(lista)
    menor = min(lista)
    soma = 0
    for i in range(n-1):
        soma += (maior-menor)
    print(soma)