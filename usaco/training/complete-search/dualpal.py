"""
ID: matheus30
LANG: PYTHON3
TASK: dualpal
"""

def conv(s, b):
    aux = []
    while s >= b:
        aux.append(s%b)
        s = s // b
    aux.append(s)
    
    saida = ''
    while len(aux) != 0:
        saida += str(aux[-1])
        del aux[-1]
        
    return saida

def isPalindrome(s):
    return s == s[::-1]

def isDual(num):
    p = 0
    for i in range(2, 11):
        base = conv(num, i)
        if isPalindrome(base):
            p += 1
    return p >= 2
    

fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')

n, s = map(int, fin.readline().split())

enc, i = 0, s+1
while enc < n:
    if isDual(i):
        fout.write(str(i)+'\n')
        enc += 1
    i+=1
