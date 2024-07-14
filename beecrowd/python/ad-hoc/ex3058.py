n = int(input())
menor = None

for i in range(n):
    p, g = map(float, input().split())
    x = (1000*p)/g
    if menor is None or x < menor:
        menor = x
        
print(f'{menor:.2f}')