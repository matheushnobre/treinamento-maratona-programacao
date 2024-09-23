t = int(input())
for i in range(t):
    n = int(input())
    x, y = map(int, input().split())
    
    saida = n / min(x, y)
    if saida % 1 != 0:
        saida += 1
    print(int(saida))
    