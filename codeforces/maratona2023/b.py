n = int(input())
lista = list(map(int, input().split()))
freq = {}

for i in lista:
    try:
        freq[i] += 1
    except KeyError:
        freq[i] = 1
    
s = 'N'
for i, n in freq.items():
    if n % 3 != 0:
        s = 'Y'
        
print(s)