"""
ID: matheus30
LANG: PYTHON3
TASK: palsquare
"""

cb = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K'}

def conv(s, b):
    aux = []
    while s >= b:
        aux.append(s%b)
        s = s // b
    aux.append(s)
    
    saida = ''
    while len(aux) != 0:
        num = aux[-1]
        if num < 10:
            saida += str(aux[-1])
        else:
            saida += cb[num]
        del aux[-1]
    return saida

def isPalindrome(s):
    return s == s[::-1]

fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')

b = int(fin.readline())
for i in range(1, 300):
    quad = conv(i**2, b)
    if isPalindrome(quad):
        fout.write(f'{conv(i, b)} {quad}\n')