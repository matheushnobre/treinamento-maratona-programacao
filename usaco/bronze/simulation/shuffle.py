fin = open('shuffle.in', 'r')
fout = open('shuffle.out', 'w')

n = int(fin.readline())
emb = [int(i)-1 for i in fin.readline().split()]
vacas = fin.readline().split()

for i in range(3):
    antes = vacas.copy()
    for i in range(n):
        antes[i] = vacas[emb[i]]
    vacas = antes.copy()

saida = '\n'.join(vacas)
fout.write(saida)
fout.close()