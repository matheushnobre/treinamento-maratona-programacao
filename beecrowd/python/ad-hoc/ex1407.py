while True:
    n, c, k = map(int, input().split())
    if n == c == k == 0: break
    
    cont = {int(i): 0 for i in range(1, k+1)}
    for i in range(n):
        for num in [int(i) for i in input().split()]:
            cont[num] += 1
    
    cont = sorted(cont.items(), key=lambda x:x[1])
    num = cont[0][1]
    l = []
    i = 0
    while cont[i][1] == num:
        l.append(cont[i][0])
        if i != k-1: i+=1
        else: break
    print(*l)