fin = open('cowsignal.in', 'r')
fout = open('cowsignal.out', 'w')

m, n, k = map(int, fin.readline().split())
sinal = []
for i in range(m):
    sinal.append(fin.readline())
    
sinalAmplificado = []
for linha in sinal:
    novaLinha = ''
    for s in range(n):
        novaLinha += linha[s]*k
    for i in range(k):
        sinalAmplificado.append(novaLinha)

saida = '\n'.join(sinalAmplificado)
fout.write(saida)
fout.close()