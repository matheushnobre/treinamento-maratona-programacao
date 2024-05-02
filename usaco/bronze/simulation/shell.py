fin = open('shell.in', 'r')
fout = open('shell.out', 'w')

jogo = [1, 2, 3]
escolhas = []

n = int(fin.readline())
for i in range(n):
    a, b, g = map(int, fin.readline().split())
    jogo[a-1], jogo[b-1] = jogo[b-1], jogo[a-1]
    escolhas.append(jogo[g-1])
    
mais, qtd = 0, 0
for i in range(1, 4):
    a = escolhas.count(i)
    if a > qtd:
        mais, qtd = i, a

fout.write(str(qtd))
fout.close()