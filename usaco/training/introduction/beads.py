"""
ID: matheus30
LANG: PYTHON3
TASK: beads
"""

fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

n = int(fin.readline())
s = fin.readline().strip()
s = s + s

maior = 0
corAtual = s[0]

for i in range(n):
    # Coletar a direita
    corAtual = ''
    d = 0
    for j in range(i, n*2):
        if s[j] == corAtual or s[j] == 'w' or corAtual == '':
            d += 1
            if corAtual == '' and s[j] != 'w':
                corAtual = s[j]
        else:
            break
    
    # Coletar para a esquerda
    corAtual = ''
    e = 0
    for j in range(i-1, -1, -1):
        if s[j] == corAtual or s[j] == 'w' or corAtual == '':
            e += 1
            if corAtual == '' and s[j] != 'w':
                corAtual = s[j]
        else:
            break
    
    maior = max(maior, e+d)
    
s = set(s)
if len(s) == 1:
    maior = n
elif len(s) == 2 and 'w' in s:
    maior = n

fout.write(str(maior)+'\n')
fout.close()