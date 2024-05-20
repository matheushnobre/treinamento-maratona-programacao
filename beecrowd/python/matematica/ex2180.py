import math

def isPrime(n):
    if n == 1: return False
    i = 2
    while i*i <= n:
        if n % i == 0: return False
        i += 1
    return True

peso = int(input())
primos = []

while len(primos) != 10:
    if isPrime(peso):
        primos.append(peso)
    peso += 1
    
velocidade = sum(primos)
horas = 60000000 // velocidade
dias = horas // 24

print(f'{velocidade} km/h')
print(f'{horas} h / {dias} dias')