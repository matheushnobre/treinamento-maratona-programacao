t = int(input())
for _ in range(t):
    n = int(input())
    lista = list(map(int, input().split()))
    
    saida = 100000000000000000000
    if n == 1:
        print(1)
    elif n % 2 == 1:
        for i in range(n):
            temp = 1
            j = 1
            while j < n:
                if j == i: 
                    j += 1
                    continue
                elif j-1 == i:
                    if j % 2 == 0:
                        temp = max(temp, lista[j]-lista[j-2])
                        j += 2
                    else:
                        j += 1
                else:
                    temp = max(temp, lista[j]-lista[j-1])
                    j += 2
            saida = min(saida, temp)
        print(saida)
    else:
        saida = 0
        for i in range(1, n, 2):
            saida = max(saida, lista[i]-lista[i-1])
        print(saida)