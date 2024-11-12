j, r = map(int, input().split())
pont = [0]*j
lista = list(map(int, input().split()))

for i in range(j*r):
    pont[i%j] += lista[i]

s = 1
maior = 0
for i in range(j):
    if pont[i] >= maior:
        maior = pont[i]
        s = i+1
        
print(s)