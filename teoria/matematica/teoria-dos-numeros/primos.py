import math

n = int(input())

# Algoritmo mais básico para verificar se um número N é primo:
# ehPrimo = True
# if n == 1: 
#     ehPrimo = False
# for i in range(2, n):
#     if n % i == 0:
#         ehPrimo = False
#         break
# print(f'{n} é primo.') if ehPrimo else print(f'{n} não é primo.')
        
# Algoritmo mais eficiente:
ehPrimo = True
if n == 1:
    ehPrimo = False
for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
        ehPrimo = False
        break
print(f'{n} é primo.') if ehPrimo else print(f'{n} não é primo.')