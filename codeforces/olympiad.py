n = int(input())
lista = input().split()

times = []
qtd = 0
i, j, k = 0, 0, 0

while True:
    while i < n:
        if lista[i] != '1':
            i += 1
        else: break
    while j < n:
        if lista[j] != '2':
            j += 1
        else: break
    while k < n:
        if lista[k] != '3':
            k += 1
        else: break
    if i >= n or j >= n or k >= n: break
    times.append([i+1, j+1, k+1])
    i += 1
    j += 1
    k += 1
    qtd += 1

print(qtd)
for t in times:
    print(*t)