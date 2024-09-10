v, n = map(int, input().split())
total = v * n

valor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for i in range(9):
    dez = total * valor[i]

    if dez % 1 != 0:
        dez = int(dez) + 1
        
    if i != 8:
        print(int(dez), end=' ')
    else:
        print(int(dez))