import time
t1 = time.time()

n = int(input())
lista = []
for i in range(n):
    lista.append(input())
lista.sort(key=len, reverse=True)

qtd = 0
for i in range(n):
    for j in range(i+1, n):
        if len(lista[i]) == len(lista[j]):
            if lista[i] == lista[j]:
                qtd += 2
        else:
            pass
            if lista[j] in lista[i]:
                qtd += 1
print(qtd)

t2 = time.time()
print(f'TEMPO = {t2-t1}s')