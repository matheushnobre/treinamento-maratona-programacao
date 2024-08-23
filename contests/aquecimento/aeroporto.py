import sys
from math import sqrt

def ehPrimo(n):
    if n <= 1: return False
    elif n == 2: return True
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True    

primos = []
for i in range(10001):
    if ehPrimo(i):
        primos.append(True)
    else:
        primos.append(False)

input = sys.stdin.read
dados = input().split()
resultados = []

for linha in dados:
    n = int(linha)
    if primos[n]:
        resultados.append('PARALELO')
    else:
        resultados.append('CHATICE')
            
sys.stdout.write('\n'.join(resultados))         
    
