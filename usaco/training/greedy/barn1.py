'''
ID: matheus30
TASK: barn1
LANG: PYTHON3               
'''             

fin = open('barn1.in', 'r')
fout = open('barn1.out', 'w')

m, s, c = map(int, fin.readline().split())
fazenda = []
for i in range(c):
    fazenda.append(int(fin.readline()))
fazenda.sort()
    
# Formando grupos iniciais, apenas com vacas que estejam uma ao lado da outra
grupos = []
g = [fazenda[0]]
for vaca in fazenda[1:]:
    if vaca == g[-1]+1:
        g.append(vaca)
    else:
        grupos.append(g)
        g = [vaca]
grupos.append(g)

# Fazendo iteração para juntar os grupos de vacas mais próximos, a fim de termos no máximo M grupos
while len(grupos) > m:
    menorDistancia = 201
    index = p = None
    for i in range(len(grupos)):
        d1 = d2 = md = 201
        if i != 0:
            d1 = grupos[i][0] - grupos[i-1][-1]
        if i != len(grupos)-1:
            d2 = grupos[i+1][0] - grupos[i][-1]
        
        md = min(d1, d2)
        if md == d1:
            pt = -1
        else:
            pt = 1
            
        if md < menorDistancia:
            menorDistancia = md
            p = pt
            index = i
    
    if p == -1:        
        grupos[index-1].extend(grupos[index])
        del grupos[index]
    else:
        grupos[index].extend(grupos[index+1])
        del grupos[index+1]

# Calculando a resposta
saida = 0
for grupo in grupos:
    saida += grupo[-1] - grupo[0] + 1
fout.write(str(saida)+'\n')