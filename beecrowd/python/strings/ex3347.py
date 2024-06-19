n, p = map(int, input().split())

grupo = []
for i in range(p):
    grupo.append(input())
genoma = input()

i=0
while i < n:
    gp = genoma[i]
    iaux = i
    isaida = -1
    
    for index, g in enumerate(grupo):
        if g[i:iaux+1] == gp:
            while g[i:iaux+1] == genoma[i:iaux+1] and iaux < n:
                iaux+=1
            if isaida == -1 or iaux-i > len(gp): isaida = index+1
            iaux-=1
            gp = genoma[i:iaux+1]
            
    i = iaux+1
    
    print(gp, isaida)