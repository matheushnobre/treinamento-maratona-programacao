n = int(input())
fila = input().split()
m = int(input())
sairam = input().split()

for p in sairam:
    fila.remove(p)
    
print(*fila)