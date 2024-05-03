"""
ID: matheus30
LANG: PYTHON3
TASK: gift1
"""

fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

np = int(fin.readline())
grupo = {}
for i in range(np):
    pess = fin.readline().strip('\n')
    grupo[pess] = 0

for i in range(np):
    pess = fin.readline().strip('\n')
    if pess == '': break
    amt, div = map(int, fin.readline().split())
        
    try:
        val = amt // div
        rest = amt % div
        grupo[pess] -= (amt-rest)
    except ZeroDivisionError:
        continue
    
    for i in range(div):
        pess = fin.readline().strip('\n')
        grupo[pess] += val
        
saida = ''
for chave, valor in grupo.items():
    saida += chave + ' ' + str(valor) + '\n'

fout.write(saida)
fout.close()