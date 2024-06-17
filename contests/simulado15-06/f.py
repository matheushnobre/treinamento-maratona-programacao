t = int(input())

for _ in range(t):
    n = int(input())
    doces = [int(i) for i in input().split()]
    doces.sort()
    qtd = dist = 0
    
    for i in range(len(doces)):
        if doces[i] > dist:
            qtd += 1
            dist += doces[i]
    
    print(qtd, dist)