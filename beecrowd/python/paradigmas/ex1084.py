while True:
    n, d = map(int, input().split())
    if n == 0: break
    num = [int(i) for i in input()]
    
    saida = []
    for i in range(n):
        if d == 0:
            saida.append(num[i])
        else:
            while(d > 0 and len(saida) > 0 and saida[-1] < num[i]):
                del saida[-1]
                d -= 1
            saida.append(num[i])
        
    while(d>0):
        del saida[-1]
        d-=1
            
    print(*saida, sep='')

    