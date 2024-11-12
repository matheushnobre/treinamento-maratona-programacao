t = int(input())
for _ in range(t):
    n = int(input())
    swit = list(map(int, input().split()))
    qtd1 = swit.count(1)
    if qtd1 % 2 == 0:
        minimo = 0
    else:
        minimo = 1
    if qtd1 <= n:
        maximo = qtd1
    else:
        maximo = n - (qtd1 - n)
    print(minimo, maximo)