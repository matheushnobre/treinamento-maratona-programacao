INF = 1e10

n = int(input())
lista = list(map(int, input().split()))
lista.sort()

menor = INF
for i in range(2):
    dif = 0
    for j in range(0, n, 2):
        dif += min(abs(lista[j] - lista[j+1]), 24 - abs(lista[j] - lista[j+1]))
    menor = min(menor, dif)
    lista = [lista[-1]] + lista[:-1]
        
print(menor)