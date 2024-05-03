"""
ID: matheus30
LANG: PYTHON3
TASK: friday
"""

fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

n = int(fin.readline())
day13 = [0]*7

dias = 13
ano = 1900
for i in range(n):
    if ano % 100 == 0:
        if ano % 400 == 0:
            isBissexto = True
        else:
            isBissexto = False
    elif ano % 4 == 0:
        isBissexto = True
    else:
        isBissexto = False
    
    ano += 1
        
    for j in range(12):
        day13[(dias%7+1)%7] += 1
        if j in [0, 2, 4, 6, 7, 9, 11]:
            dias += 31
        elif j in [3, 5, 8, 10]:
            dias += 30
        else:
            if isBissexto:
                dias += 29
            else:
                dias += 28

saida = ' '.join(map(str, day13))+'\n'
fout.write(saida)
fout.close()