a, b = map(int, input().split())
s = list(input())

saida = 0
vb = []
vw = []
qb = 0
for i, c in enumerate(s):
    if c == 'B':
        qb += 1
        vb.append(i)
    else:
        vw.append(i)
        
while True:
    wr = None
    iwr = None
    bl = None   
    ibl = None 
    for index, i in enumerate(vw):
        if i < qb:
            wr = i
            iwr = index
        else:
            break
    
    for index, i in enumerate(vb):
        if i >= qb:
            bl = i
            ibl = index
            break

    if wr == None or bl == None: break
    if (((bl - wr) * a) - ((bl-wr) * b)) <= a:
        del vw[iwr]
        del vb[ibl]
        saida += (((bl - wr) * a) - ((bl-wr) * b))
    else:
        break

t = 0
for i in vw:
    if i < qb:
        t += 1
    else:
        break
    
v = t * a
saida += v
print(saida)
