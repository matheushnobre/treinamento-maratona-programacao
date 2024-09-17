"""
ID: matheus30
LANG: PYTHON3
TASK: namenum
"""

fin = open('namenum.in', 'r')
fout = open('namenum.out', 'w')
dicionario = open('dict.txt', 'r')
dicionario = dicionario.read().split()
dicionario.sort()

guia = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PRS', 8: 'TUV', 9: 'WXY'}
n = fin.readline().strip()

saida = []
for palavra in dicionario:
    if len(palavra) == len(n):
        isPossivel = True
        for i in range(len(n)):
            if palavra[i] not in guia[int(n[i])]:
                isPossivel = False
                break
        if isPossivel:
            saida.append(palavra)
            
if len(saida) == 0:
    fout.write('NONE\n')
else:
    for p in saida:
        fout.write(p+'\n')