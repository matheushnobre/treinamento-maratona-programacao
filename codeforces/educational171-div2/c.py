t = int(input())
for _ in range(t):
    n = int(input())
    entrada = input()
    saida = int((n*(n+1))/2)
    descontos = int(n/2)
    precisos = 0
    for i in range(n-1, -1, -1):
        if entrada[i] == '1' and descontos > 0 and i > precisos:
            saida -= i+1
            descontos -= 1
            precisos += 1
        else:
            precisos = max(0, precisos-1)
    print(saida)