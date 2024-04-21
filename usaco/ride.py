"""
ID: matheus30
LANG: PYTHON3
TASK: ride
"""

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

fin = open('ride.in', 'r')
fout = open('ride.out', 'w')

e = fin.read().split('\n')
a = e[0]
b = e[1]

pa = 1
for l in a:
    pa *= (letters.index(l)+1)

pb = 1
for l in b:
    pb *= (letters.index(l)+1)
    
if pa % 47 == pb % 47:
    s = 'GO'
else:
    s = 'STAY'
    
fout.write(s+'\n')
fout.close()